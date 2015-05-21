<?php
//phpinfo();
include ('connect.php');

$username = $_POST["name"] ;
$email = $_POST["email"];
$password = $_POST["password"] ;

$dbConnection = connect_to_db();
//THE FIRST COLUMN IS ID (AUTO-INCREMENTED)
$query = "INSERT INTO user (username, email, password) VALUES ('$username', '$email', '$password')";

if (mysqli_query($dbConnection, $query)) {
	echo "Successfully inserted " . mysqli_affected_rows($dbConnection) . " row"; }
else {
echo "Error occurred: " . mysqli_error($dbConnection); }

?> 