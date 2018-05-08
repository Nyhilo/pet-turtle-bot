#pet-turtle-bot
import discord
from discord.ext import commands
import sys

NAME = 'Bok Choy'


with open("token",'r') as f:
    TOKEN = f.read()

with open("ascii_sprite",'r') as f:
    SPRITE = "".join(f.readlines())


def main():
    #Prefix
    bot = commands.Bot(command_prefix='!', description="A bot for running a community pet keeping game. The app will keep track of a pet's hunger, happiness, and health as well as other stats.")

    @bot.event
    async def on_ready():
        print("Python version", sys.version)
        print(SPRITE[3:-3])
        print('Logged in as', bot.user.name)
        print("Discord API version: " + discord.__version__)

    msg = ""

    @bot.command()
    async def hello():
        msg = await bot.say('Hi! My name is ' + NAME)

    @bot.command(msg)
    async def revise():
        await bot.edit_message(msg,'Hi! This message has been edited')

    @bot.command()
    async def turtle():
        await bot.say(SPRITE)

    bot.run(TOKEN)

  

if __name__ == '__main__':  
    if len(sys.argv) > 1:
        if (sys.argv[1].lower() == "-test" or sys.argv[1].lower() == "-t"):
            print("Testing...")
        else:
            main()
    else:
        main()