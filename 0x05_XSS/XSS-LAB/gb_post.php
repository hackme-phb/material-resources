<?php

session_start();

include 'koneksi.php';

$nama = mysqli_real_escape_string($conn, $_POST['nama']);
$pesan = mysqli_real_escape_string($conn, $_POST['pesan']);

$insert = mysqli_query($conn, "INSERT INTO guestbook (id, tanggal, nama, pesan) VALUES(NULL, NOW(), '{$nama}', '{$pesan}')");

if ($insert) {
	echo "Pesan Anda sudah disimpan.";
  	header("location:gb.php");
}


