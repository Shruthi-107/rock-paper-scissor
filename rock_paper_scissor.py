from tkinter import *;
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")

#picture
rock_img= ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img= ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img= ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_img_comp= ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp= ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp= ImageTk.PhotoImage(Image.open("scissor.png"))
happy_user=ImageTk.PhotoImage(Image.open("happy_user.png"))
sad_user=ImageTk.PhotoImage(Image.open("sad_user.png"))
happy_comp=ImageTk.PhotoImage(Image.open("happy_comp.png"))
sad_comp=ImageTk.PhotoImage(Image.open("sad_comp.png"))


#insert picture
user_pic=Label(root,image=happy_user,bg="#9b59b6")
comp_pic=Label(root,image=happy_comp,bg="#9b59b6")
user_label=Label(root,image=paper_img,bg="#9b59b6")
comp_label=Label(root,image=paper_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=1)
user_label.grid(row=1,column=4)
user_pic.grid(row=0,column=4)
comp_pic.grid(row=0,column=1)

#scores
playerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerScore.grid(row=1,column=2)
playerScore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=2)

#messages
msg=Label(root,font=50,bg="#9b59b6",fg="white")    # text="YOU LOOSE"
msg.place(x=718,y=803)

#update message
def updateMessage(x):
    msg['text']=x

#playerNameLabel = Label(root, text="Player Name:", font=50, bg="#9b59b6", fg="white")
#playerNameLabel.grid(row=2, column=0)
#playerNameEntry = Entry(root, font=50)
#playerNameEntry.grid(row=2, column=1)
#playerScoreLabel = Label(root, text="Score: 0", font=50, bg="#9b59b6", fg="white")
#playerScoreLabel.grid(row=2, column=2)

#update user score
def updateUserScore():
    score=int(playerScore["text"])
    score += 1
    playerScore["text"]=str(score)

#update computer score
def updateCompScore():
    score=int(computerScore["text"])
    score += 1
    computerScore["text"]=str(score)

#update user and computer pictures
def updatePicture(x):
    if x==1:
        comp_pic.configure(image=sad_comp)
        user_pic.configure(image=happy_user)
    elif x==0:
        comp_pic.configure(image=happy_comp)
        user_pic.configure(image=sad_user)
    else:
        comp_pic.configure(image=happy_comp)
        user_pic.configure(image=happy_user)



#check winner
def checkWin(player,computer):
    x=2
    if player==computer:
        updateMessage("It's a tie!!!")
    elif player== "rock":
        if computer=="paper":
            updateMessage("You loose")
            updateCompScore()
            x=0
        else:     
            updateMessage("You Win")
            updateUserScore()
            x=1
    elif player=="paper":
        if computer=="scissor":
            updateMessage("You loose")
            updateCompScore()
            x=0
        else:
            updateMessage("You Win")
            updateUserScore()
            x=1
    elif player=="scissor":
        if computer=="rock":
            updateMessage("You loose")
            updateCompScore()   
            x=0   
        else:
            updateMessage("You Win")
            updateUserScore()       
            x=1
    else:
        pass  
    updatePicture(x)                    


#update choices
choices=["rock","paper","scissor"]

def updateChoice(x):

 #for computer
    compChoice=choices[randint(0,2)]

    if compChoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)      

 #for user
    if(x=="rock"):
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:   
        user_label.configure(image=scissor_img)    
    checkWin(x,compChoice)    


#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="black",command=lambda:updateChoice("rock"),activeforeground='red',font=("bold")).grid(row=2,column=2)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="black",command=lambda:updateChoice("paper"),activeforeground='red',font=("bold")).grid(row=2,column=3)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="black",command=lambda:updateChoice("scissor"),activeforeground='red',font=("bold")).place(x=717,y=507)#.grid(row=2,column=4)#.place(x=918,y=703)



root.mainloop()


