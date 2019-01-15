from tkinter import *
from SbouPad import Pad
import random

w = 700
h = 400

axel_score = 0
paris_score = 0

fenetre = Tk()
menubar = Menu(fenetre)
fenetre.config(menu=menubar)
fenetre.resizable(False, False)
fenetre.geometry("{}x{}".format(w, 475))
fenetre.title("SBOU Pong")

B1 = Button(fenetre, text = "Quitter", command =fenetre.destroy )
Button(fenetre, text = "Quitter", command =fenetre.destroy ).pack(side=BOTTOM, padx=5, pady=5)

canvas = Canvas(fenetre, width=w, height=475, bg="black")
canvas.pack()

#def menu():
#	c.delete(ALL)
#	c.create_text(400, 200, fill= "white", font=("Arial", 40),text ="Accueil")


#tableau de score
axel = Label(canvas, text="Player 1", font=("Arial", 20), fg="white", bg="black")
axel.place(relx=0.1, rely=0.9)

paris = Label(canvas, text="Player 2", font=("Arial", 20), fg="white", bg="black")
paris.place(relx=0.735, rely=0.9)

#Score actuel 
score = Label(canvas, text="{} - {}".format(axel_score, paris_score), font=("Arial", 20), fg="white", bg="#1050b7")
score.place(relx=0.46, rely=0.9)

#Création de la balle 
ball = canvas.create_oval(w//2-20, h//2-20, w//2+20, h//2+20, fill="orange", outline="#EA9111")
ball_R = (canvas.coords(ball)[2]-canvas.coords(ball)[0]) / 2

d = ball_R - (Pad.pad_width*(2*ball_R-Pad.pad_width))**0.5

#Les raquettes
quentin_pad = Pad(0, 0, canvas)
gans_pad = Pad(w-Pad.pad_width, 0, canvas)


# Vecteurs random de la balle 
vx, vy = random.choice([-5, 5]), random.choice([6, -6])

#ici c'est pour faire des choses quand on appui sur les touches c'est cool 
def touchepresse(event):
	key = event.keysym
		
	if key.lower() == "w":
		quentin_pad.active = True
		quentin_pad.speed = -10

	if key.lower() == "s":
		quentin_pad.active = True
		quentin_pad.speed = 10

	if key == "Up":
		gans_pad.active = True
		gans_pad.speed = -10

	if key == "Down":
		gans_pad.active = True
		gans_pad.speed = 10
#c'est pour éviter les guignols qui appuis tout le temps sur la meme touche pour spamm 
def touche(event):
	key = event.keysym

	if key.lower() == "w" or key.lower() == "s":
		quentin_pad.active = False

	if key == "Up" or key == "Down":
		gans_pad.active = False
#j'ai pas besoin de commenter tout est dans le nom de la fonction toutefois ici on fait bouger la balle DU DU DU DU 
def mouvement_balle():
	global vx, vy
	global axel_score, paris_score

	ball_coords = canvas.coords(ball)

	if ball_coords[1] == 0 or ball_coords[3] == h:
		vy = -vy
			

	quentin_pad_coords = canvas.coords(quentin_pad.pad)
	gans_pad_coords = canvas.coords(gans_pad.pad)

	touch_on_quentin = (quentin_pad_coords[0] <= ball_coords[0] <= quentin_pad_coords[2]) and ((quentin_pad_coords[1] <= ball_coords[3]-d <= quentin_pad_coords[3]) or (quentin_pad_coords[1] <= ball_coords[1]+d <= quentin_pad_coords[3]))
	touch_on_gans = (gans_pad_coords[0] <= ball_coords[2] <= gans_pad_coords[2]) and ((gans_pad_coords[1] <= ball_coords[3]-d <= gans_pad_coords[3]) or (gans_pad_coords[1] <= ball_coords[1]+d <= gans_pad_coords[3]))

	if touch_on_gans or touch_on_quentin:
		vx = -vx
		gans_pad.speed = gans_pad.speed + 3
		quentin_pad.speed = quentin_pad.speed + 3

			
	if ball_coords[0] <= 0:
		paris_score += 1
		but()
			

	if ball_coords[2] >= w:
		axel_score += 1
		but()
			

	canvas.move(ball, vx, vy)

# éxécution du code au lancement de l'appli 
def main():
	quentin_pad.mouvement()
	gans_pad.mouvement()
	mouvement_balle()	
	fenetre.after(30, main)
	return 0
#SECOND POTEAU non plus serieusement ici on met le point au joueur et on remet la balle au centre 
def but():
	score.config(text="{} - {}".format(axel_score, paris_score))
	canvas.coords(ball, w//2-20, h//2-20, w//2+20, h//2+20)
		

#start = Button(fenetre, text="commencer", command=main).pack(side=BOTTOM, padx=5, pady=4)


canvas.bind("<KeyPress>",touchepresse)
canvas.bind("<KeyRelease>",touche)
canvas.focus_set()
main()
fenetre.mainloop()
