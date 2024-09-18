
from tkinter import *
from tkinter import messagebox
import random



timeleft=60
def timer():
    global timeleft,i
    if timeleft>0:
        timeleft-=1
        time_countLabel.config(text=timeleft)
        time_countLabel.after(1000,timer)
    else:
        wordEntry.config(state=DISABLED)
        result=correct_word-wrong_word
        instructionLabel.config(text=f'correct words {correct_word}\n Wrong Words {wrong_word}\n Final Score {result}')
        if result<15:
            emoji1Label.config(image=poorpic)
        if result>15:
            emoji1Label.config(image=poorpic)
        if result> 15:
            emoji1Label.config(image=poorpic)
        res=messagebox.askyesno('Confirm','Do you want to play again?')
        if res:
            i=0
            timeleft=10
            countLabel.config(text='0')
            time_countLabel.config(text='60')
            wordEntry.config(state=NORMAL)
            instructionLabel.config(text='Type Word And Hit Enter')
            emoji1Label.config(image='')
            emoji2Label.config(image='')

correct_word=0
wrong_word=0
i=0
def play_game(event):
    if wordEntry.get()!='':
        global i, correct_word, wrong_word
        i += 1
        countLabel.config(text=i)

        instructionLabel.config(text='')
        if timeleft == 60:
            timer()

        if wordEntry.get() == word_list_Label['text']:
            correct_word += 1
        else:
            wrong_word += 1

        random.shuffle(word_list)
        word_list_Label.config(text=word_list[0])
        wordEntry.delete(0, END)


word_list=['abroad','casual','around','couple','beyond','budget','during','device','eager','final','going','ideal',
'judge','metal','media','newly','known','local','might','noise','life','like','love','more','nose','near','open',
'only','push','pull','sell','sale','bad','her','rag','box','jug','sow','cut','lot','tap','dug','map','use','Nanjing'
,'Hankai','Academy']
#Functionality part
sliderwords=''
count=0
def slider():
    global sliderwords,count
    text='HKA 2ND TYPING COMPETITION'
    if count>=len(text):
        count=0
        sliderwords=''
    sliderwords=sliderwords+text[count]
    movingLabel.config(text=sliderwords)
    count+=1
    movingLabel.after(250,slider)


#GUI part
root=Tk()
root.title('HKA 2ND TYPING COMPETITION')
root.iconbitmap('hankailogo.ico')
root.geometry('1920x1080')
root.config(bg='burlywood3')
logoImage=PhotoImage(file='hkalogo4.png')
logoLabel=Label(root,image=logoImage,bg='burlywood3')
logoLabel.place(x=0,y=-27)
movingLabel=Label(root,text='',bg='burlywood3',font=('Helvetica',58,'bold italic'),fg=('blue4'))
movingLabel.place(x=270, y=50)
slider()
random.shuffle(word_list)
word_list_Label=Label(root,text=word_list[0],bg='burlywood3',font=('Helvetica',45,('italic bold')),fg=('coral4'))
word_list_Label.place(x=790,y=350,anchor=CENTER)

wordLabel=Label(root,text='WORDS:',font=('Helvetica',40,'italic bold'),bg='burlywood3')
wordLabel.place(x=300,y=350,anchor=CENTER)

countLabel=Label(root,text='0',font=('Helvetica',40,'italic bold'),bg='burlywood3')
countLabel.place(x=300,y=420,anchor=CENTER)

timelabel=Label(root,text='TIME:',font=('Helvetica',40,'italic bold'),bg='burlywood3')
timelabel.place(x=1280,y=350,anchor=CENTER)

time_countLabel=Label(root,text='60',font=('Helvetica',40,'italic bold'),bg='burlywood3')
time_countLabel.place(x=1280,y=420,anchor=CENTER)

wordEntry=Entry(root,font=('arial',25,'italic bold'),bd=10,justify=CENTER)
wordEntry.place(x=790,y=500,anchor=CENTER)
wordEntry.focus_set()

instructionLabel=Label(root,text='Type the words and click enter!',font=('Helvetica',35,'italic bold'),bg='burlywood3',
fg=('coral4'))
instructionLabel.place(x=790,y=700,anchor=CENTER)
poorpic=PhotoImage(file='mickey1.png')
goodpic=PhotoImage(file='tyson1.png')
propic=PhotoImage(file='tony1.png')
emoji1Label=Label(root,bg='burlywood3')
emoji1Label.place(x=1250,y=740)

root.bind('<Return>',play_game)



root.mainloop()

