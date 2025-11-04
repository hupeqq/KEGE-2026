from turtle import *
screensize(2000, 2000)
tracer(0)
m = 20
for i in range(4):
    fd(19 * m)
    rt(90)
    fd(30 * m)
    rt(90)
up()
fd (2 * m)
rt(90)
fd(8 * m)
lt(90)
down()
for i in range(4):
    fd(93 * m)
    rt(90)
    fd(97 * m)
    rt(90)
up()
for x in range(-10, 20):
    for y in range(-40, 5):
        goto(x * m, y * m)
        dot(3)
update()
done()
# ответ 374 (17 * 22)