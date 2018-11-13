<?php
	//start the session
	session_start();
  $pageHeading = "Home Page";

  // echo "SESSION data: ";
	// print_r($_SESSION);
	// echo "<hr/>";
	// echo "POST data: ";
	// print_r($_POST);
	// echo "<hr/>";
	// echo "GET data: ";
	// print_r($_GET);
	// echo "<hr/>";
	/**************************************
	*INSERT IMPORTANT PHP FILES HERE
	***************************************/

  include_once('./modules/fileHandling.php');
	include_once('./modules/globals.php');
	include_once('./modules/sections.php');
	include_once('./modules/communication.php');
  include_once('./modules/formProcessor.php');
?>

<!DOCTYPE>
<html>
  <head>
    <title>Temperature Sensors</title>
    <link rel="stylesheet" href="./css/styles.css?version=0.11">
    <script src="./js/js1.js"></script>
    <!--
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
    -->
  </head>

  <body>
    <div id="Sensors">
      Sensors
			<?php fillDeviceSensorsTable();?>
    </div>
		<div id="testingWrapper">
      Testing
			<!-- <form action='./index.php'method='get'>
				<input type="number" name="solenoid">
				<input type="number" name="time">
				<input type="submit" value="submit">
			</form> -->
    </div>

  </body>
</html>
