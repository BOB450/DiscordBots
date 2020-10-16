# bot.py
import os
import random
import discord
from discord.ext import commands

from phue import Bridge
import logging
import time
logging.basicConfig()

b = Bridge('192.168.0.4')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single$
#b.connect()

TOKEN = "NzYwNjE0MTE0OTg4NTIzNTMx.X3OnGA.IJuwyOR7ZkCY-a_gS3yS4-zh0Ps"
GUILD = "Simply survival MC server"

#create data file 


client = discord.Client()
bot = commands.Bot(command_prefix='!')
print("hi")

def lightcontroll(light,state):#pass in light as int and statee as a true or false
    b.set_light(light, 'on', state)

@bot.event
async def on_message(message):
    
    print("Received a message:", message.content)
    #------------Messages------------------------------------------------------
    if len(message.content) == 6 and message.content.isupper():
        f= open("gbot_data.txt","w+")
        print("Code: ",message.content)
        code = message.content
        f.write(code)
        res = "The Among Us code is: ",message.content
        #await message.channel.send(res)
        #await message.channel.send("To use code go to online and type the code into the box")
        
    if message.content  == "!code":
        f=open("gbot_data.txt", "r")
        rcode =f.read()
        messagecode = 'The current among us code is: '+ rcode
        print(messagecode)
        await message.channel.send(messagecode)
    #-----------Commands-------------------------------------------------------
    if "!" in message.content:
        print("command")
        if message.content == "!Turn on Lights":
                lightcontroll([1],True)
                await message.channel.send("Turning on lights")
        if message.content == "!Turn off Lights":
                        lightcontroll([1],False)
                        await message.channel.send("Turning off lights")
        if message.content == "!Turn on Room Lights":
                        lightcontroll([3,4,5,6],True)
                        #lightcontroll(4,True)
                        #lightcontroll(5,True)
                        await message.channel.send("Turning on lights")
        if message.content == "!Turn off Room Lights":
                        lightcontroll([3,4,5,6],False)
                        #lightcontroll(4,False)
                        #lightcontroll(5,False)
                        await message.channel.send("Turning off lights")
        if message.content == "!help":
                        await message.channel.send("!code | Recive the latest among us code")
                        await message.channel.send("------------------------------------------------------------------------------------")
                        await message.channel.send("This Bot controlls Rowans Lights")
                        await message.channel.send("!Turn on Room Lights | Turns on by bedroom lights")
                        await message.channel.send("!Turn off Room Lights | Turns off by bedroom lights")
                        await message.channel.send("!Turn on Lights | Turns on Light next to computer")
                        await message.channel.send("!Turn off Lights | Turns off Light next to computer")




bot.run(TOKEN)
