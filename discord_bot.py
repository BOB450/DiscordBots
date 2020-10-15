# bot.py
import os
import random
import discord
from discord.ext import commands

from phue import Bridge
import logging
logging.basicConfig()

b = Bridge('192.168.0.4')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single$
#b.connect()

TOKEN = "NzYwNjE0MTE0OTg4NTIzNTMx.X3OnGA.IJuwyOR7ZkCY-a_gS3yS4-zh0Ps"
GUILD = "Simply survival MC server"


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
        print("Code: ",message.content)
        res = "The Among Us code is: ",message.content
        await message.channel.send(res)
        await message.channel.send("To use code go to online and type the code into the box")
        
    #-----------Commands-------------------------------------------------------
    if "!" in message.content:
        print("command")
        if message.content == "!Turn on Lights":
                lightcontroll(1,True)
                await message.channel.send("Turning on lights")
        if message.content == "!Turn off Lights":
                        lightcontroll(1,False)
                        await message.channel.send("Turning off lights")
        if message.content == "!Turn on Room Lights":
                        lightcontroll(3,True)
                        lightcontroll(4,True)
                        lightcontroll(5,True)
                        await message.channel.send("Turning on lights")
        if message.content == "!Turn off Room Lights":
                        lightcontroll(3,False)
                        lightcontroll(4,False)
                        lightcontroll(5,False)
                        await message.channel.send("Turning off lights")
        if message.content == "!help":
                        await message.channel.send("This Bot controlls Rowans Lights")
                        await message.channel.send("!Turn on Room Lights | Turns on by bedroom lights")
                        await message.channel.send("!Turn off Room Lights | Turns off by bedroom lights")
                        await message.channel.send("!Turn on Lights | Turns on Light next to computer")
                        await message.channel.send("!Turn off Lights | Turns off Light next to computer")
        if message.content == "!Wake Rowan Up":
                        lightcontroll(3,False)
                        lightcontroll(4,False)
                        lightcontroll(5,False)
                        




bot.run(TOKEN)
