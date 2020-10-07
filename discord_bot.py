# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = "NzYwNjE0MTE0OTg4NTIzNTMx.X3OnGA.IJuwyOR7ZkCY-a_gS3yS4-zh0Ps"
GUILD = "Simply survival MC server"

numof = 0

client = discord.Client()
bot = commands.Bot(command_prefix='!')
print("hi")

@bot.command()
async def rolea(ctx, arg):
    print("GGGGGGGGGGGGGGGGGGGGGGGGGGG")
    await ctx.send(arg)
    role = discord.utils.get(ctx.guild.roles, name = "Admin") 
    await ctx.add_roles(role)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


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
        #---------------Votetine----------------------
        if message.content == "!vote":
            if numof >= 1:
                numof += 1
            elif numof == 0:
                numof = 1
            print(numof)
            await message.channel.send(numof)
        if message.content == "!clense":
            #await message.channel.send(message.author.id)
            if message.author.id == 277920295833305088 or message.author.id == 408821725128818688:
                await message.channel.send("Clensing")

                
                

#----------------------BANMETHOD-------------
@bot.command(pass_context=True)
@commands.has_role("Admin") # This must be exactly the name of the appropriate role
async def addrole(ctx):
    member = ctx.message.author
    role = get(member.server.roles, name="Test")
    await bot.add_roles(member, role)

@bot.event
async def on_message_delete(message):
    """
    This is called when a message is deleted.
    For older messages, it's possible that this event
    might not get triggered.
    Args:
        message:
             A Message object of the deleted message.
    """
    print("This message been deleted:", message)

def voteamong():
    numof += 1
    
bot.run(TOKEN)
