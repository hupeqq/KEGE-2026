from turtle import *
m = 40
screensize(2000,2000)
tracer(False)
rt(270)
for i in range(2):
    fd(8 * m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)
rt(240)
for i in range(2):
    fd(14 * m)
    rt(120)
up()
for x in range(-10, 50):
    for y in range(-50, 20):
        goto(x * m, y * m)
        dot(3, 'green')
update()
done()
# 12 * 14 / 2 = 84