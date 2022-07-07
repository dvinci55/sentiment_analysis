<?php
$pid=$_POST['productid'];
$file=fopen("homepath.txt","r") or die(" unalble to open");
$home=fread($file,filesize("homepath.txt"));
$home=trim($home);

fclose($file);
$tmp=exec("python ".$home."/newamazon.py"." ".$pid);

echo "<script type='text/javascript'>window.location='MainPage.php';</script>";
?>
