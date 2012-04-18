<?
/*
Copyright (C) 2005 Rémy HUBSCHER

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. 
*/

//Repertoire transmis par $_GET
//Definition des variables
if (!isset($_GET['dir'])) $dir='.';
else $dir=$_GET['dir'];
$gDirectory = $dir."/miniature/"; // Repertoire des miniatures
$aDirectory = $dir."/agrandie/";  // Repertoire des images non réduite
$gExtension = "jpg gif png jpeg JPG"; // séparez les extensions par un espace
$taille_text ="2";
?>
<html>
<head>
<title>.: Galleries d'images :.</title>
<!-- DEBUT DU SCRIPT -->
<SCRIPT LANGUAGE="JavaScript">
/*
SCRIPT EDITE SUR L'EDITEUR JAVASCRIPT
http://www.editeurjavascript.com
Revu par Rémy Hubscher pour le rajout des commentaires
*/
function afficheMaxi(chemin)
  {
  i1 = new Image;
  i1.src = chemin;
  html = '<HTML><HEAD><TITLE>Image</TITLE></HEAD><BODY bgcolor=#A21E32 LEFTMARGIN=0 MARGINWIDTH=0 TOPMARGIN=0 MARGINHEIGHT=0><div align="center"><center><table border="0" cellpadding="0" cellspacing="0" width="750"><tr><td><img src="/photos/000.gif" width="750" height="39"></td></tr><tr><td background="/photos/003.gif"><table border="0" width="100%"><tr><td width="4%" height="21"></td><td width="92%" height="21" align="center"><a href="javascript:window.close();"><IMG src="/photos/<? echo $aDirectory; ?>'+chemin+'" BORDER=0 NAME=imageTest /></a></td><td width="4%" height="21"></td></tr></table></td></tr><tr><td><img src="/photos/001.gif" width="750" height="39"></td></tr></table></CENTER></div></BODY></HTML>';
  popupImage = window.open('','_blank','toolbar=0,location=0,directories=0,menuBar=0,scrollbars=0,resizable=1,width=800,height=700,top=(screen.height-hauteur)/2,left=(screen.width-largeur)/2');
  popupImage.document.open();
  popupImage.document.write(html);
  popupImage.document.close()
  };
</SCRIPT>
<!-- FIN DU SCRIPT -->
</head>
<body bgcolor="#A21E32" link="#AA112C" vlink="#AA112C">
<div align="center"><center>

<table border="0" cellpadding="0" cellspacing="0" width="750">
  <tr>
    <td><img src="/photos/000.gif" width="750" height="39"></td>
  </tr>
  <tr>
    <td background="/photos/003.gif">
         <table border="0" width="100%">
         <tr>
          <td width="4%" height="21"></td>
          <td width="92%" height="21">
