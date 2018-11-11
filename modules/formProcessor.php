<?php

  if(isset($_GET['function'])){
    // var_dump($_GET['override']);
    // $override = json_decode($_GET['override']);
    // var_dump($override);
    // echo "<br/>device = ".$override[0]."<br/>";
    // echo "solenoid = ".$override[1];
    // echo "<br/><br/>";

    // if function is 'turnOn'
    if($_GET['function'] == 'turnOn'){
      // check if a run time was provided
      if($_GET['time'] == ''){
        $_GET['time'] == 0;
      }
      postToQueue($_GET['function'],(int)$_GET['device'],(int)$_GET['access'],$_GET['solenoid'],$_GET['time']);

    }

    // if function is 'turnOff'
    if($_GET['function'] == 'turnOff'){
      postToDevice($_GET['function'],(int)$_GET['device'],(int)$_GET['access'],255,0);
    }
    header('Location: index.php');

  }elseif(isset($_GET['solenoid'])){  //for testing
    particleFunctionCall("200033000b47363433353735", getAccessToken(0), "turnOn", $_GET['solenoid'],$_GET['time']);


  }


  function postToDevice($function,$deviceNum, $accessToken, $solenoid,$time){
    // echo "postToDevice() $function, $deviceNum, $accessToken, $command<br/>";
    // get device ID
    // echo "<br/>DeviceID $deviceID == ";
    // echo getDeviceID($deviceID);
    // $deviceID = getDeviceID($deviceID);
    // echo "$deviceID <br/>";
    // echo "<br/>Acess Token == ".getAccessToken()."<br/>";

    particleFunctionCall(getDeviceID($deviceNum), getAccessToken($accessToken), $function, $solenoid,$time);

  }
  function postToQueue($function,$deviceNum, $accessToken, $solenoid,$time){
    sendCommandToQueue(getDeviceID($deviceNum),$function, $solenoid, $time, getDeviceName($deviceNum));

  }
?>
