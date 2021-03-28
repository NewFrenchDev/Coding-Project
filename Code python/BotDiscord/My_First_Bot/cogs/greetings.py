from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', aliases=['h', 'he', 'hi'])
    async def hello_command(self, ctx):
        await ctx.channel.send("Hello")
        print('Hello')
        

def setup(bot):
    bot.add_cog(Greetings(bot))
    print("Greetings loaded")