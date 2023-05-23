#Импорт модулей
import tkinter
import turtle
import time
import random

score = 0          #счет
high_score = 0     #наибольший счет
delay = 0.1        #время задержки

# Создание экрана для игры
wind = turtle.Screen()
wind.title("ЗМЕЙКА")    #Название игры
wind.bgcolor("#94F041") #Цвет экрана
 
# Ширина и высота экрана
wind.setup(width=1000, height=800)
wind.tracer(0) #Значение задержки обновления экрана

# Создание головы змеи
snake = turtle.Turtle()
snake.shape("square")   #Форма головы змеи
snake.color("green")    #Цвет головы змеи
snake.penup()           #Перемещение змеи без рисования линии
snake.goto(0, 0)        #Координаты головы змеи
snake.direction = "Stop"

# Создание еды для змеи
apple = turtle.Turtle()
colors = random.choice(['yellow', 'red']) #Цвет еды
shapes = random.choice(['circle']) #Форма еды
apple.shape(shapes)
apple.color(colors)
apple.speed(0)
apple.penup()
apple.goto(0, 300)
 
# Создание счета
score1 = turtle.Turtle()
score1.shape("square")
score1.color("white")
score1.speed(0)
score1.penup()
score1.hideturtle()
score1.goto(-300,373)
score1.write("Score : 0  High Score : 0", align="center",
font=("Verdana", 21, "bold"))

# Назначение движения змеи
def goup():
    if snake.direction != "down":
        snake.direction = "up"
 
def godown():
    if snake.direction != "up":
        snake.direction = "down"
 
def goleft():
    if snake.direction != "right":
        snake.direction = "left"
 
def goright():
    if snake.direction != "left":
        snake.direction = "right"

 
def move():
    if snake.direction == "up":
        y = snake.ycor()    #Положение головы змеи по y-координату
        snake.sety(y+20)    #Изменяет y-координату черепахи на ypos.
                            #Это перемещает черепаху вертикально.
                            #Направление черепахи не меняется.

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)

    if snake.direction == "left":
        x = snake.xcor()    #положение головы змеи по x-координату
        snake.setx(x-20)    #Изменяет x-координаты черепахи на xpos.
                            #Это перемещает черепаху горизонтально.
                            #Направаление черепахи не меняется.
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)
        
wind.listen()
wind.onkeypress(goup, "w")
wind.onkeypress(godown, "s")
wind.onkeypress(goleft, "a")
wind.onkeypress(goright, "d")


# Игровой процесс
segments = []

while True:
    wind.update()
    #Проверка столкновения змеи с экраном
    if snake.xcor() > 509 or snake.xcor() < -479 or snake.ycor() > 378 or snake.ycor() < -360:
        time.sleep(0.1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score1.clear()
        score1.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Veranda", 24, "bold"))
    if snake.distance(apple) < 15:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)
 
        # Добавление тела змеи
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("yellow")  
        body.penup()
        segments.append(body)

        score += 1  
        if score > high_score:
            high_score = score
            score1.clear()
            score1.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Veranda", 24, "bold"))
# Проверка столкноввения змеи с телом
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
    move()

    time.sleep(delay)
wind.mainloop()

