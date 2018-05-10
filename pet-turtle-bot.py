# TODO List
# * Add gender to pet, format this throughout bot responses
# * Add more age-related sprites
# * Move responses to a more readable external file
# * Have the pet keep track of what's given to it


# pet-turtle-bot
import discord
from discord.ext import commands
import sys
import time
from datetime import datetime
from random import choice

# Vars #
UPDATE = 15  # Time between updates in minutes

with open("token", 'r') as f:
    TOKEN = f.read()

# Sprite file can contain multiple ascii art sprites, each seperated by a $
with open("ascii_sprite", 'r') as f:
    SPRITES = "".join(f.readlines()).split('$')

# Possible responses by category
responses = {
    'happy': ["{} nudges a stone with his snout."],
    'feed':  ["{} gently nibbles the lettuce from your hand.",
              "{} eats with ravenous glee."],
    'play':  ["{} looks like he's having fun!"],
    'sick':  ["{} is looking pale and sickly.",
              "{} is looking sluggish and doesn't want to move."],
    'sleep': ["{} is currently snoozing, you can type &awake to wake him up.",
              "{} is currently in a deep sleep, you can type &awake to wake him up.",
              "{} is currently asleep, you can type &awake to wake him up."]
}


# Misc Functions #
def chooseResponse(category):
    if category in responses:
        return choice(responses[category])
    else:
        return "{} is sitting there, being idle."


# Pet Class #
class Pet(object):
    """docstring for Pet"""
    def __init__(self, name, spritelist):
        self.name = name
        # self.birthday = datetime(year=2017, month=5, day=8)
        self.birthday = datetime.utcnow()
        self.sprite = spritelist
        self.statSplit = 5
        self.maxstat = 100
        self.happiness = 100
        self.hunger = 100
        self.health = 100
        self.status = "Healthy"
        self.sleep = 100
        self.growth = 0  # Growth is what sprite is displayed
        self.growthrate = 1

    def respond(self, string):
        # {} in the string will be replaced with the pet's name
        return "*" + string.format(self.name) + "*"

    def statmod(self, stat, value):
        stat += value
        if stat > self.maxstat:
            stat = maxstat
        if stat < 0:
            stat = 0;

    def logic(self):
        pass

    def feed(self, amount=1):
        if self.hunger/self.maxstat < .1:
            msg = "{} looks so relieved. He was almost starving!"
        if self.hunger >= self.maxstat:  #Pet is allowed to be overfed, but not when already full
            msg = "{} doesn't look very hungry now."
        elif self.status == "Sick":
            msg = chooseResponse('sick') + " He doesn't seem to want to eat anything."
        else:
            amountTilFull = (self.maxstat - self.hunger) % 30) + 1
            if amount > amountTilFull:
                msg = "That's way too much! {} only eats what he can handle."
                amount = amountTilFull
            else:
                msg = chooseResponse('feed')
            self.hunger += 30*amount

        return self.respond(msg)

    def play(self):
        if self.status == "sick":
            msg = chooseResponse('sick') + " He doesn't want to play right now."
        elif self.hunger < 5:
            msg = "{} is too hungry to play right now!"
        else:
            self.statmod(self.happiness, 40)
            self.statmod(self.health, 10)
            self.statmod(self.hunger, -5)

            msg = chooseResponse('play')
        return self.respond(msg)

    def treat(self):
        pass    # Given medicine

    def getStatBar(self, value):
        if value > self.maxstat:
            value = maxstat

        fill = int(value / self.statSplit)
        rest = int(self.maxstat/self.statSplit) - fill
        # return ('█' * fill) + (' ' * rest)
        return ('|' * fill) + (' ' * rest)

    def calculateAge(self):
        diff = datetime.utcnow() - self.birthday
        if diff.days < 14:
            return str(diff.days) + (" day" if diff.days == 1 else " days")
        elif diff.days < 70:
            num = int(diff.days/7)
            return str(num) + (" week" if num == 1 else " weeks")
        elif diff.days < 365:
            num = int(diff.days/30.5)
            return str(num) + (" month" if num == 1 else " months")
        else:
            num = int(diff.days/364.25)
            return str(num) + (" year" if num == 1 else " years")

    def format(self):
        outstring = self.sprite[self.growth]
        outstring += "\n\n Name: " + self.name + "    Status: " + self.status + "    Age: " + self.calculateAge()
        outstring += "\n HAP [" + self.getStatBar(self.happiness) + "]    HUNG [" + self.getStatBar(self.hunger) + "]"
        outstring += "\n SLP [" + self.getStatBar(self.health) +    "]    HLTH [" + self.getStatBar(self.hunger) + "]"
        return outstring


pet = Pet("Bok Choy", SPRITES)
print(pet.format())
print(pet.respond("{} string"))

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
