from turtle import *
import ColabTurtle
import math
import random
import numpy as np

#functions ***********BEGGINING*************
""" 
draw_box#rysowanie pola mapy, na podstawie zdefiniowanego lewego gornego rogu

#pokazanie aktualnego prawdopodobienstwa na mapie,
#do przerobienia gdy zmienimy wiersz wysowania mapy
def show_p(mapa_size, world_row_position): 

#update prawdopodobienstwa po pomiarze, step1
def sense(sense_precision, sense_temp, mapa_size):
"""


#rysowanie pola mapy, na podstawie zdefiniowanego lewego gornego rogu
def draw_box(left_top_corner_x, left_top_corner_y, color):  #
  #szerokosc przeszkody
  obstacle_width = 1
  #wysokosc przeszkody
  obstacle_height = 1
  #ukrycie ikony agenta,
  turtle1.hideturtle()
  #wylaczenie rysowania
  left_top_corner_y += 2
  turtle1.penup()
  turtle1.setx(left_top_corner_x * factor)
  turtle1.sety(left_top_corner_y * factor)
  #wlaczenie rysowania
  turtle1.pendown()
  #rysownie wypelnionego kolorem niebieskim prostokata,
  turtle1.fillcolor(color)
  turtle1.begin_fill()
  #ustawiamy poczatkowy kierunek na polnoc, polnoc jest skierowna w prawo,
  turtle1.setheading(0)
  turtle1.forward(obstacle_width * factor)
  turtle1.right(90)
  turtle1.forward(obstacle_height * factor)
  turtle1.right(90)
  turtle1.forward(obstacle_width * factor)
  turtle1.right(90)
  turtle1.forward(obstacle_height * factor)
  turtle1.right(90)
  turtle1.end_fill()


#pokazanie aktualnego prawdopodobienstwa na mapie,
#do przerobienia gdy zmienimy wiersz wysowania mapy
def show_p(mapa_size, mapa_size2, world_row_position):  #
  for i in range(0, mapa_size):
    for j in range(0, mapa_size2):
      turtle1.penup()
      j += 2
      temp = i + 0.2
      turtle1.setx(temp * factor)
      turtle1.sety((j - 0.5) * factor)
      turtle1.write(np.around(probability[i][j - 2], decimals=3))


#update prawdopodobienstwa po pomiarze, step1
def sense(sense_precision, sense_temp, mapa_size, mapa_size2):  #
  for i in range(0, mapa_size):
    for j in range(0, mapa_size2):
      if (mapa[i][j] == sense_temp):
        probability[i][j] = probability[i][j] * sense_precision
      else:
        probability[i][j] = probability[i][j] * (1 - sense_precision)
  #update prawdopodobienstwa po pomiarze, step2
  #normalizacja,
  suma = np.sum(probability)  #
  for i in range(0, mapa_size):
    for j in range(0, mapa_size2):
      probability[i][j] = probability[i][j] / suma


#pamietamy ze swiat jest cykluczny z 6 trafiamy do 0, za pomoca modulo,
def move_right(mapa_size, mapa_size2, move_precision1, move_precision2,
               move_precision3):  #
  probability_apriori = probability.copy()
  for i in range(0, mapa_size):
    for j in range(0, mapa_size2):
      probability[i][j] = probability_apriori[i][j] * move_precision1
      probability[i][j] = probability[i][j] + probability_apriori[
        (i - 1) % mapa_size][(j - 1) % mapa_size2] * move_precision2
    probability[i][j] = probability[i][j] + probability_apriori[
      (i - 2) % mapa_size][(j - 2) % mapa_size2] * move_precision3


global max_index2


def find_max(mapa_size, mapa_size2):  ##
  #szukam max,
  temp_max = 0
  global max_index2
  #numer pola z wartoscia max
  max_index = 0
  for i in range(0, mapa_size):
    for j in range(0, mapa_size):
      if (probability[i][j] > temp_max):
        temp_max = probability[i][j]
        max_index = i
        max_index2 = j
  return max_index
  print('temp_max = ', temp_max)


