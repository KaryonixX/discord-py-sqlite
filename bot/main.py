import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("Logged in as {}({})".format(bot.user.name, bot.user.id))

bot.run(TOKEN)