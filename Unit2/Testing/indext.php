
<html>
   <body>
      <form action = "<?php $_PHP_SELF ?>" method = "GET">
		  Name: <select name = "name">
		  <option value="1" textcontent="1" name="1">1</option>
		  <option value="2" textcontent="2" name="1">2</option>
		  <option value="3" textcontent="3" name="1">3</option>
		  <option value="4" textcontent="4" name="1">4</option>
		  </select>
		  <button id="button">Click!</button>
      </form>
	   <script>
	   
	   console.log(text)
	   </script>
	  <script>
		  var text='<?php 
		if(isset($_GET['name'])){
		echo $_GET['name'];}?>'
		  function print(){
			console.log("clicked!")
		  }
		  document.getElementById("button").addEventListener("click",print(),false);
		  
	  </script>
	   
	   
	      </body>
</html>