from turtle import *
screensize(4000, 4000)
tracer(0)
m = 25
for i in range(5):
    rt(45)
    fd(10 * m)
    rt(45)
for i in range(6):
    fd(20 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3)
update()
done()