import discord
from discord.ext import commands

class Modarator(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name = "clear", aliases = ["nuke", "delete"])
	@commands.has permissions(administrator = True)
	async def clear(self, ctx, amount: int):
		await ctx.channel.purge(limit = amount + 1)
		await ctx.send(f"{amount} message(s) deleted.", delete_after = 5)
	
	@clear.error
	async def clear_error(self, ctx, error):
		await ctx.send(error)
	
	@commands.command(name = "dm", hidden = True)
	@commands.is_owner()
	async def dm(self, ctx, member: discord.Member, *, msg):
		if msg != None:
			try:
				await member.send(msg)
				await ctx.message.delete()
				await ctx.send(f"✅ Successfully sent message to **{member.name}**", delete_after = 5)
			except:
				await ctx.send(f'**{member.name}** has closed his/her DM.')
		else:
			await ctx.send("please give a valid username or msg")
	
	@dm.error
	async def dm_error(self, ctx, error):
		await ctx.send(error)


def setup(bot):
	bot.add_cog(Modarator(bot))