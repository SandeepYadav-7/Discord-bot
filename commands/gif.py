import discord
from discord.ext import commands
import json
import requests
import asyncio
import aiohttp

class GIF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("test is working!")
    
    

def setup(bot):
    bot.add_cog(GIF(bot))