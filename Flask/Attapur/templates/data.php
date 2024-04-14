<?php
$host = "localhost";
$username = "root"; 
$password = ""; 
$database = "sign_up";

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $faname = $_POST['faname'];
    $email = $_POST['email'];
    $age = $_POST['age'];
    $info = $_POST['info'];

    $sql = "INSERT INTO signup (fname, lname, faname, email, age, info) VALUES (?, ?, ?, ?, ?, ?)";

    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ssssis", $fname, $lname, $faname, $email, $age, $info);

    if ($stmt->execute()) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $stmt->close();
    $conn->close();
}
?>
