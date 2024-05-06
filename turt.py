
for i in range(10):
    print("Iteration: ", i)



# Importing a library (a library is a compilation of prewritten code to server some end, in our case drawing to the screen with lines)
import turtle

turtle.right(72)
turtle.forward(500)

for _ in range(4):
    turtle.right(144)
    turtle.forward(500)

# Required(?) to hold the result on the screen after we are finished drawing
turtle.done()