

function updateTime(){
  // for each element with name = 'time'
  // change value of time to
  // value of element id='runTime'
  var els = document.getElementsByName("time");
  var i;
  for (i = 0; i < els.length; i++) {
      els[i].value = document.getElementById("runTime").value * 60;
  }
}
