<?php
/**
 * CodinGame planet is being attacked by slimy insectoid aliens.
 * <---
 * Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.
 **/


// game loop
while (TRUE)
{
    // $enemy1: name of enemy 1
    fscanf(STDIN, "%s", $enemy1);
    // $dist1: distance to enemy 1
    fscanf(STDIN, "%d", $dist1);
    // $enemy2: name of enemy 2
    fscanf(STDIN, "%s", $enemy2);
    // $dist2: distance to enemy 2
    fscanf(STDIN, "%d", $dist2);

    if($dist1 < $dist2){
        echo("$enemy1\n");
    }
    else{
        echo("$enemy2\n");
    }

    // You have to output a correct ship name to shoot ("Buzz", enemy1, enemy2, ...)
}
?>
