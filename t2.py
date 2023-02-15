# nested loops 
from turtle import*
speed('slow')
pencolor('blue')

for i in range(6):
    pensize(6)
    fd(100)
    for i in range(6):
        pensize(3)
        fd(50)
        for i in range(6):
            pensize(1)
            fd(25)
            rt(60)
        rt(60)
    rt(60)    
hideturtle()
mainloop()

