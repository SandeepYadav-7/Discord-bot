import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{'=' * 38}")
        print(f"{self.__class__.__name__} Cog has been loaded...")
        print(f"{'=' * 38}")
        print(f"We have logged in as {self.bot.user}")
        print(f"{'=' * 38}")
        print(f"Discord version: {discord.__version__}")
        print(f"{'=' * 38}")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("🚫 command not found !")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Looks like you don't have permission to use this command.")
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.TextChannels:
            if channel.has_permissions(guild.me).send_messages:
                await channel.send(f"Hi I am **{self.bot.user.name.upper()}**, Thanks for inviting me into this server! My prefix is: _**K.**_")
                break
    
    
    
    
    
    
    
def setup(bot):
    bot.add_cog(Events(bot)