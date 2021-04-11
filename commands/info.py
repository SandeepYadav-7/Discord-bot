import discord
from discord.ext import commands
import datetime

class Information(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name = "serverinfo", aliases = ["guildinfo"])
	async def serverinfo(self, ctx):
		embed = discord.Embed(title = f"{ctx.guild.name}", description = "Serverinfo", timestamp = datetime.datetime.utcnow(), color = discord.Color.random())
		embed.add_field(name = "Server created at", value = f"{ctx.guild.created_at}")
		embed.add_field(name = "Server owner", value = f"{ctx.guild.owner}")
		embed.add_field(name = "Server Region", value = f"{ctx.guild.region}")
		embed.add_field(name = "Server ID", value = f"{ctx.guild.id}")
		embed.set_thumbnail(url = f"{ctx.guild.icon_url}")
		
		await ctx.send(embed = embed)
	
	@commands.command(name = "invite")
	async def invite(self, ctx):
		await ctx.send("https://discord.com/api/oauth2/authorize?client_id=824712689582342174&permissions=8&scope=bot")
		
	@commands.command(name = "support_server", aliases = ["support"])
	async def support_server(self, ctx):
		await ctx.send("https://discord.gg/vTv8uGwvcG")
	
	@commands.command(name = "userinfo", aliases = ["user", "whois"])
	async def userinfo(self, ctx, user: discord.Member = None):
		if not user:
			user = ctx.message.author
		avatar = user.avatar_url
		em = discord.Embed(title = "Userinfo", description = " ", color = discord.Color.random())
		em.set_thumbnail(url = avatar)
		em.add_field(name = "Name", value = f"This user name is {user.name}", inline = True)
		em.add_field(name = "ID", value = f"The user ID is {user.id}", inline = True)
		em.add_field(name = "Status", value = f"The user status is: {user.status}", inline = False)
		em.add_field(name = "Highest Role", value = f"The users highest role is: {user.top_role}", inline = True)
		em.add_field(name = "Joined", value = f"The user joined at: {user.joined_at}", inline = True)
		
		await ctx.send(embed = em)
	
	



def setup(bot)
	bot.add_cog(Information(bot))