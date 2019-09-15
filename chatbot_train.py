from tkinter import *
from chatterbot import ChatBot
import pyttsx3 as pp
from chatterbot.trainers import ListTrainer
import os



def setup():
    bot = ChatBot('Norman')
    trainer=ListTrainer(bot)
    for files in os.listdir("data"):

        convo=open("data/"+files,'r').readlines()
        trainer.train(convo)
    print()
    custom_convo=["Who is Soumya Gupta ?","He is my creator "]
    trainer.train(custom_convo)
    print("Training Completed !!")

setup()
