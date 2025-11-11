from turtle import *
screensize(2000, 2000)
tracer(0)
m = 15
rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)
up()
for x in range(-20, 50):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, 'green')
update()
done()
# 64 + 49 = 113