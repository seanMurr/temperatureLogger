<?php

  function getConfigObj(){
    // echo "Filename: ".$GLOBALS['configFileName']." <br/>";
    $fh = fopen($GLOBALS['configFileName'],'r')
			or die("Unable to open file!");

    $configJson = fread($fh, filesize($GLOBALS['configFileName']));
    fclose($fh);
    // print($configJson);
    // $configObj = json_decode($configJson);
    // var_dump($configObj); //->{'devices'}[0]->{'name'};
    return json_decode($configJson);
  }

  function getDeviceVariable($device,$variable){
    $fh = fopen("./python/".$device.'.txt','r')
			or die("Unable to open file! ".$deviceID.'.txt');

    $deviceJson = fread($fh, filesize("./python/".$device.'.txt'));
    fclose($fh);
    $deviceObj = json_decode($deviceJson);
    return $deviceObj->{$variable};
  }

  function sendCommandToQueue($device,$function, $solenoid, $time, $deviceName){
    $fh = fopen("./python/queue.txt", "a") or die("Unable to open file! ./python/queue.txt");
    // // {"solenoid":7,"time":25,"functName":"turnOn","deviceID":"200033000b47363433353735"}
    $txt = "{\"solenoid\":\"$solenoid\",\"time\":\"$time\",\"functName\":\"$function\",\"deviceID\":\"$device\",\"deviceName\":\"$deviceName\"}";
    fwrite($fh, $txt."\n");
    fclose($fh);
  }

  function getDeviceID($id){
    // $confObj = getConfigObj();
    // var_dump($confObj);
    return $GLOBALS['configObj']->{'devices'}[$id]->{'deviceID'};
  }

  function getDeviceName($id){
    return $GLOBALS['configObj']->{'devices'}[$id]->{'name'};
  }

  function getAccessToken($id){
    // $confObj = getConfigObj();
    // echo "<br/> confObj <br/>";
    // var_dump($confObj);
    return $GLOBALS['configObj']->{'accessToken'}[$id];
  }

  function getNumDevices(){
    // $confObj = getConfigObj();
    // echo "<br/> confObj <br/>";
    // var_dump($GLOBALS['configObj']);
    return count($GLOBALS['configObj']->{'devices'});
  }

  function getDeviceDetails($id){
    // $confObj = getConfigObj();
    // var_dump($confObj);
    return $GLOBALS['configObj']->{'devices'}[$id];
  }
?>
