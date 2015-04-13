#!/usr/bin/php
<?php
	if ($argc != 2)
	{
		echo "Nop...\n";
		return (0);
	}
	$i = 0;
	while ($i < $argv[1])
	{

		mkdir(($i > 9) ? "ex".$i : "ex0".$i, 0755);
		$i++;
	}
?>
