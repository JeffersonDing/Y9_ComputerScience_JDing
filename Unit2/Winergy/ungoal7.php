<?php
include_once( "./includes/Connection.php" );
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Winergy®</title>
<link href="css/style.css" rel="stylesheet">
<link rel="stylesheet" href="https://use.typekit.net/bjd5jat.css">
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
    <h2>United Nations</h2>
    <h1>Sustainable Development Goal #7</h1>
    <div class="description">
      <p>Energy is central to nearly every major challenge and opportunity the world faces today. Be it for jobs, security, climate change, food production or increasing incomes, access to energy for all is essential. Working towards this goal is especially important as it interlinks with other Sustainable Development Goals. Focusing on universal access to energy, increased energy efficiency and the increased use of renewable energy through new economic and job opportunities is crucial to creating more sustainable and inclusive communities and resilience to environmental issues like climate change.</p>
      <p>At the current time, there are approximately 3 billion people who lack access to clean-cooking solutions and are exposed to dangerous levels of air pollution. Additionally, slightly less than 1 billion people are functioning without electricity and 50% of them are found in Sub-Saharan Africa alone. Fortunately, progress has been made in the past decade regarding the use of renewable electricity from water, solar and wind power and the ratio of energy used per unit of GDP is also declining.</p>
      <p>However, the challenge is far from being solved and there needs to be more access to clean fuel and technology and more progress needs to be made regarding integrating renewable energy into end-use applications in buildings, transport and industry. Public and private investments in energy also need to be increased and there needs to be more focus on regulatory frameworks and innovative business models to transform the world’s energy systems.</p>
      
    </div>
  </div>
  <div class="sidebar-right">
    <div class="ranking-results">
      <div class="rank-number"> <sup>#</sup>7 </div>
      <div class="rank-desc"> Facts and Figures </div>
      <div class="rank-stats">
        <div class="stat"><span class="stat-value">13</span><span class="stat-unit"> Percent</span><br>
         Global population still lacks access to modern electricity.</div>
        <div class="stat"><span class="stat-value">3</span><span class="stat-unit"> Billion</span><br>
          People rely on wood, coal, charcoal or animal waste for cooking and heating</div>
        <div class="stat"><span class="stat-value">17.5</span><span class="stat-unit"> Percent</span><br>
          Renewable energy in final energy consumption</div>
      </div>
    </div>
  </div>
	<div clas="summary">
    <div class="impact-label">Targets:</div>
    <div class="stat">
		7.1 By 2030, ensure universal access to affordable, reliable and modern energy services</div>
<div class="stat">
7.2 By 2030, increase substantially the share of renewable energy in the global energy mix</div>
<div class="stat">
7.3 By 2030, double the global rate of improvement in energy efficiency</div>
<div class="stat">
7.A By 2030, enhance international cooperation to facilitate access to clean energy research and technology, including renewable energy, energy efficiency and advanced and cleaner fossil-fuel technology, and promote investment in energy infrastructure and clean energy technology</div>
<div class="stat">
7.B By 2030, expand infrastructure and upgrade technology for supplying modern and sustainable energy services for all in developing countries, in particular least developed countries, small island developing States, and land-locked developing countries, in accordance with their respective programmes of support
</div>
	</div>
  <div class="charts">
    <canvas id="myChart" width="400" height="200"></canvas>
    <div class="addRegion">
	
</div>
	
 

<?php
  $timesql = "SELECT Time FROM cleanenergy WHERE Area = 'World';";
  $result = mysqli_query( $conn, $timesql );
  while ( $row = mysqli_fetch_assoc( $result ) ) {
    $Time[] = $row[ 'Time' ];
  }
	$areasql = "SELECT Area FROM cleanenergy;";
  $result = mysqli_query( $conn, $areasql );
  while ( $row = mysqli_fetch_assoc( $result ) ) {
    $Area[] = $row['Area'];
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
	  

</script>
<script>
var bgcolorset=['rgba(0,139,248,0.4)','rgba(4,231,98,0.4)','rgba(245,183,0,0.4)','rgba(145,78,97,0.5)','rgba(77,19,245,0.3)','rgba(17,138,178,0.4)','rgba(6,214,160,0.4)','rgba(252,68,15,0.4)',]
var dataset = [
		{ 
		label:"North America",
        data: NorthAmerica,
		backgroundColor:'rgba(0,139,248,0.4)'
      },
      { 
		label:"World",
        data: World,
		backgroundColor:'rgba(4,231,98,0.4)'
      },
		{ 
		label:"Africa",
        data: Africa,
		backgroundColor:'rgba(245,183,0,0.4)'
      }
		
    ]
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: Time,
    datasets: dataset
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
        <form action=""<?php $_PHP_SELF ?>"" method="GET">
        Add Compare Source:<select id="regions" name="area"></select>
		<button type="submit" id="addarea" >Add!</button>
        </form>
    </div>
<script>
document.getElementById("addarea").addEventListener("click",addRegion(),false);
function addData(chart, inlabel, indata) {
   dataset.push({label:inlabel,data:indata,backgroundColor:bgcolorset[Math.floor(Math.random() * bgcolorset.length)]});
    chart.update();
}
function addRegion(){
	<?php
	$addsql = "SELECT Percentage FROM cleanenergy WHERE Area ='{$_GET['area']}';";
  $result = mysqli_query( $conn, $addsql );
  while ( $row = mysqli_fetch_assoc( $result ) ){
    $addData[] = $row[ 'Percentage' ];
  }
	  ?>
  }
	var addOn = <?php echo json_encode($addData);?>;
	for(var i=0;i<addOn.length;i++){
		addOn[i]=parseFloat(addOn[i])
	}
var lable='<?php 
	if(isset($_GET['area'])){
	echo $_GET['area'];}?>'
addData(myChart,lable,addOn);
</script>
  </div>

<script>
var options = <?php echo json_encode($Area);?>;
let unique = [...new Set(options)];
var select = document.getElementById("regions"); 
for(var i = 0; i < unique.length; i++) {
    var opt = unique[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
}		  
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
