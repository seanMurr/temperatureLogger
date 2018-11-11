<?php
  function fillOverideDiv(){
    echo "<br/><br/>";

    // echo "<br/>Num devices:  ";
    // echo count($config->{"devices"});
    // echo "<br/>Num sections:  ";
    // echo count($config->{'sections'});
    // echo "<br/>";

    // runtime input
    echo "<label class='runTime'>Run time: </label>";
    echo '<input type="number" id="runTime" value="3" onchange="updateTime()">';
    echo "<label class='runTime'> Minutes </label><br/>";
    // each section has own form
    for($i=0;$i<count($GLOBALS['configObj']->{'sections'});$i++){
      echo "<form action='./index.php' method='get'>";
      // $inputName = $GLOBALS['configObj']->{'sections'}[$i]->{'name'};
      // $inputValue = "[".$GLOBALS['configObj']->{'sections'}[$i]->{'device'}.
      //               ",".$GLOBALS['configObj']->{'sections'}[$i]->{'accessID'}.
      //               ",".$GLOBALS['configObj']->{'sections'}[$i]->{'solenoids'}."]";
      // echo "$inputName - $inputValue <br/>";
      //function to be ccalled
      echo "<input type='hidden' class='btn' name='function' value='turnOn'>";
      //index of deviceID in configuration file
      echo "<input type='hidden' class='btn' name='device' value='".$GLOBALS['configObj']->{'sections'}[$i]->{'device'}."'>";
      //index of accessToken in configuration file
      echo "<input type='hidden' class='btn' name='access' value='".$GLOBALS['configObj']->{'sections'}[$i]->{'accessID'}."'>";
      //solenoid data
      echo "<input type='hidden' class='btn' name='solenoid' value='".$GLOBALS['configObj']->{'sections'}[$i]->{'solenoids'}."'>";
      //run time in seconds
      echo "<input type='hidden' class='btn' name='time' value='180'>";
      // input button has label of section->name
      echo "<input type='submit' class='btn_override' value='".$GLOBALS['configObj']->{'sections'}[$i]->{'name'}."'>";
      echo "<br/>";
      echo "</form>";
    }
    echo "<hr>";
  }

  function fillDeviceStatusDiv(){
    //get number of devices
    // var_dump($GLOBALS['configObj']);
    $numDevices = getNumDevices();
    // echo "<br/>Num devices == $numDevices";

    //get device id's
    $devices = array();
    for($i=0;$i<$numDevices;$i++){
      $devices[$i] = getDeviceDetails($i);
    }
    // for($i=0;$i<$numDevices;$i++){
    //   echo "<br/>device $i == ".$devices[$i]->{'name'}."  ".$devices[$i]->{'deviceID'}."<br/>";
    // }
    //get solenoid values of each device
    $devValues = array();
    for($i=0;$i<$numDevices;$i++){
      $accessToken = getAccessToken($devices[$i]->{'accessID'});
      //get int value of solenoid states
      $valTemp=particleGetVariable($devices[$i]->{'deviceID'}, $accessToken, "pinIntValue");
      // echo "<br/>valTemp == $valTemp <br/>";
      if($valTemp !== -1){
        // echo "<br/>No error received<br/>";
        //get array of solenoid states
        $devValues[$i] = array();
        $valTemp = (int)$valTemp;
        for($s=8;$s>=0;$s--){
          if($valTemp/pow(2,$s)>=1){
            $devValues[$i][$s] = 1;
          }else{
            $devValues[$i][$s] = 0;
          }
          $valTemp = $valTemp % pow(2,$s);
        }
      }else{
        //ERROR getting particle variable

      }
    }
    // var_dump($devValues);
    // make list for device pinValues
    echo "<table class='deviceStatusTable'>";
    // headings
    echo "<tr><th>DEVICE</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th></tr>";

    for($i=0;$i<$numDevices;$i++){
      echo "<tr>";
      echo "<td>".$devices[$i]->{'name'}."</td>";
      //check for communication error
      if(!is_array($devValues[$i])){
        // comms error
        echo "<td colspan='8'>Communication error</td>";
      }else{
        for($j=0;$j<8;$j++){
          echo "<td>".$devValues[$i][$j]."</td>";
        }
        echo "<td>";
        // turn off button
        echo "<form action='./index.php' method='get'>";
        // $inputName = $GLOBALS['configObj']->{'sections'}[$i]->{'name'};
        // $inputValue = "[".$GLOBALS['configObj']->{'sections'}[$i]->{'device'}.
        //               ",".$GLOBALS['configObj']->{'sections'}[$i]->{'accessID'}.
        //               ",".$GLOBALS['configObj']->{'sections'}[$i]->{'solenoids'}."]";
        // echo "$inputName - $inputValue <br/>";
        //function to be ccalled
        echo "<input type='hidden' class='btn' name='function' value='turnOff'>";
        //index of deviceID in configuration file
        echo "<input type='hidden' class='btn' name='device' value='".$i."'>";
        //index of accessToken in configuration file
        echo "<input type='hidden' class='btn' name='access' value='".$devices[$i]->{'accessID'}."'>";
        // input button has label of section->name
        echo "<input type='submit' class='btn_deviceStatus' value='Turn Off'>";
        echo "<br/>";
        echo "</form>";
        echo "</td>";
      }
      echo "</tr>";
    }
    echo "</table>";
    echo "<hr>";
  }

  function fillTimersDiv(){

  }
?>
