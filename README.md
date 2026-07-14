This updated version of `USRPAudio.py` reflects the current Python 3 implementation for your DVSwitch environment.

---

### Overview

`USRPAudio.py` is a lightweight Python 3 bridge that enables full-duplex VoIP-to-Radio audio streaming. It uses UDP to communicate with a bridge (such as `Analog Reflector`) and uses `PyAudio` to interface with your system's sound card.

### Key Components

#### 1. Audio Processing Threads

The script uses `_thread` to manage two concurrent streams, ensuring that audio input and output can happen simultaneously without blocking.

* **`rxAudioStream` (Port 3211)**:
* Listens for incoming UDP packets with the `USRP` header.
* **Voice Handling**: Identifies `ptype 0` packets and writes the 160-sample payload to the local audio device.
* **Metadata Handling**: Identifies `ptype 2` packets to parse Talkgroup IDs, RX slots, and call signs.
* **Logging**: Tracks session timing and displays key-up/key-down event details to the console.


* **`txAudioStream` (Port 3210)**:
* Captures 160-sample chunks from the default system input device.
* Sends data to the `ipAddress` identified by the RX thread.
* **PTT Logic**: Monitors the global `ptt` variable. When the state changes, it sends a specific `USRP` control packet to the bridge to toggle transmission.



#### 2. Control Mechanism

* **Manual Toggle**: The script uses `_find_getch` to provide cross-platform terminal input. The `while True` loop at the bottom captures a keystroke; if you press any key (other than `Ctrl+C` which triggers a clean exit), it toggles the `ptt` flag.
* **Configuration**:
* `RATE = 8000`: Audio is sampled at 8 kHz.
* `CHUNK = 160`: Data is processed in 20ms frames (160 samples at 8kHz).


---

### Technical Architecture

The following diagram illustrates how your Work Station sits between the digital network bridge and the local audio hardware.

### Implementation Notes for Your Setup

* **Network Behavior**: The script dynamically sets the `ipAddress` to the source of the last received UDP packet. This ensures that the TX stream always points back to the bridge that is currently talking to it.
* **Exception Handling**: `txAudioStream` includes a `try-except` block for `OSError` to maintain stability if the audio buffer overflows or if the device index becomes unavailable during runtime.
* **Dependencies**: Ensure your server environment has `pyaudio` installed and that the user running the script has permission to access the audio hardware (often requiring `audio` group membership on Linux).
