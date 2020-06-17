import turtle
h = turtle.Turtle()
h.up()
h.backward(200)
def house():
  number = int(input("# of Houses: "))
  i = 0
  while i < number:
    length = int(input("Length: "))
    height = int(input("Height: "))
    dh = int(input("Door Height: "))
    dw = int(input("Door Width: "))
    ch1 = int(input("Chimney Height: "))
    color = input("Color: ")
    distance = (length / 2) - (dw /2)  
    if distance > 20:
      cw = 20
    else:
      cw = distance
    ch2 = ch1 - (cw * (3 ^ 1/2))
    h.down()
    h.color(color)
    h.forward(length)
    h.left(90)
    h.forward(height)
    h.left(30)
    h.forward(length)
    h.left(120)
    h.forward(length)
    h.left(120)
    h.forward(length)
    h.left(180)
    h.forward(length)
    h.left(90)
    h.forward(height)
    h.left(90)
    h.forward(distance)
    h.left(90)
    h.forward(dh)
    h.right(90)
    h.forward(dw)
    h.right(90)
    h.forward(dh)
    h.right(90)
    h.forward(dw)
    h.forward(distance)
    h.right(90)
    h.forward(height)
    h.forward(ch1)
    h.right(90)
    h.forward(cw)
    h.left(90)
    h.forward(ch2)
    h.left(180)
    h.forward(ch2)
    h.right(90)
    h.forward(cw)
    h.left(90)
    h.forward(ch1)
    h.forward(height)
    h.left(90)
    h.forward(distance)
    h.forward(dw)
    h.up()
    a = distance + 20
    h.forward(a)
    i += 1
house()