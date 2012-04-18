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

  header("Content-type: image/jpg");

  $dirname = $_GET['dir'].'/miniature/';

  $extensoes = array("jpg","JPG","jpeg", "png");
  
  $files = array();

  $dir = @opendir($dirname);

   while(false !== ($file = @readdir($dir)))
    {
       //GET THE FILES ACCORDING TO THE EXTENSIONS ON THE ARRAY
       for ($i = 0; $i < count($extensoes); $i++)
       {
           if (eregi("\.". $extensoes[$i] ."$", $file))
           {
               $files[] = $file;
           }
       }
    }

   $id = count($files)-1;
   $j=mt_rand(0,$id);

   //CLOSE THE HANDLE
   @closedir($dir);

readfile($dirname.$files[$j]);


?> 