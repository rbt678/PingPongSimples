# Importar a biblioteca Turtle
import turtle

# Criar uma janela
janela = turtle.Screen()
janela.title("Jogo de Ping-Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(10)

# Criar a raquete esquerda
raquete_esq = turtle.Turtle()
raquete_esq.speed(0)
raquete_esq.shape("square")
raquete_esq.color("white")
raquete_esq.shapesize(stretch_wid=5, stretch_len=1)
raquete_esq.penup()
raquete_esq.goto(-350, 0)

# Criar a raquete direita
raquete_dir = turtle.Turtle()
raquete_dir.speed(0)
raquete_dir.shape("square")
raquete_dir.color("white")
raquete_dir.shapesize(stretch_wid=5, stretch_len=1)
raquete_dir.penup()
raquete_dir.goto(350, 0)

# Criar a bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.3 # Velocidade horizontal da bola
bola.dy = 0.3 # Velocidade vertical da bola

# Criar o placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
pontos_esq = 0 # Pontos do jogador esquerdo
pontos_dir = 0 # Pontos do jogador direito
placar.write(f"Esquerda: {pontos_esq} Direita: {pontos_dir}", align="center", font=("Courier", 24, "normal"))

# Funções para mover as raquetes
def raquete_esq_sobe():
    y = raquete_esq.ycor() # Pegar a coordenada y da raquete esquerda
    y += 40 # Aumentar em 20 pixels
    raquete_esq.sety(y) # Atualizar a coordenada y da raquete esquerda

def raquete_esq_desce():
    y = raquete_esq.ycor() # Pegar a coordenada y da raquete esquerda
    y -= 40 # Diminuir em 20 pixels
    raquete_esq.sety(y) # Atualizar a coordenada y da raquetes esquerda

def raquetes_dir_sobe():
    y = raquete_dir.ycor() # Pegar a coordenada y da rauete direita
    y += 40 # Aumenta emr 20 pixels
    raquete_dir.sety(y) # Atualizar a coordenada y da rauete direita

def rauete_dir_desce():
    y = raquete_dir.ycor() # Pegara coordenada y da rauete direita
    y -= 40 # Diminuir emr pixels
    raquete_dir.sety(y) # Atualizar aa coordenada yr auete direita

# Vincular as teclas às funções das racquetes
janela.listen()
janela.onkeypress(raquete_esq_sobe,"w")
janela.onkeypress(raquete_esq_desce,"s")
janela.onkeypress(raquetes_dir_sobe,"Up")
janela.onkeypress(rauete_dir_desce,"Down")

# Loop principal do jogo
while True:
   janela.update()

   bola.setx(bola.xcor() + bola.dx)
   bola.sety(bola.ycor() + bola.dy)

   if bola.ycor() >290:
      bola.sety(290)
      bola.dy *= -1

   if bola.ycor() < -290:
      bola.sety(-290)
      bola.dy *= -1

   if bola.xcor() > 390:
      bola.goto(0, 0)
      bola.dx *= -1
      pontos_esq += 1
      placar.clear()
      placar.write(f"Esquerda: {pontos_esq} Direita: {pontos_dir}", align="center", font=("Courier", 24, "normal"))

   if bola.xcor() < -390:
      bola.goto(0, 0)
      bola.dx *= -1
      pontos_dir += 1
      placar.clear()
      placar.write(f"Esquerda: {pontos_esq} Direita: {pontos_dir}", align="center", font=("Courier", 24, "normal"))

   if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_dir.ycor() + 50 and bola.ycor() > raquete_dir.ycor() -50):
      bola.setx(340)
      bola.dx *= -1

   if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_esq.ycor() + 50 and bola.ycor() > raquete_esq.ycor() -50):
      bola.setx(-340)
      bola.dx *= -1

   if pontos_esq == 10 or pontos_dir == 10:
       placar.clear()
       placar.write(f"Fim de jogo! Esquerda: {pontos_esq} Direita: {pontos_dir}", align="center", font=("Courier", 24, "normal"))
       break
