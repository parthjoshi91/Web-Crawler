<?php

  if(!empty($_GET))
  { $dbhost = 'ec2-52-10-122-11.us-west-2.compute.amazonaws.com';
	$dbuser = 'root';
	$dbpass = '';
	$conn = mysql_connect($dbhost, $dbuser, $dbpass);
	if(! $conn )
	{
	  die('Could not connect: ' . mysql_error());
	}
	$sql = "SELECT * FROM t_data where Title like '%".$_GET['keywords']."%' OR Description like '%".$_GET['keywords']."%'";
	mysql_select_db('test');
	$retval = mysql_query( $sql, $conn );
	if(! $retval )
	{ 
	  die('Could not get data: ' . mysql_error());
	}
	$x=0;
	while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
	{	$x=$x+1;
		$test_data["item$x"]['url']=$row['Url'];
	    $test_data["item$x"]['titl']=$row['Title'];
	    if(isset($row['Description']))
	    {$test_data["item$x"]['descript']=$row['Description'];}
	    if(isset($row['Image']))
		{$test_data["item$x"]['imag']=$row['Image'];
}		
	} 
	$test_data["count"]="$x";
	$json=json_encode($test_data);
  	echo $json;

	mysql_close($conn);
  }
?>