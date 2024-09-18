from tkinter import *
import random
word_list=['Abroad','Casual','Around','Couple','Beyond','Budget','During','Device','Eager','Final','Going','Ideal',
'Judge','Metal','Media','Newly','Known','Local','Might','Noise','Life','Like','Love','More','Nose','Near','Open',
'Only','Push','Pull','Sell','Sale','Bad','Her','Rag','Box','Jug','Sow','Cut','Lot','Tap','Dug','Map','Use','Nanjing'
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
movingLabel=Label(root,text='',bg='burlywood3',font=('Helvetica',58,'bold italic'))
movingLabel.place(x=270, y=50)
slider()
random.shuffle(word_list)
word_list_Label=Label(root,text=word_list[0],bg='burlywood3',font=('Helvetica',45,('italic bold')))
word_list_Label.place(x=790,y=350,anchor=CENTER)

wordLabel=Label(root,text=)

root.mainloop()

