<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="pinterest" content="nopin" />
    <meta name="pinterest" content="nohover" />

    <meta name="3778517eb4810dfb5d143ed8f1b359b3b5a82923" content="0f56257c3db4a222e91b11bc6871c4df2e263b28" />

    <link rel="apple-touch-icon" sizes="57x57" href="/img/org.1/favicons/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/img/org.1/favicons/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/img/org.1/favicons/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/img/org.1/favicons/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/img/org.1/favicons/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/img/org.1/favicons/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/img/org.1/favicons/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/img/org.1/favicons/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/img/org.1/favicons/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192"  href="/img/org.1/favicons/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/img/org.1/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/img/org.1/favicons/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/img/org.1/favicons/favicon-16x16.png">

    <link rel="icon" type="image/x-icon" href="/img/org.1/favicons/favicon.ico" />

    
    <link rel="stylesheet" href="/bootstrap/3.3.6/css/bootstrap.min.css">
    <link rel="stylesheet" href="/bootstrap/3.3.6/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="/css/header.css?v=1">
    <link rel="stylesheet" href="/css/groupsio.css?v=6">

        

            

    <script src="/js/jquery-1.11.1.min.js"></script>
    
    <script src="/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <link href="/fontawesome/5.9.0/css/all.min.css" rel="stylesheet">
    
    
    




    




<title>Log In</title>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="/css/bootstrap-social.css">
<script src="/js/jstz.min.js"></script>
</head>
<body class="fuelux">


<div class="navbar navbar-head" role="navigation" id="headerbar">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#headerCollapse">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>
    <a href="https://groups.io" class="navbar-left"><img src="https://groups.io/img/org.1/mainlogo.png" height="50"></a>
  </div>
  <div id="headerCollapse" class="collapse navbar-collapse">
    
      <ul class="nav navbar-nav">
        <li><a href="https://groups.io/search?p=SubsCount,,,20,2,0,0"><i class="fa fa-search"></i> Find or Create a Group</a></li>
          
      </ul>
    

    <ul class="nav navbar-nav pull-right">
      <li><a href="https://groups.io/static/help"><i class="fa-fw fa fa-info-circle"></i> Help</a></li>
      <li><a href="https://groups.io/login"><i class="fa fa-sign-in-alt"></i> Log In</a></li>
      
        <li><a href="https://groups.io/register"><i class="fa fa-user"></i> Sign Up</a></li>
      
    </ul>
  </div>
</div>



<div id="content" class="container-fluid">





<div id="alertdiv"></div>

<div class="noticetemplate template">
	<div class="alert alert-success alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		<span id="msg"></span>
	</div>
</div>
<div class="alerttemplate template">
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		<span id="msg"></span>
	</div>
</div>




<script>
var $alerttemplate = $(".alerttemplate");
var $noticetemplate = $(".noticetemplate");
function createAlert(msg, isError, autoClose) {
	if (isError == false) {
		$newPanel = $noticetemplate.clone();
	} else {
		$newPanel = $alerttemplate.clone();
	}
	$newPanel.find("#msg").html(msg);
	if (autoClose == true) {
		$("#alertdiv").append($newPanel.fadeTo(2000, 500).slideUp(500, function(){
		    $newPanel.slideUp(500);
		    $newPanel.remove();
		}));  	
	} else {
		$("#alertdiv").append($newPanel.fadeIn());
	}
}


</script>


<div class="row">
  <div class="col-md-offset-2 col-md-8">

<form role="form" method="POST" action="/login">
  <input type="hidden" id="timezone" name="timezone" value="">
  <input name="r" type="hidden" value="/g/main/files/USRPAudio.py">
<div class="form-group">
<h4>Please Log In</h4>
</div>
<div class="form-group">
  <label for="email">Email Address</label>
    <input name="email" id="email" class="form-control" type="text" required autofocus>
    
      <p class="help-block"></p>
    
</div>
<div class="form-group">
  <label for="email">Password</label>
    <input name="password" class="form-control" type="password" required>
    
      <p class="help-block"><a href="#" onclick="missingPassword();return false;">Forgot your password, or don't have one yet?</a></p>
    
</div>


<p>Our site uses cookies so that we can remember you and understand how you and other visitors use our site, to improve your browsing experience and help us improve our site. By continuing to use our website, you agree to our use of such cookies. <a href="/static/cookie_policy">Learn more</a></p>


<div class="form-group">
  <button class="btn btn-success btn-sm" id="submit" type="submit"><i class="fa fa-sign-in-alt"></i> Log In</button>
</div>

<div class="form-group">
<h4>Or You Can</h4>
</div>

