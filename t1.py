from turtle import*
speed('slowest')
fillcolor('red')
side= 7

#fd(100)
#lt(90)
#fd(100)
#lt(90)
#fd(100)
#lt(90)
#fd(100)
#lt(90)

#mainloop()



# using for loops: 
begin_fill()
for i in range(side):
    fd(100)
    lt(360/side)
end_fill()    
hideturtle()
mainloop()