def show_localized_agent(max_index, max_index2):
  for i in range(0, mapa_size):
    for j in range(0, mapa_size2):
      turtle1.penup()  #wylaczenie rysowania
      turtle1.setx((max_index + 0.4) * factor)
      turtle1.sety((max_index2 - 0.8) * factor)
      #turtle1.write('here')
  turtle1.showturtle()
  print('Agent localized itself')
  #arrow, turtle, circle, square, triangle,classic
  turtle1.shape("turtle")


def is_localized(mapa_size, mapa_size2, world_row_position):
  max_index = find_max(mapa_size, mapa_size2)
  global propability
  global max_index2
  temp_max = probability[max_index][max_index2]
  #sprawdzam czy max jest tylko jeden, jezeli tak wstawiam ikone agenta,
  count = 0
  for i in range(0, mapa_size):
    for j in range(0, mapa_size2):
      if probability[i][j] == temp_max:
        count = count + 1
    if count == 1:
      show_localized_agent(max_index, max_index2)
      print(max_index2)


#functions ***********THE END*************

#PROGRAM GLOWNY
#rysowani przestszeni, na podstawie lewej dolnej i prawej górnej koordynaty
drawing_area = Screen()
setworldcoordinates(-20, -20, 1200, 1200)

turtle1 = Turtle()  #definicja agenta,
turtle1.hideturtle()  #ukrycie ikony agenta,
turtle2 = Turtle()  #definicja agenta,
turtle2.hideturtle()  #ukrycie ikony agenta,

#liczba pixeli na jednostkę,
factor = 150

turtle1.speed(10)  #szybkosc rysowania od 1 do 10,

#definicja swiata, jest cykliczny, ruch tylko w prawo,
#przechodzac z pola 6 w prawo trafiamy do 0,
mapa = [['red', 'blue', 'red', 'orange', 'red', 'blue'],
        ['blue', 'orange', 'blue', 'orange', 'blue', 'blue'],
        ['orange', 'red', 'orange', 'red', 'yellow', 'red'],
        ['orange', 'orange', 'red', 'blue', 'yellow', 'yellow']]
mapa_size = len(mapa)
mapa_size2 = len(mapa[0])

#wizualizacja swiata
world_row_position = 5
for i in range(0, mapa_size):
  for j in range(0, mapa_size2):
    draw_box(i, j, mapa[i][j])

#inicjacja prawdopodobienstwa
global probability
probability = np.zeros((mapa_size, mapa_size2))
for i in range(0, mapa_size):
  for j in range(0, mapa_size2):
    probability[i][j] = (1 / mapa_size)

#prezentacja finalnego filra histogramowego
sense_precision = 0.8
move_precision1 = 0.1  #pozostanie w miejscu
move_precision2 = 0.8  #trafiamy do kratki docelowej
move_precision3 = 0.1  #trafiamy do kratki kolejnej
sense(sense_precision, 'orange', mapa_size, mapa_size2)
move_right(mapa_size, mapa_size2, move_precision1, move_precision2,
           move_precision3)
sense(sense_precision, 'yellow', mapa_size, mapa_size2)
move_right(mapa_size, mapa_size2, move_precision1, move_precision2,
           move_precision3)
sense(sense_precision, 'yellow', mapa_size, mapa_size2)
move_right(mapa_size, mapa_size2, move_precision1, move_precision2,
           move_precision3)
sense(sense_precision, 'yellow', mapa_size, mapa_size2)
move_right(mapa_size, mapa_size2, move_precision1, move_precision2,
           move_precision3)
sense(sense_precision, 'orange', mapa_size, mapa_size2)
move_right(mapa_size, mapa_size2, move_precision1, move_precision2,
           move_precision3)

#pokazanie obliczonego prawdopodobienstwa lokalizacji robota
show_p(mapa_size, mapa_size2, world_row_position)

#sprawdzenie czy robot zlokalizowal sie
is_localized(mapa_size, mapa_size2, world_row_position)
