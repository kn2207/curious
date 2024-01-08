how_many_snakes = 3
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes, sep= "  ")

for i in range(how_many_snakes):
    print(snake_string, sep="")