<?
if (!is_dir($dir)){
 echo ('Le dossier \''.$dir.'\' n\'est pas valide');
}
elseif (!@is_dir($gDirectory) or !@is_dir($aDirectory)) {
function browse_dir($path) {
    $O = dir($path);
    if(!is_object($O)) return false;

    echo 'Ce dossier contient les dossiers de photos suivantes : <table border="0" width="100%">';
    while($file = $O -> read()) {
        if($file != '.' && $file != '..') {
$true = preg_match_all("!^[0-9]{8}$!isU", $file, $rec_id);
                if(is_dir($path.'/'.$file) && $true) {
		  $DIR[] = $file;
		  }
}
}

		  sort ($DIR);
		  $DIR = array_reverse($DIR);
foreach ($DIR as $file) {
		  $annee = substr($file, 0, 4);
		  $mois = substr($file, 4, 2);
		  $jour = substr($file, 6, 2);
		  if ($path == '.'){ echo '        <tr>
          <td width="32%" height="21"><p align="center"><a href="'.$file.'"><img src="/photos/aleatoire.php?dir='.$file.'" border="0" title="Activite du '.$jour.'/'.$mois.'/'.$annee.'" alt="Activite du '.$jour.'/'.$mois.'/'.$annee.'"></a></p></td>
          <td width="64%">';@include $file.'/text.txt';
		  echo '</td></tr>';}
		  else { echo '<tr>
          <td width="32%" height="21"><p align="center"><a href="index.php?dir='.$path.'/'.$file.'"><img src="/photos/aleatoire.php?dir='.$path.'/'.$file.'" border="0" title="Activite du '.$jour.'/'.$mois.'/'.$annee.'" alt="Activite du '.$jour.'/'.$mois.'/'.$annee.'"></a></p></td>
          <td width="64%">';@include $file.'/text.txt';
		 }
		}

    echo '</table>';
    $O -> close();
  
    return true;
   }
browse_dir($dir);
}else{
?>
<?php
/*Nom :		Louloux_images
Description :	Affiche les images d'un dossier selon les extentions données, s'il n'y a pas d'image, affiche les dossiers d'image tester par une RegEx de la forme 20041129
Auteur :	Natim <www.natim.clan.st> pour l'affichage et le changement de page
URL :		http://www.natim.clan.st/
*/
?>
<?php

//Insertion d'un TITRE
echo '<h'.$taille_text.' align=center>';
@include $dir.'/text.txt';
echo '</h'.$taille_text.'>';
//Definition de variable
$debut = $_GET['debut'];
if (!isset($_GET['debut'])) $debut = 0;
$max=12;//multiple de 3

function browse($pDirectory, $pExtension)
{
	if($handle = opendir($pDirectory))
	{
 		while(false !== ($file = readdir($handle)))
		{
			$getExt = explode(".", $file);
			$countExt = count($getExt);
			$fExt = $countExt - 1;
			$myExt = $getExt[$fExt];
			
			if (($myExt == $pExtension) && ($file != ".") && ($file != "..") && (isset($file)) ){
				$files[] = $file;
			}
		}
	}
return $files;	
closedir($handle);
}

$ExpExt = explode(" ", $gExtension);
sort ($ExpExt);

foreach ($ExpExt as $findExt)
	{
		$getFile = @browse($gDirectory, $findExt);
for ($i=0; $i < count($getFile); $i++){
  if(isset($getFile[$i])){
		$Files[] = $getFile[$i];
  }
		}
	}
		$countFile = count($Files);
echo "<TABLE width=100% BORDER=0><tr>";
for($i = $debut ; $i < $countFile; $i++) {
		
			     echo "<TD align=center><a href=\"javascript:afficheMaxi('$Files[$i]')\"><img src='/photos/".$gDirectory.$Files[$i]."' border='0'></TD>";
			      if (($i+1) % 3 == 0){
			      echo "</tr><tr>";
			      }	
$bzw=0;
if (($i+1)==$countFile && $debut!=0 ){
$nb = ($i+1) % $max;
echo '</tr></TABLE><p align=center><a href="/photos/'.$dir.'/'.($debut-$max != 0 ? $debut - $max : '' ).'/">< Pr&eacute;c&eacute;dente</a><br /><a href="/">Retour</a></p>';
}

if (($i+1)==$countFile && $debut==0 ){
$nb = ($i+1) % $max;
echo '</tr></TABLE><p align=center><a href="/">Retour</a></p>';
}
if ((($i+1) % $max == 0) && (($i+1)!=$countFile)) {
if ($i-$max >= 0){
 echo '</tr></TABLE><p align=center><a href="/photos/'.$dir.'/'.($i-(2*$max-1)).'/">< Pr&eacute;c&eacute;dente</a>&nbsp;';
 $bzw=1;
}
if($bzw!=1) $p='</tr></TABLE><p align=center>';
echo ($p.'<a href="/photos/'.$dir.'/'.($i+1).'/">Suivante ></a><br /><a href="/">Retour</a></p>');
break;
}
}
}	
?>
</td>
          <td width="4%" height="21"></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td><img src="/photos/001.gif" width="750" height="39"></td>
  </tr>
</table>
</center></div>
</body>
</html>
