import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "say",
        aliases = ["repeat"]
        )
    async def say(self, ctx, *, msg):
        await ctx.send(msg)
        await ctx.message.delete()
    
    @say.error
    async def say_error(self, ctx, error):
        await ctx.send("You forgot to give me input to repeat!")
    
    @commands.command(
        name = "reply",
        hidden = True
        )
    async def reply(self, ctx):
        await ctx.message.add_reaction("✅")
        msg = await ctx.reply("I replied! (but didn't mention\nThis command is just for testing (◍•ᴗ•◍)")
        await msg.add_reaction("😊")
    
    
def setup(bot):
    bot.add_cog(Fun(bot)