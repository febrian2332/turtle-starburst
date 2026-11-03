
import turtle
import colorsys

LEBAR_LAYAR, TINGGI_LAYAR = 900, 900
JUMLAH_GARIS = 200
SUDUT_BELOK = 144        
PANJANG_AWAL = 4
PERTAMBAHAN_PANJANG = 3.2

screen = turtle.Screen()
screen.setup(LEBAR_LAYAR, TINGGI_LAYAR)
screen.bgcolor("black")
screen.title("Starburst Animasi - Turtle Graphics")
screen.tracer(1) 
screen.delay(0)  

t = turtle.Turtle()
t.speed(8)         
t.hideturtle()
t.pensize(2)
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(JUMLAH_GARIS):
    hue = (i / JUMLAH_GARIS) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(r, g, b)

    panjang = PANJANG_AWAL + i * PERTAMBAHAN_PANJANG
    t.forward(panjang)
    t.right(SUDUT_BELOK)
   
screen.update()


t2 = turtle.Turtle()
t2.hideturtle()
t2.penup()
t2.goto(-LEBAR_LAYAR / 2 + 20, TINGGI_LAYAR / 2 - 50)
t2.color("white")
t2.write("Starburst - klik jendela lalu tekan tombol apa saja untuk keluar",
          font=("Arial", 11, "normal"))

screen.listen()
screen.exitonclick()
