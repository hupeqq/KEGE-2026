from turtle import *
m = 5
screensize(2000,2000)
tracer(False)
for i in range(5):
    fd(37 * m)
    rt(90)
    fd(44 * m)
    rt(90)
up()
bk(18 * m )
rt(90)
fd(29 * m)
lt(90)
down()
for i in range(5):
    fd(31 * m)
    rt(90)
    fd(35 * m)
    rt(90)
up()
for x in range(-10, 50):
    for y in range(-50, 20):
        goto(x * m, y * m)
        dot(3, 'green')
update()
done()
# 16 * 14 = 224