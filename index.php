<!DOCTYPE html>
<html>
<head>
<title>PIDS</title>
<style>
	.row {
		display: flex;
	}
	.column {
		flex: 33%;
	}
</style>
</head>
<body bgcolor="#DEB887">
<h1>Pi Intrusion Detection System</h1> 
<div class="row">
  <div class="column" style="background-color:#FAEBD7;">
    <h2><a href="/intrusions">Intrusions</a></h2>
    </form> 
        <form method="post" >
        <button name="delete" type="submit">Delete Intrusion Log</button>
    </form>
    
  </div>
  <div class="column" style="background-color:#FAEBD7;">
    <h2>Settings</h2>
    	<form method="post">
    		Enter Your Phone Number Here:<br>
    		<input type="text" name="phonedata"><br>
    		Enter Your Email Here:<br>
    		<input type="text" name="emaildata"><br>
    	 	<input type="submit" name="submit" value="Save">
  </div>
  <div class="column" style="background-color:#DEB887;">
    <h2>Video Feed</h2>
    <video width="720" controls>
      <source src="video.mp4" type="video/mp4">
    </video>
    
  </div>
</div>
</body>
</html>
<?php
              
	if(isset($_POST['phonedata']))
	{
		$data=$_POST['phonedata'];
		$fp = fopen('phone.txt', 'w');
		fwrite($fp, $data);
		fclose($fp);
	}

	if(isset($_POST['emaildata']))
	{
		$data=$_POST['emaildata'];
		$fp = fopen('email.txt', 'w');
		fwrite($fp, $data);
		fclose($fp);
	}

	if (isset($_POST['delete']))
	{
		array_map('unlink', glob("intrusions/*.jpg"));
	}

?>
