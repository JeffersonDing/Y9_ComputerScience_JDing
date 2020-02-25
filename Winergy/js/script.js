var years = [2000,
2001,
2002,
2003,
2004,
2005,
2006,
2007,
2008,
2009,
2010,
2011,
2012,
2013,
2014,
2015,
2016];
var World = 
[17.29,
17.04,
17.05,
16.85,
16.51,
16.33,
16.27,
16.15,
16.29,
16.81,
16.56,
16.63,
16.89,
17.06,
17.18,
17.24,
17.48];
var NorthAmerica = 
[7.3,
6.57,
6.82,
7.15,
7.32,
7.72,
8.18,
8.15,
8.67,
9.18,
9.1,
10.06,
10.46,
10.81,
10.86,
10.76,
11.11];
var Africa = 
[60.84,
60.42,
60.01,
59.38,
59.39,
58.28,
58.15,
57.49,
57.2,
57.23,
57.3,
57.25,
56.34,
55.47,
55.4,
55.7,
55.63];
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
	
  data: {
    labels: years,
    datasets: [
		{ 
		label:"North America Percentage",
        data: NorthAmerica,
		backgroundColor:'rgba(0,139,248,0.6)'
      },
      { 
		label:"World Percentage",
        data: World,
		backgroundColor:'rgba(4,231,98,0.5)'
      },
		{ 
		label:"Africa Percentage",
        data: Africa,
		backgroundColor:'rgba(245,183,0,0.4)'
      }
		
    ]
  },
	options: {
        title: {
            display: true,
            text: 'Renewable energy share in the total final energy consumption (%)',
			fontSize:21,
			
        }
    }
});




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
