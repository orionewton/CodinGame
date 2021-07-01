Module Player
' CodinGame planet is being attacked by slimy insectoid aliens.
' <---
' Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.

    Sub Main ()
        
        ' game loop
        While True
            Dim enemy1 as String
            enemy1 = Console.ReadLine() ' name of enemy 1

            Dim dist1 as Integer
            dist1 = Console.ReadLine() ' distance to enemy 1

            Dim enemy2 as String
            enemy2 = Console.ReadLine() ' name of enemy 2

            Dim dist2 as Integer
            dist2 = Console.ReadLine() ' distance to enemy 2

            if(dist1 < dist2)
                Console.WriteLine(enemy1)
            else
                Console.WriteLine(enemy2)
            end if
        End While
    End Sub
End Module
