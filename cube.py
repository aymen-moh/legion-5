import turtle, math, time
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.hideturtle()
t.pensize(3)
t.speed(0)
screen.tracer(0, 0)

points = [
  [-50,-50,-50],[50,-50,-50],[50,50,-50],[-50,50,-50],
  [-50,-50,50],[50,-50,50],[50,50,50],[-50,50,50]
]
edges = [
  (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)
]
def rot_y(x, y, z, a):
    r = math.radians(a); c = math.cos(r); s = math.sin(r)
    return [x * c + z * s, y, -x * s + z * c]

def rot_x(x, y, z, a):
    r = math.radians(a); c = math.cos(r); s = math.sin(r)
    return [x, y * c - z * s, y * s + z * c]


def draw(pts):
    t.clear()
    t.color("black")
    for e in edges:
        p1, p2 = pts[e[0]], pts[e[1]]
        t.penup()
        t.goto(p1[0], p1[1])
        t.pendown()
        t.goto(p2[0], p2[1])
    screen.update()
    
angle=0
frame_time=1/60

while True:
  start=time.time()
  projected=[]
  for x,y,z in points:
    rx,ry,rz=rot_y(x,y,z, angle)
    rx,ry,rz=rot_x(rx,ry,rz,angle/2)
    s = 200 / (rz + 300)
    projected.append([rx*s,ry*s])
  draw(projected)
  angle=(angle+2)%360
  elapsed=time.time()-start
  if elapsed<frame_time:
    time.sleep(frame_time-elapsed)