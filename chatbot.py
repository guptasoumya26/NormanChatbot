
from tkinter import *
from PIL import ImageTk, Image
from chatterbot import ChatBot
import pyttsx3 as pp
from chatterbot.trainers import ListTrainer
import os


engine=pp.init()
bot = ChatBot('Norman',
            logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        },
                {
                      'import_path': 'chatterbot.logic.TimeLogicAdapter'  
                        },
                        {
                        'import_path': 'chatterbot.logic.MathematicalEvaluation'  
                        }
    ]
        
   )
voices=engine.getProperty('voices')


engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()





root = Tk()
root.title("Norman in your service !!")
#root.geometry("480x400")

img_gif=PhotoImage(file='chatbot.gif')
## Displaying in Label
photoLabel=Label(image=img_gif)
photoLabel.pack()

frame=Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=90,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()


## Creating text field
textF=Entry(root,font=("Verdana",20))
textF.pack(fill=X,pady=10)

def askFromBot():
    query=textF.get()
    ans_from_bot=bot.get_response(query)
    msgs.insert(END,"You : "+query)
    msgs.insert(END,"Norman : "+str(ans_from_bot))
    speak(ans_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
    
    
btn=Button(root,text="Ask from Norman",font=("Verdana",10),command=askFromBot)
btn.pack()


## creating a function for enter key
def enterKey_function(event):
    btn.invoke()

## going to bind main window with enter key
root.bind('<Return>',enterKey_function)


root.mainloop()


# In[ ]:




