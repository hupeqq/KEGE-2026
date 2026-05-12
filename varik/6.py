from turtle import *
screensize(2000, 2000)
tracer(0)
m = 15
rt(45)
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
rt(315)
fd(10 * m)
rt(90)
fd(20 * m)
rt(90)
for i in range(2):
    fd(10 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, 'green')
update()
done()
####### 261