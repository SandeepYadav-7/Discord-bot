import discord
from discord.ext import commands

class Maths(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	
	@commands.command(name = "add", aliases = ["sum", "addition"])
	async def add(self, ctx, numOne: int, numTwo: int):
		await ctx.send(f"{numOne} + {numTwo} = {numOne + numTwo}")
	
	@add.error
	async def add_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("🚫 Please give me some parameters !")
		else:
			await ctx.send("🚫 please give me integer values !")
	
	@commands.command(name = "sub", aliases = ["minus"])
	async def sub(self, ctx, numOne: int, numTwo: int):
		await ctx.send(f"{numOne} - {numTwo} = {numOne - numTwo}")
	
	@sub.error
	async def sub_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("🚫 Please give me some parameters !")
		else:
			await ctx.send("🚫 please give me integer values !")
	
	@commands.command(name = "divide", aliases = ["division"])
	async def divide(self, ctx, numOne: int, numTwo: int):
		await ctx.send(f"{numOne} / {numTwo} = {numOne / numTwo}")
	
	@divide.error
	async def divide_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("🚫 Please give me some parameters !")
		else:
			await ctx.send("🚫 please give me integer values !")
	
	@commands.command(name = "multiply", aliases = ["mult", "multiplication"])
	async def multiply(self, ctx, numOne: int, numTwo: int):
		await ctx.send(f"{numOne} * {numTwo} = {numOne * numTwo}")
	
	@multiply.error
	async def multiply_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("🚫 Please give me some parameters !")
		else:
			await ctx.send("🚫 please give me integer values !")


def setup(bot):
	bot.add_cog(Maths(bot))