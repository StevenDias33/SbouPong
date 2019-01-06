from tkinter import *
from SbouPad import Pad
import random

w = 700
h = 400

joueur1_score = 0
joueur2_score = 0

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.resizable(False, False)
root.geometry("{}x{}".format(w, 475))
root.title("SBOU Pong")

B1 = Button(root, text = "Quitter", command =root.destroy )
Button(root, text = "Quitter", command =root.destroy ).pack(side=BOTTOM, padx=5, pady=5)

c = Canvas(root, width=w, height=475, bg="black")
c.pack()


#tableau de score
joueur1 = Label(c, text="Player 1", font=("Arial", 20), fg="white", bg="#1050b7")
joueur1.place(relx=0.1, rely=0.9)

joueur2 = Label(c, text="Player 2", font=("Arial", 20), fg="white", bg="#1050b7")
joueur2.place(relx=0.735, rely=0.9)

#Score actuel 
score = Label(c, text="{} - {}".format(joueur1_score, joueur2_score), font=("Arial", 20), fg="white", bg="#1050b7")
score.place(relx=0.46, rely=0.9)

#Création de la balle 
ball = c.create_oval(w//2-20, h//2-20, w//2+20, h//2+20, fill="#EA9111", outline="#EA9111")
ball_R = (c.coords(ball)[2]-c.coords(ball)[0]) / 2

d = ball_R - (Pad.pad_width*(2*ball_R-Pad.pad_width))**0.5

#Les raquettes
left_pad = Pad(0, 0, c)
right_pad = Pad(w-Pad.pad_width, 0, c)


# Vecteurs random de la balle 
vx, vy = random.choice([-5, 5]), random.choice([6, -6])

def keypress(event):
	key = event.keysym
		
	if key.lower() == "w":
		left_pad.active = True
		left_pad.speed = -10

	if key.lower() == "s":
		left_pad.active = True
		left_pad.speed = 10

	if key == "Up":
		right_pad.active = True
		right_pad.speed = -10

	if key == "Down":
		right_pad.active = True
		right_pad.speed = 10

def keyrelease(event):
	key = event.keysym

	if key.lower() == "w" or key.lower() == "s":
		left_pad.active = False

	if key == "Up" or key == "Down":
		right_pad.active = False

def mouvement_balle():
	global vx, vy
	global joueur1_score, joueur2_score

	ball_coords = c.coords(ball)

	if ball_coords[1] == 0 or ball_coords[3] == h:
		vy = -vy
			

	left_pad_coords = c.coords(left_pad.pad)
	right_pad_coords = c.coords(right_pad.pad)

	touch_on_left = (left_pad_coords[0] <= ball_coords[0] <= left_pad_coords[2]) and ((left_pad_coords[1] <= ball_coords[3]-d <= left_pad_coords[3]) or (left_pad_coords[1] <= ball_coords[1]+d <= left_pad_coords[3]))
	touch_on_right = (right_pad_coords[0] <= ball_coords[2] <= right_pad_coords[2]) and ((right_pad_coords[1] <= ball_coords[3]-d <= right_pad_coords[3]) or (right_pad_coords[1] <= ball_coords[1]+d <= right_pad_coords[3]))

	if touch_on_right or touch_on_left:
		vx = -vx
		right_pad.speed = right_pad.speed + 3
		left_pad.speed = left_pad.speed + 3

			
	if ball_coords[0] <= 0:
		joueur2_score += 1
		but()
			

	if ball_coords[2] >= w:
		joueur1_score += 1
		but()
			

	c.move(ball, vx, vy)


def main():
	left_pad.mouvement()
	right_pad.mouvement()
	mouvement_balle()
	root.after(30, main)

def but():
	score.config(text="{} - {}".format(joueur1_score, joueur2_score))
	c.coords(ball, w//2-20, h//2-20, w//2+20, h//2+20)
		

c.bind("<KeyPress>",keypress)
c.bind("<KeyRelease>",keyrelease)
c.focus_set()

main()
root.mainloop()
