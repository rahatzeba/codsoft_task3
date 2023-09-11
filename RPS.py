from tkinter import *

from PIL import Image,ImageTk
from random import randint



root=Tk()

root.title(" ROCK PAPER SCISSOR GAME")

root.config(background="powderblue")


#picture

R_image=ImageTk.PhotoImage(Image.open("rock.png"))

P_image=ImageTk.PhotoImage(Image.open("paper.png"))

S_image=ImageTk.PhotoImage(Image.open("scissor.jpg"))


R_image_comp=ImageTk.PhotoImage(Image.open("rock.png"))

P_image_comp=ImageTk.PhotoImage(Image.open("paper.png"))

S_image_comp=ImageTk.PhotoImage(Image.open("scissor.jpg"))


#show pictute

user_choice=Label(root,image=R_image,background="powderblue")

user_choice.grid(row=2,column=0)

comp_choice=Label(root,image=R_image_comp,background="powderblue")

comp_choice.grid(row=2,column=4)


#PlayerSpecification

user=Label(root,text="USER",font=100,bg="powderblue",fg="black").grid(row=0,column=0)

comp=Label(root,text="COMPUTER",font=100,bg="powderblue",fg="black").grid(row=0,column=4)



#score

userScore=Label(root,text=0,font=100,bg="lightseagreen",fg="black")

compScore=Label(root,text=0,font=100,bg="lightseagreen",fg="black")

userScore.grid(row=2,column=1)

compScore.grid(row=2,column=3)


#playBUTTONS

rock=Button(root,command=lambda:updateChoice("rock"),width=20,height=2,text="ROCK",bg="lightslategrey",fg="black")

paper=Button(root,command=lambda:updateChoice("paper"),width=20,height=2,text="PAPER",bg="lightslategrey",fg="black")

scissor=Button(root,command=lambda:updateChoice("scissor"),width=20,height=2,text="scissor",bg="lightslategrey",fg="black")

rock.grid(row=3,column=1)

paper.grid(row=3,column=2)

scissor.grid(row=3,column=3)


#result

result=Label(root,font=100,bg="teal",fg="black",)

result.grid(row=4,column=2)


#result update

def updateResult(x):

    result['text']=x


#update score

def updateUserScore():
    score=int(userScore['text'])
    score+=1
    userScore["text"]=str(score)
def updateCompScore():
    score=int(compScore["text"])
    score+=1
    compScore['text']=str(score)



#updateChoices

RPS=["rock","paper","scissor"]   

def updateChoice(x):
    computerRandomChoice=RPS[randint(0,2)]


#for comp
    if computerRandomChoice=="rock":

        comp_choice.configure(image=R_image_comp)
    elif computerRandomChoice=="paper":

        comp_choice.configure(image=P_image_comp)

    elif computerRandomChoice=="scissor":

        comp_choice.configure(image=S_image_comp)
    else:
        pass

    

#for user    

    if x=="rock":

        user_choice.configure(image=R_image)

    elif x=="paper":

        user_choice.configure(image=P_image)  

    else:

        user_choice.configure(image=S_image)
    

    winner(x,computerRandomChoice)


#CHECK winner
def winner(player,computer): 
    if player==computer:
        updateResult("It's a DRAW")
    elif player=="rock":
        if computer=="paper":
            updateResult("YOU LOOSE")
            updateCompScore()
        else:
            updateResult("YOU WIN")
            updateUserScore()
    elif player=="paper":
        if computer=="scissor":
            updateResult("YOU LOOSE")
            updateCompScore()
        else:
            updateResult("YOU WIN")
            updateUserScore()
    elif player=="scissor":
        if computer=="rock":
            updateResult("YOU LOOSE")
            updateCompScore()
        else:
            updateResult("YOU WIN")
            updateUserScore()
    else:
        pass

root.mainloop()














'''import random

UC=int(input("enter 0 for Rock, 1 for paper or 2 for scissor :"))

CC=random.randint(0,2)

print("computers choice :",CC)

if UC>=3 and UC<0:

    print(" you entered the wrong choice")


else:

     if UC==CC:

      print(" It's a draw ")

     elif UC==0 and CC==2:

      print(" you win ")

     elif UC==1 and CC==2:

      print(" you win ")

     elif UC>CC:

      print(" you win ")

     elif UC<CC:

      print(" you lose ")'''