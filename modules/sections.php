<?php
  function fillDeviceSensorsTable(){
    // echo "<br/>";
    // var_dump($GLOBALS['configObj']);
    // echo "<br/>";

    //get number of devices
    $numDevices = getNumDevices();
    // echo "<br/>Num devices == $numDevices <br/>";

    //get device id's
    $devices = array();
    for($i=0;$i<$numDevices;$i++){
      $devices[$i] = getDeviceDetails($i);
    }
    // echo "Device details: <br/>";
    // var_dump($devices);
    // echo "<br/>";

    //get sensor values of each device
    $devValues = array();
    for($i=0;$i<$numDevices;$i++){
      $accessToken = getAccessToken($devices[$i]->{'accessID'});
      // echo "access Token = $accessToken <br/>";
      //get json blob of sensors on device
      echo "<div class='hidden'>";
      $valTemp=particleGetVariable($devices[$i]->{'deviceID'}, $accessToken, "sensorsJSON");
      echo "</div>";
      // echo "<br/>valTemp == $valTemp <br/>";
      if($valTemp !== -1){
        // echo "<br/>No error received<br/>";
        //get array of solenoid states
        $valTemp = json_decode($valTemp);
        // print_r($valTemp);
        $devValues = array_merge($devValues, $valTemp);
        // echo "<br/>devValues: <br/>";
        // print_r($devValues);
        // echo "<br/>";
      }else{
        //ERROR getting particle variable
        // echo "ERROR: Particle Variable not accessable<br/>";
      }
    }
    // var_dump($devValues);

    // make list for sensor Values
    echo "<table class='deviceStatusTable'>";
    // headings
    echo "<tr><th>SENSOR</th><th>Temp</th></tr>";
    $numSensors = count($GLOBALS['configObj']->{'sensors'});
    // echo "<br/>Num Sensors: $numSensors";
    for($i=0;$i<$numSensors;$i++){
      echo "<tr>";
      echo "<td>".$GLOBALS['configObj']->{'sensors'}[$i]->{'name'}."</td>";
      echo "<td>";
      // search $devValues for sensor address and return temp
      echo getSensorTemp($devValues,$GLOBALS['configObj']->{'sensors'}[$i]->{'address'});
      echo "</td>";
      echo "</tr>";
    }
    echo "</table>";
    echo "<hr>";
  }

  function getSensorTemp($records,$address){
    $record=0;
    while(($record < count($records)) and ($records[$record]->{'address'} != $address)){
      $record++;
    }
    if($record >= count($records)){
      //sensor address not found
      return "error";
    }else{
      return $records[$record]->{"temp"};
    }
  }
?>