<div class="form-group">
  <div class="row">
    <div class="col-md-4">
    <a class="btn btn-block btn-social btn-reddit bottom10" href="#" onclick="loginLink();return false;">
      <i class="fa fa-paper-plane"></i> Email me a link to log in
    </a>
    </div>
    <div class="col-md-4">
    <a class="btn btn-block btn-social btn-facebook bottom10" href="/facebookstartauth?r=%2fg%2fmain%2ffiles%2fUSRPAudio.py">
      <i class="fab fa-facebook"></i> Log in with Facebook
    </a>
    </div>
    <div class="col-md-4">
    <a class="btn btn-block btn-social btn-facebook bottom10" href="/googlestartauth?r=%2fg%2fmain%2ffiles%2fUSRPAudio.py" style="font-family: 'Roboto', sans-serif;background-color:#fff;color:#333">
      <img width="18px" alt="Google &quot;G&quot; Logo" src="/img/google_logo.png" style="width:22px;border-right:0;margin-left:4px; margin-top:5px" />
      Log in with Google
    </a>
    </div>
  </div>
</div>
</form>

<div class="form-group">
<h4>Not Sure?</h4>
</div>


<p>Are you receiving emails from a Groups.io group but have never visited the Groups.io website? You probably don't have a password set up yet. Use the <b>Email me a link to log in</b> button above to log into the website.</p>
<p>Don't have a Groups.io account? <a href="/register">Registration</a> is free and easy.</p>

  </div>
</div>

<script>
  var tz = jstz.determine();
  $('#timezone').val(tz.name());

function loginLink() {
  var email = $("#email").val();
  if (email != "") {
    form = '<form id="sllform" action="/sendloginlink" method="POST">' + 
      '<input type="hidden" name="email" value="' + email + '">' +
      '<input type="hidden" name="r" value="\/g\/main\/files\/USRPAudio.py">' +
      '</form>'
    $(document.body).append(form);
    $('form#sllform').submit();
    return;
  }
  form = '<form id="sllform" action="/sendloginlink" method="POST">' + 
    '<input type="hidden" name="r" value="\/g\/main\/files\/USRPAudio.py">' +
    '</form>'
  $(document.body).append(form);
  $('form#sllform').submit();
}

function missingPassword() {
  var email = $("#email").val();
  if (email != "") {
    form = '<form id="sllform" action="/sendloginlink" method="POST">' + 
      '<input type="hidden" name="email" value="' + email + '">' +
      '<input type="hidden" name="r" value="/account">' +
      '</form>'
    $(document.body).append(form);
    $('form#sllform').submit();
    return;
  }
  form = '<form id="sllform" action="/sendloginlink" method="POST">' + 
    '<input type="hidden" name="r" value="/account">' +
    '</form>'
  $(document.body).append(form);
  $('form#sllform').submit();
}
</script>

    </div>

<div class="scroll-top-wrapper">
  <span class="scroll-top-inner">
    <i class="fa fa-arrow-circle-up fa-fw fa-2x" style="vertical-align:-.25em"></i>
  </span>
</div>

<p><br>

<div class="hidden-xs" id="footer">
  <div class="navbar navbar-default" role="footer">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#footercollapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
    </div>
    <div class="collapse navbar-collapse" id="footercollapse">
      <ul class="nav navbar-nav">

        <li><a href="https://groups.io/static/about">About</a></li>
        <li><a href="https://groups.io/static/transfer">Easy Group Transfer</a></li>
        <li><a href="https://groups.io/static/features">Features</a></li>
        <li><a href="https://groups.io/static/pricing">Pricing</a></li>
        <li><a href="https://groups.io/g/updates/messages?expanded=1">Updates</a></li>
        <li><a href="https://groups.io/static/tos">Terms</a></li>
        <li><a href="https://groups.io/static/help">Help</a></li>
        <li><a href="http://twitter.com/groupsio" target="_blank"><i class="fab fa-twitter fa-lg"></i></a></li>

      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><p class="navbar-text">&copy; <span class="hidden-sm">2019 </span> Groups.io</p></li>
      </ul>
    </div>
  </div>
<script>

$(function(){
  $(document).on( 'scroll', function(){
    if ($(window).scrollTop() > 100) {
      $('.scroll-top-wrapper').addClass('show');
    } else {
      $('.scroll-top-wrapper').removeClass('show');
    }
  });
  $('.scroll-top-wrapper').on('click', scrollToTop);
});
 
function scrollToTop() {
  verticalOffset = typeof(verticalOffset) != 'undefined' ? verticalOffset : 0;
  element = $('body');
  offset = element.offset();
  offsetTop = offset.top;
  $('html, body').animate({scrollTop: offsetTop}, 100, 'linear');
}
</script>

    
    

</div>

</body>
</html>
