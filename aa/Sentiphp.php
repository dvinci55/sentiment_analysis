<?php

$file=fopen("homepath.txt","r") or die(" unalble to open");
$home=fread($file,filesize("homepath.txt"));
$home=trim($home);
$myfile = fopen("pos.txt", "w") or die("Unable to open file!");
$txt = " ";
fwrite($myfile, $txt);
$myfilee = fopen("neg.txt", "w") or die("Unable to open file!");
$txt = " ";
fwrite($myfilee, $txt);
$myy = fopen("count.txt", "w") or die("Unable to open file!");
$txt = " ";
fwrite($myy, $txt);

fclose($file);
fclose($myfile);
fclose($myfilee);
fclose($myy);
$tmp=exec("python ".$home."/Senti.py");

echo "<script type='text/javascript'>window.location='Chart.php';</script>";
?>
