<?php
    
     
	$unam1=$_POST['a'];
	$pass2=$_POST['b'];

	if($unam1=="admin"&& $pass2=="admin")
	{ 
	    
		
	   echo "<script type='text/javascript'>alert('Detailed login successfull');</script>";
	   echo "<script type='text/javascript'>window.location='main.php';</script>";
	}
	else
	{
		echo "<script type='text/javascript'>alert('wrong username or password');</script>";
	   echo "<script type='text/javascript'>window.location='index.html';</script>";
		

}
?>

