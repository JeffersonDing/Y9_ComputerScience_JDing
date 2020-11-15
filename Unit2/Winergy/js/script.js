function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }
}
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var indexts = document.getElementsByClassName("indext");
  if (n > slides.length) {
    slideIndex = 1
  }
  if (n < 1) {
    slideIndex = slides.length
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < indexts.length; i++) {
    indexts[i].className = indexts[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  indexts[slideIndex - 1].className += " active";
	if(slideIndex === 1){
		document.getElementById("label").innerHTML = "Envision Group: ";
		document.getElementById("impact").innerHTML = "Envision Energy is the first in the industry to develop 'smart turbine' with its exclusive core technology of smart control,advanced measurement method, expert data analysis system, active performance control and reliability-based deterministic turbines. The effective combination and application of these ground-breaking technologies have enabled these turbines to accurately perceive their own status and external environmental conditions. This ensures that the turbine will always function at its optimal working condition for maximum power generation and longer service life. Through a “software-defined turbine” approach, Envision Energy has surpassed the technological limits of traditional wind turbines, and increased the efficiency of wind power generation by 15%. "
	}else if(slideIndex === 2){
	document.getElementById("label").innerHTML = "Vestas: ";
		document.getElementById("impact").innerHTML = "Vestas is the energy industry’s global partner on sustainable energy solutions. We design, manufacture, install, and service wind turbines across the globe, and with +113 GW of wind turbines in 81 countries, we have installed more wind power than anyone else. Through our industry-leading smart data capabilities and +96 GW of wind turbines under service, we use data to interpret, forecast, and exploit wind resources and deliver best-in-class wind power solutions. Together with our customers, Vestas’ more than 25,000 employees are bringing the world sustainable energy solutions to power a bright future.";
	}else if(slideIndex===3){
		document.getElementById("label").innerHTML = "WES: ";
		document.getElementById("impact").innerHTML = "Our mission is to bring renewable energy everywhere!  We believe that wind energy solutions can and should be applied in virtually any situation. As long as there is sufficient wind and a demand for a reliable and renewable source of electricity, WES has a wind energy solution that works for you!";
	}else{
		console.log("Error!")
	}

}
var yvalue ;
window.addEventListener("scroll", function (event) {
	document.querySelector("#bg-modal").style.display="none";
    yvalue = this.scrollY;
});
function expand(){
	document.querySelector("#bg-modal").style.top=`${yvalue}px`;
	document.querySelector("#bg-modal").style.display="flex";
}
function close(){
	document.querySelector("#bg-modal").style.display="none";
}
document.getElementById("windspeed").addEventListener("click",expand)
document.querySelector("#close").addEventListener("click",close)
