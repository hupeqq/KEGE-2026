from turtle import *
screensize(2000,2000)
tracer(False)
m = 10
for i in  range(3):
    fd(7 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()

fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
down()
for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-100, 25):
    for y in range(-20, 100):
        goto(x * m, y * m)
        dot(3, 'green')
update()
done()
# ответ 6228 (84*78 + 13*8 - 7 * 4)