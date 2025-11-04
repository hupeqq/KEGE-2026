from turtle import *
screensize(2000, 2000)
tracer(0)
m = 10
for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-30, 50):
    for y in range(-50, 30):
        goto(x * m, y * m)
        dot(3)
update()
done()