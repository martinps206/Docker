<?php
$con = mysqli_connect("basedatos:3307","root","martin","usuarios");

if(!$con){
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?>