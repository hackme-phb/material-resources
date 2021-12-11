<?php

$host = "localhost";
$user = "xss";
$pass = "xss";
$db   = "xss";

$conn = mysqli_connect($host, $user, $pass);
mysqli_select_db($conn, $db);
