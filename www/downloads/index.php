<?php
$nb = intval(file_get_contents("count.txt"));
$nb++;
file_put_contents("count.txt", $nb);
header('Location: http://download.trunat.fr/PyTalk/');
?>