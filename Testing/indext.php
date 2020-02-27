<?php
include_once("./Connection.php")
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Testing Page</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>
<?php
	$sql = "SELECT Percentage FROM cleanenergy WHERE Area = 'World';";
	$result = mysqli_query($conn,$sql);
	while($row = mysqli_fetch_assoc($result)){
		$World[] = $row['Percentage'];	
	}
	$Africasql = "SELECT Percentage FROM cleanenergy WHERE Area='Africa';";
	$result = mysqli_query($conn,$Africasql);
	while($row = mysqli_fetch_assoc($result)){
		$Africa[] = $row['Percentage'];	
	}
    $NAMsql = "SELECT Percentage FROM cleanenergy WHERE Area='Americas';";
	$result = mysqli_query($conn,$NAMsql);
	while($row = mysqli_fetch_assoc($result)){
		$NorthAmerica[] = $row['Percentage'];	
	}
		
?>
<script>
	var World = <?php echo json_encode($World);?>;
	var Africa = <?php echo json_encode($Africa);?>;
	var NorthAmerica = <?php echo json_encode($NorthAmerica);?>;
</script>
</body>
<script type="text/javascript" src="script.js"></script>

</html>
