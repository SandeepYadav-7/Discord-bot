import discord
from discord.ext import commands
import requests
import json
import asyncio
import aiohttp

class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "cat",
        aliases = ["kitty"]
        )
    async def cat(self, ctx):
        response = requests.get("https://aws.random.cat/meow")
        data = response.json()
        
        em = discord.Embed(
            title = "A random cat",
            color = discord.Color(0xffff)
            )
        em.set_image(url = data['file'])
        em.set_footer(text = "Shared by someone")
        
        await ctx.send(embed = em)
    
    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            response = await session.get("https://some-random-api.ml/img/dog")
            data = await response.json()
            
            em = discord.Embed(
                title = "A random dog",
                color = discord.Color(0xffff)
                )
            em.set_image(url = data['link'])
            em.set_footer(text = "Shared by someone")
            
            await ctx.send(embed = em)
    
    @commands.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            response = await session.get("https://randomfox.ca/floof")
            data = await response.json()
            
            em = discord.Embed(
                title = "A random fox",
                color = discord.Color(0xffff)
                )
            em.set_image(url = data['image'])
            em.set_footer(text = "Shared by someone")
            
            await ctx.send(embed = em)
    
    


def setup(bot):
    bot.add_cog(Animals(bot)