<?php

$file=fopen("homepath.txt","r") or die(" unalble to open");
$home=fread($file,filesize("homepath.txt"));
$home=trim($home);

fclose($file);

$tmp=exec("python ".$home."/Charts.py");

echo "<script type='text/javascript'>window.location='DispChart.php';</script>";
?>
