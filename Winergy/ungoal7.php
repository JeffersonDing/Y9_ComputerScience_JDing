<?php
include_once( "./includes/Connection.php" )
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Winergy®</title>
<link href="css/style.css" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script> 
</head>
<body>
<div id="ungoal7">
  <nav id="siteNav" class="navbar" >
    <div id="navbar">
      <ul id="ulnavbar">
        <li> <a class="logo" href="./index.html"> <img id="logo" src="images/Colab.png" alt="Logo"/></a> </li>
        <li class="active"> <a href="./index.html">Home</a> </li>
        <li> <a href="./The_Problem.html">The Problem</a> </li>
        <li >
          <div class="dropdown">
            <button class="dropbtn" onclick="myFunction()">UN Goals </button>
            <div class="dropdown-content" id="myDropdown"> <a href="./ungoal7.html">Goal 7</a> <a href="./ungoal11.html">Goal 11</a> </div>
          </div>
        </li>
        <li> <a href="./solution.html">Solutions</a> </li>
      </ul>
    </div>
  </nav>
  <center>
    <div class="ungoal intro">
      <h1>UN Goal 7</h1>
      <p>Affordable and Clean Energy</p>
    </div>
  </center>
</div>
<div class="text-grid-container">
  <div class="body-left">
    <h2>Electricity Generation</h2>
    <h1>Wind Turbines (Offshore)</h1>
    <div class="caption"> An athlete swims past the Sheringham Shoal Offshore Wind Farm off the coast of Norfolk, England. The wind farm consists of 88 Siemens 3.6 megawatt turbines placed over a 35-square kilometer area, 11 miles from shore. </div>
    <div class="description">
      <p>Wind energy is at the crest of initiatives to address global warming in the coming three decades. Investment in offshore wind was $29.9 billion in 2016, 40 percent greater than the prior year.</p>
      <p>32 turbines—each double the height of the Statue of Liberty—have been installed off the coast of Liverpool, England. Owned by Lego, the toy maker, this is an international effort: The blades are made on the Isle of Wight by a Japanese company for its Danish client, Vestas. Each turbine generates 8 megawatts of electricity; together, they will supply all 466,000 inhabitants of Liverpool.</p>
      <p>The wind industry is marked by a proliferation of turbines, dropping costs, and heightened performance. In many locales, wind is either competitive with or less expensive than coal-generated electricity—and it has no fuel costs and no pollution. Yet, not-in-my-backyard sentiment remains an obstacle in many places.</p>
      <p>The variable nature of wind means there are times when turbines are not turning. Wind energy, like other sources of energy, is part of a system. Investment in 24-7 renewables such as geothermal, energy storage, transmission infrastructure, and distributed generation is essential to its growth.</p>
    </div>
  </div>
  <div class="sidebar-right">
    <div class="ranking-results">
      <div class="rank-number"> <sup>#</sup>22 </div>
      <div class="rank-desc"> Rank and Results by 2050 </div>
      <div class="rank-stats">
        <div class="stat"><span class="stat-value">14.1</span><span class="stat-unit"> gigatons</span><br>
          reduced CO2</div>
        <div class="stat"><span class="stat-value">$545.3</span><span class="stat-unit"> Billion</span><br>
          net implementation cost</div>
        <div class="stat"><span class="stat-value">$762.5</span><span class="stat-unit"> Billion</span><br>
          net operational savings</div>
      </div>
    </div>
  </div>
  <div class="impact"><span class="impact-label">Impact: </span>For offshore wind, growing from .1 percent to 4 percent could avoid 14.1 gigatons of emissions. At a combined cost of $1.8 trillion, wind turbines can deliver net savings of $8.2 trillion over three decades of operation. These are conservative estimates, however. Costs are falling annually and new technological improvements are already being installed, increasing capacity to generate more electricity at the same or lower cost. <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <div>Summary:</div>
    <div class="stat"><span class="stat-value">14.1</span><span class="stat-unit"> gigatons</span><br>
      reduced CO2</div>
    <div class="stat"><span class="stat-value">$545.3</span><span class="stat-unit"> Billion</span><br>
      net implementation cost</div>
    <div class="stat"><span class="stat-value">$762.5</span><span class="stat-unit"> Billion</span><br>
      net operational savings</div>
  </div>
<div class="charts">
    <canvas id="myChart" width="400" height="200"></canvas>
  </div>
  <?php
	$timesql = "SELECT Time FROM cleanenergy WHERE Area = 'World';";
  $result = mysqli_query( $conn, $timesql );
  while ( $row = mysqli_fetch_assoc( $result ) ) {
    $Time[] = $row[ 'Time' ];
  }
  $sql = "SELECT Percentage FROM cleanenergy WHERE Area = 'World';";
  $result = mysqli_query( $conn, $sql );
  while ( $row = mysqli_fetch_assoc( $result ) ) {
    $World[] = $row[ 'Percentage' ];
  }
  $Africasql = "SELECT Percentage FROM cleanenergy WHERE Area='Africa';";
  $result = mysqli_query( $conn, $Africasql );
  while ( $row = mysqli_fetch_assoc( $result ) ) {
    $Africa[] = $row[ 'Percentage' ];
  }
  $NAMsql = "SELECT Percentage FROM cleanenergy WHERE Area='Americas';";
  $result = mysqli_query( $conn, $NAMsql );
  while ( $row = mysqli_fetch_assoc( $result ) ) {
    $NorthAmerica[] = $row[ 'Percentage' ];
  }

  ?>
  <script>
	var Time = <?php echo json_encode($Time);?>;
	Time=Time.map(Number);
	var World = <?php echo json_encode($World);?>;
	for(var i=0;i<World.length;i++){
		World[i]=parseFloat(World[i])
	}
	var Africa = <?php echo json_encode($Africa);?>;
	for(var i=0;i<Africa.length;i++){
		Africa[i]=parseFloat(Africa[i])
	}
	var NorthAmerica = <?php echo json_encode($NorthAmerica);?>;
	for(var i=0;i<NorthAmerica.length;i++){
		NorthAmerica[i]=parseFloat(NorthAmerica[i])
	}
	var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: Time,
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

</script>
  
</div>
<footer>
  <div class="small">
    <p>Copyright &copy; jeffersonucc.github.io</p>
  </div>
</footer>
<script src="./js/script.js" type="text/javascript"></script>
</body>
</html>
