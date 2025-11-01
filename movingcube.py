import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("up and down right and left square")
pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)

x, y = 0, -200
size = 80
speed = 8
keys = {"Up": False, "Down": False, "Left": False, "Right": False}

def draw_square(cx, cy):
  pen.clear()
  pen.up()
  pen.goto(cx - size / 2, cy - size /2)
  pen.down()
  pen.color("black", "darkgreen")
  pen.begin_fill()
  for _ in range(4):
    pen.forward(size)
    pen.left(90)
  pen.end_fill()

def press(key): keys[key] = True
def release(key): keys[key] = False
def update():
  global x, y
  if keys["Up"]: y += speed
  if keys["Down"]: y -= speed
  if keys["Right"]: x += speed
  if keys["Left"]: x -= speed
  draw_square(x, y)
  screen.update()
  screen.ontimer(update, 16)

for k in keys:
  screen.onkeypress(lambda k=k: press(k), k)
  screen.onkeyrelease(lambda k=k: release(k), k)

screen.listen()
update()
screen.mainloop()
  