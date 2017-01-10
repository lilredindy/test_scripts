<?php
$_fp = fopen("hacker.txt", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */

fscanf($_fp, "%d", $n);
print $n;

$phonebook = array();
for ($i = 0; $i < $n; ++$i){
    list($key, $value)= explode(" ", trim(fgets($_fp)));
    //fscanf($_fp, "%s %s", $key, $value);
    $phonebook[$key] = $value;
}

//print_r($phonebook);


$count = 0;

while(true){
  //fscanf($_fp, "%s", $line);
  $line = trim(fgets($_fp));
  if (!$line)
	break;

  ++$count; 
  $result = "Not found\n";

  foreach ($phonebook as $key => $value){
      if ($line == $key){
          $result = "$key=$value\n";
          break;
      }
  }

  print $result;
} 
print $count;

fclose($_fp);
?>
