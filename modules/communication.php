<?php
function particleFunctionCall($device, $accessToken, $function, $solenoid, $time) {
  // example: {"solenoid":7,"time":25,"functName":"turnOn","deviceID":"200033000b47363433353735"}
  // send command directly to device (bypassthe queue)

  $args = '{\"data\":\"'.$solenoid.','.$time.'\",\"functName\":\"'.$function.'\",\"deviceID\":\"'.$device.'\",\"accessToken\":\"'.$accessToken.'\"}';
  $cmd = "python3.6 ./python/particleFunction.py";
  exec($cmd.' '.$args);
}

function particleGetVariable($device, $accessToken, $variable){
  // echo "particleGetVariable--------------<br/>";
  // echo "   device $device <br/>";
  // echo "   accessToken $accessToken <br/>";
  // echo "   variable $variable <br/>";
  $args = '{\"varName\":\"'.$variable.'\",\"deviceID\":\"'.$device.'\",\"accessToken\":\"'.$accessToken.'\"}';
  $cmd = "python3.6 ./python/particleVariable.py";
  $result = exec($cmd.' '.$args,$out,$status);
  // echo "Exit Status: $status <br/>";
  if($status != 0){
    return -1;
  }

  echo "Result: $result<br/>";
  return $result;

  // open deviceFile from python folder
  // echo getPinIntValue($device)."<br/>";
  // return getDeviceVariable($device,$variable);

  // read contents
  // create object from json
  // return 'pinIntValues'
}
?>
