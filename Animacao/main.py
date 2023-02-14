import turtle
import random

# Configurações iniciais da janela e da caneta
window = turtle.Screen()
window.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()

# Desenhe a lua
pen.goto(-200, 100)
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Desenhe as estrelas
for i in range(200):
    x = random.randint(-400, 400)
    y = random.randint(-200, 200)
    pen.goto(x, y)
    pen.dot(4)

# Esconder a caneta e exibir a janela
pen.hideturtle()
window.mainloop()