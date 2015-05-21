<?php

function connect_to_db(){

	error_log('conneect to registration', 4);

	// Define connection variables
	$DBServer = "localhost";  // server name or IP address
	$DBUser = "root";
	$DBPass = "maverick";
	$DBName = "registration";

	// Create connection
	$conn = mysqli_connect($DBServer, $DBUser, $DBPass, $DBName);

	// Check connection
	if ($conn->connect_error) {
	    echo "Database connection failed: " . $conn->connect_error, E_USER_ERROR;
	}
	else {echo "Database connection was success!"; }

	return $conn;
}



?> 

