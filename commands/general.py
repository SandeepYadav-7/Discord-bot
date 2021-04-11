import discord
from discord.ext import commands
import requests
import json

def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]["q"] + "\n-" + json_data[0]["a"]
	return(quote)


class General(commands.cog):
	def __init__(self, bot):
		self.bot = bot
	
	
	@commands.command(name = "inspire", aliases = ["quote"])
	async def inspire(self, ctx):
		await ctx.send(get_quote())
	
	@commands.command(name = "ping", aliases = ['pong', "latency"])
	async def ping(self, ctx):
		message = await ctx.send(f"🏓 hey {ctx.author.mention}, pong! Latency is ")
		await message.edit(content = f"🏓 hey {ctx.author.mention}, pong! Latency is {round(self.bot.latency * 1000)}ms")
	
	@commands.command(name = "youtube", aliases = ["yt"])
	async def youtube(self, ctx, *, search):
		query_string = parse.urlencode({"search_query": search})
		html_content = requests.urlopen("http://www.youtube.com/results?" + query_string)
		search_content = html_content.read().decode()
		search_results = re.findall(r"\/watch\?v=\w+", search_content)
		await ctx.send("https://www.youtube.com" + search_results[0])
	
	@youtube.error
	async def youtube(self, ctx, error):
		await ctx.send(error)
	
	@commands.command(name = "avatar", aliases = ["a"])
	async def avatar(ctx, member: discord.Member = None):
		if not member:
			member = ctx.message.author
		em = discord.Embed(color = discord.Color.random(), timestamp = ctx.message.created_at)
		em.set_author(name = f"Avatar of {member}")
		em.set_image(url = member.avatar_url)
		em.set_footer(text = f"requested by {ctx.message.author}", icon_url = ctx.author.avatar_url)
		
		await ctx.send(embed = em)
	


def setup(bot):
	bot.add_cog(General(bot))