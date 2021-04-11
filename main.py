import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix "!", case_insensitive = True)

@bot.command(name = "ping")
async def ping(ctx):
  msg = await ctx.send(f"hey {ctx.message.author.mention}, pong! latency")
  await msg.edit(content = f"hey {ctx.message.author.mention}, pong! latency is {round(bot.latency * 1000)}ms")
  

keep_alive()
bot.run(os.getenv("TOKEN"))