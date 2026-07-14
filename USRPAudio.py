#!/usr/bin/env python3
###################################################################################
# DVSwitch-USRP_Audio
# Copyright (C) 2014 - 2026 N4IRR
# Copyright (C) 2026 by DVSwitch KaT
# Py3 conversion + port fixes for EchoLink_Bridge
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
from time import time, sleep, localtime, strftime
import socket, struct, _thread, sys, pyaudio

RX_PORT = 3211   # bridge sends audio here
TX_PORT = 3210   # bridge reads audio from here
ipAddress = "127.0.0.1"

def rxAudioStream():
    global ipAddress
    FORMAT = pyaudio.paInt16
    CHUNK = 160
    CHANNELS = 1
    RATE = 8000

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    output=True, frames_per_buffer=CHUNK)

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp.bind(("", RX_PORT))

    lastKey = -1
    start_time = time()
    call = ''
    tg = ''
    loss = '0.00%'
    rxslot = '0'
    while True:
        soundData, addr = udp.recvfrom(1024)
        if addr[0] != ipAddress:
            ipAddress = addr[0]
        if soundData[0:4] == b'USRP':
            seq = struct.unpack(">i", soundData[4:8])[0]
            memory = struct.unpack(">i", soundData[8:12])[0]
            keyup = struct.unpack(">i", soundData[12:16])[0]
            talkgroup = struct.unpack(">i", soundData[16:20])[0]
            ptype = struct.unpack("i", soundData[20:24])[0]
            mpxid = struct.unpack(">i", soundData[24:28])[0]
            reserved = struct.unpack(">i", soundData[28:32])[0]
            audio = soundData[32:]
            if ptype == 0:  # voice
                if len(audio) >= 320:
                    stream.write(audio[:320], 160)
                if keyup != lastKey:
                    if keyup:
                        start_time = time()
                    else:
                        print('{} {} {} {} {} {} {:.2f}s\r'.format(
                            strftime(" %m/%d/%y", localtime(start_time)),
                            strftime("%H:%M:%S", localtime(start_time)),
                            call, rxslot, tg, loss, time() - start_time))
                    lastKey = keyup
            if ptype == 2:  # metadata
                if audio[0] == 8:
                    tg = (audio[9] << 16) + (audio[10] << 8) + audio[11]
                    rxslot = audio[12]
                    call = audio[14:].decode('ascii', errors='replace').rstrip('\x00')
        else:
            print(soundData, len(soundData))
    udp.close()

def txAudioStream():
    FORMAT = pyaudio.paInt16
    CHUNK = 160
    CHANNELS = 1
    RATE = 8000

#    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
#                    input=True, frames_per_buffer=CHUNK)

    stream = p.open(format=FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK,
                    input_device_index=None
                    )


    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    lastPtt = ptt
    seq = 0
    while True:
        try:
            audio = stream.read(160, exception_on_overflow=False)
            if ptt != lastPtt:
                usrp = b'USRP' + struct.pack('>iiiiiii', seq, 0, int(ptt), 0, 0, 0, 0)
                udp.sendto(usrp, (ipAddress, TX_PORT))
                seq += 1
                print('PTT: {}'.format(ptt))
            lastPtt = ptt
            if ptt:
                usrp = b'USRP' + struct.pack('>iiiiiii', seq, 0, 1, 0, 0, 0, 0) + audio
                udp.sendto(usrp, (ipAddress, TX_PORT))
                seq += 1
        except OSError:
            pass

def _find_getch():
    try:
        import termios, tty
    except ImportError:
        import msvcrt
        return msvcrt.getch
    import sys as _sys
    def _getch():
        fd = _sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return _sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return _getch

ptt = False

p = pyaudio.PyAudio()
_thread.start_new_thread(rxAudioStream, ())
_thread.start_new_thread(txAudioStream, ())

getch = _find_getch()
while True:
    ch = getch()
    if ch == '\x03':
        sys.exit(0)
    ptt = not ptt
