import discord
from discord.ext import commands
import json
import requests
import asyncio
import aiohttp

class GIF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
    

def setup(bot):
    bot.add_cog(GIF(bot))