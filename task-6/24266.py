from turtle import *
m = 5
screensize(2000,2000)
tracer(False)
for i in range(4):
    fd(30 * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()
fd(27 * m)
rt(90)
fd(24 * m)
lt(90)
down()
for i in range(4):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 20):
        goto(x * m, y * m)
        dot(3, 'green')
update()
done()
# при x = 30:
# p = 19 + 19 + 2 + 2