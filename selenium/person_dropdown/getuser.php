<?php

sleep(1);

$q = intval($_POST['q']);
echo $_POST['q'];
echo $q;


$conn = pg_connect("host=localhost port=5432 dbname=test user=postgres password=maverick");
if (!$conn) {
  echo "An error occurred connecting.\n";
  exit;
}


$result = pg_query($conn, "SELECT firstname, lastname, age, hometown, job FROM foo where id=$q");
if (!$result) {
  echo "An error occurred querying.\n";
  exit;
}

echo "<table border='1'>
<tr>
<th>Firstname</th>
<th>Lastname</th>
<th>Age</th>
<th>Hometown</th>
<th>Job</th>
</tr>";


while ($row = pg_fetch_row($result)) {	
  echo "<tr>";
  echo "<td>" . $row[0] . "</td>";
  echo "<td>" . $row[1] . "</td>";
  echo "<td>" . $row[2] . "</td>";
  echo "<td>" . $row[3] . "</td>";
  echo "<td>" . $row[4] . "</td>";
  echo "</tr>";
}

echo "</table>";

?> 