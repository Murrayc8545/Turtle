import turtle            

jay = turtle.Screen()
cay = turtle.Turtle()


cay.pensize(3)            # increase pensize (takes integer)
cay.pencolor("purple")     # set pencolor (takes string)
cay.shape("turtle")


for x in range (4):

    cay.shape("turtle")
    cay.forward(50)          
    cay.left(90)             
    
for y in range (3):

    cay.forward(100)          
    cay.left(120)            
    cay.forward(100)
 
# end commands
win.mainloop()             # Wait for user to close window


