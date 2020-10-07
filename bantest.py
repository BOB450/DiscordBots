import discord
from discord.ext import commands
TOKEN = "NzYwNjE0MTE0OTg4NTIzNTMx.X3OnGA.IJuwyOR7ZkCY-a_gS3yS4-zh0Ps"      # Put your Bot token here
SKIP_BOTS = False


bot = commands.Bot(command_prefix='!')

@bot.command()
async def hello(ctx, user: discord.Member, role: discord.Role):  # note: discord commands must be coroutines, so define the function with `async def`
    # the ctx argument is automatically passed as the first positional argument

    # you can access the author (type discord.Member) and channel (type discord.TextChannel) of the command as followed:
    message_author = ctx.author
    message_channel = ctx.channel

    
    #role = discord.utils.get(ctx.guild.roles, name = "Admin") 
    await user.add_roles(role)
    

    
bot.run(TOKEN)