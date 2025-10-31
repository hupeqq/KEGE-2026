from turtle import *
m = 20
screensize(2000,2000)
tracer(False)
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-10, 25):
    for y in range(-25, 10):
        goto(x * m, y * m)
        dot(3, 'green')
update()
done()