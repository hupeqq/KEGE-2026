from turtle import *
screensize(2000, 2000)
tracer(0)
m = 40
rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)
up()
for x in range(-30, 50):
    for y in range(-50, 30):
        goto(x * m, y * m)
        dot(3)
update()
done()