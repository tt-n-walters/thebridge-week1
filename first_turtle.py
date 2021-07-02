import turtle

turtle.Turtle()

turtle.pencolor("red")
turtle.fillcolor("orange")
turtle.pensize(4)

size = int(input("Number of sides: "))
#turtle.begin_fill()
           
#counter = 0
#while counter < size:
#    turtle.forward(100)
#    turtle.right(360/size)
#    counter = counter + 1

for counter in range(size):
    turtle.forward(100)
    turtle.right(360/size)

for counter in range(size):
    turtle.circle(counter * 10)
    
    
#turtle.end_fill()
