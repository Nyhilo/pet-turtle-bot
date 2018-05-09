#pet-turtle-bot
import discord
from discord.ext import commands
import sys
import time
from datetime import datetime
from random import choice

# Vars #
with open("token",'r') as f:
    TOKEN = f.read()

# Sprite file can contain multiple ascii art sprites, each seperated by a $
with open("ascii_sprite",'r') as f:
    SPRITES = "".join(f.readlines()).split('$')

# Possible responses by category
responses = {
    'happy': ["{} nudges a stone with their snout."]
}

# Misc Functions #
def chooseResponse(category):
    pass


# Pet Class #
class Pet(object):
    """docstring for Pet"""
    def __init__(self, name, spritelist):
        self.name = name
        self.birthday = datetime(year=2017, month=5, day=8)
        # self.birthday = datetime.utcnow()
        self.sprite = spritelist
        self.statSplit = 5
        self.maxstat = 100
        self.happiness = 100
        self.hunger = 100
        self.health = 100
        self.status = "Healthy"
        self.sleep = 100
        self.growth = 0 #Growth is what sprite is displayed
        self.growthrate = 1

    def msg(self, string):
        # {} in the string will be replaced with the pet's name
        return "*" + string.format(self.name) + "*"

    def logic(self):
        pass

    def feed(self, amount=1):
        if self.hunger/self.maxstat < .2:
            msg = "{} looks"
        self.hunger +=30

    def getStatBar(self, value):
        fill = int(value / self.statSplit)
        rest = int(self.maxstat/self.statSplit) - fill
        # return ('█' * fill) + (' ' * rest)
        return ('|' * fill) + (' ' * rest)

    def calculateAge(self):
        diff = datetime.utcnow() - self.birthday
        if diff.days < 14:
            return str(diff.days) + (" day" if diff.days==1 else " days")
        elif diff.days < 70:
            num = int(diff.days/7)
            return str(num) + (" week" if num==1 else " weeks")
        elif diff.days < 365:
            num = int(diff.days/30.5)
            return str(num) + (" month" if num==1 else " months")
        else: 
            num = int(diff.days/364.25)
            return str(num) + (" year" if num==1 else " years")

    def format(self):
        outstring = self.sprite[self.growth]
        outstring += "\n\n Name: " + self.name + "    Status: " + self.status + "    Age: " + self.calculateAge()
        outstring += "\n HAP [" + self.getStatBar(self.happiness) + "]    HUNG [" + self.getStatBar(self.hunger) + "]"
        outstring += "\n SLP [" + self.getStatBar(self.health)    + "]    HLTH [" + self.getStatBar(self.hunger) + "]"
        return outstring


pet = Pet("Bok Choy", SPRITES)
print(pet.format())


# #Prefix
# bot = commands.Bot(command_prefix='!', description="A bot for running a community pet keeping game. The app will keep track of a pet's hunger, happiness, and health as well as other stats.")


# # Bot Functions #
# @bot.event
# async def on_ready():
#     print("Python version", sys.version)
#     print(SPRITE[3:-3])
#     print('Logged in as', bot.user.name)
#     print("Discord API version: " + discord.__version__)



# @bot.command()
# async def hello():
#     bot.msg = await bot.say('Hi! My name is ' + NAME)

# @bot.command()
# async def revise():
#     await bot.edit_message(bot.msg,'Hi! This message has been edited')

# @bot.command()
# async def turtle():
#     await bot.say(SPRITE)

# bot.run(TOKEN)