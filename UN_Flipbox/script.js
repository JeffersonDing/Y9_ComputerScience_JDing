// JavaScript Document
 //This script gets run once when the program starts. 
  var  w = window.innerWidth   //Takes window object and stores width in w
  //A conditional statement that checks w
  if (w > 940) {

    document.getElementsByClassName("flex-container")[0].style.marginTop = "200px";
  }
  else {
    document.getElementsByClassName("flex-container")[0].style.marginTop = "280px";
  }
	window.addEventListener('resize', function(event){
  
    w = window.innerWidth

    if (w > 940) {

      document.getElementsByClassName("flex-container")[0].style.marginTop = "200px";

    }
    else {
      document.getElementsByClassName("flex-container")[0].style.marginTop = "280px";
    }
});
