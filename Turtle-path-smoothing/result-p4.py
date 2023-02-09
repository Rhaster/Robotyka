from turtle import *
import ColabTurtle
import math
import random
from PIL import Image
import numpy as np
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.00.0\bin\gswin64c'
TURTLE_SIZE = 10

#inicjacja przestrzeni do rysowania,
drawing_area = Screen()
setworldcoordinates(0, 0, 1200,
                    1000)  #ustawienie wspolrzeędnej pixelowej dolej i górnej,

speed(1)  #szybkosc rysowania od 1 do 10,
factor = 150  #liczba pixeli na jednostkę,
iter_number = 10  # liczba iteracji wygladzania

turtle1 = Turtle()  #definicja agenta,

hideturtle()  #make the turtle invisible
penup()

#generacja losowych punktów trasy
liczba_punktow = 10
x = []
y = []
x.append(.5)
y.append(4.5)
temp_x = x[0]
temp_y = y[0]
a = 0
#przykladowe rysowanie prostokatnej przeszkody:
#lewa górna współrzędna przeszkody
left_top_corner_x = 3
left_top_corner_y = 5
obstacle_width = 1
#szerokosc przeszkody
obstacle_height = 3
#wysokosc przeszkody
turtle1.hideturtle()  #ukrycie ikony agenta,
turtle1.penup()  #wylaczenie rysowania
turtle1.setx(left_top_corner_x * factor)
turtle1.sety(left_top_corner_y * factor)
turtle1.showturtle()  #odkrycie ikony agenta
turtle1.pendown()  #wlaczenie rysowania
#rysownie wypelnionego kolorem niebieskim prostokata,
turtle1.fillcolor('green')
turtle1.begin_fill()
turtle1.setheading(
  0)  #ustawiamy poczatkowy kierunek na polnoc, pólnoc jest skierowna w prawo,
turtle1.forward(obstacle_width * factor)
turtle1.right(90)
turtle1.forward(obstacle_height * factor)
turtle1.right(90)
turtle1.forward(obstacle_width * factor)
turtle1.right(90)
turtle1.forward(obstacle_height * factor)
turtle1.right(90)
turtle1.end_fill()

turtle1.getscreen().getcanvas().postscript(file="map.png", colormode='color')

# otwarcie pliku PNG i zapisanie go do zmiennej
image = Image.open("map.png")
#print(image.type)
# wyświetlenie obrazu
##image.show()
color = image.getpixel((1, 1))
image.putpixel((100,100),(122,22,11))
image.show()
w,h = image.size
for x in range(0,w):
    for j in range(0,h):
        if(image.getpixel((x, j))!=(255,255,255)):
            print(x,j)
#img.save("map.png", "png")
## sprawdzenie poprawnosci
def test(lista):
  set_lista = set(lista)
  return all(x in set_lista for x in lista)


def czywliscie(list1, list2, element1, element2):
  return element1 in list1 and element2 in list2


for i in range(1, liczba_punktow):
  while True:
    choicex = random.choice([0, 1])
    temp_x = temp_x + choicex
    if temp_y > 3:
      temp_y = temp_y - 1
    else:
      temp_y = temp_y + random.choice([0, 1])
    # sprawdzenie, czy punkt już został dodany
    print(image.getpixel((temp_x, temp_y)))
    if (czywliscie(x, y, temp_x, temp_y) == False
        and (image.getpixel((temp_x, temp_y))==(255,255,255))):
      x.append(temp_x)
      y.append(temp_y)
      break
  #print(x)
  #print(y)
lista = []
i = 0
while (i < liczba_punktow):
  lista.append((x[i], y[i]))
  i += 1
print(test(lista))  ## zwraca True czyli nie zawiera powtarzajacych sie punktów
print(lista)
#path smoothing
x0 = x
y0 = y
alpha = .1
beta = .1


def iteracja():
  for i0 in range(0, iter_number):
    for i in range(1, 8):
      holderx = x[i]
      holdery = y[i]
      x[i] = x[i] + alpha * (x0[i - 1] + x0[i + 1] - 2 * x[i])
      y[i] = y[i] + alpha * (y0[i - 1] + y0[i + 1] - 2 * y[i])
      x[i] = x[i] + beta * (x0[i] - x[i])
      y[i] = y[i] + beta * (y0[i] - y[i])
      if (((abs(x[i] - holderx) < 0.001)) and ((abs(y[i] - holdery) < 0.001))
          and holderx != x[i] and holdery != y[i]):
        return


#the end of path smoothing
iteracja()

setx(x[0] * factor)
sety(y[0] * factor)
dot(20, "blue")

print(distance(x[1] * factor, y[1] * factor))

angle = math.atan2(y[1] * factor - y[0] * factor,
                   x[1] * factor - x[0] * factor) * 180 / 3.14
setheading(angle)

showturtle()  #make the turtle visible
pendown()

#rysowanie trasy przez punkty sciezki
for i in range(1, liczba_punktow):
  #ustalanie kierunku agenta do kolejnego punktu sciezki,
  angle = math.atan2(y[i] * factor - y[i - 1] * factor,
                     x[i] * factor - x[i - 1] * factor) * 180 / 3.14
  setheading(angle)
  forward(distance(x[i] * factor, y[i] * factor))
  dot(10, "blue")
  if i == liczba_punktow - 1:
    dot(20, "green")

