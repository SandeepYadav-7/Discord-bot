import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

prefix_list = ["N.", "n.", "Nezuko", "Nezuko ", "nezuko", "nezuko "]
bot = commands.Bot(command_prefix = prefix_list, description = "Still Development", case_insensitive=l = True, intents = intents)

for filename in os.listdir("./commands"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'commands.{filename[:-3]}')

keep_alive()
bot.run(os.getenv("TOKEN"))