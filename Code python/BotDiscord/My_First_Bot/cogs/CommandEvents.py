from discord.ext import commands

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    commands_tally = {}

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + " was invoked incorrectly.")
        print(error)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command.name in commands_tally:
            commands_tally[ctx.command.name] += 1
        else:
            commands_tally[ctx.command.name] = 1
        print(commands_tally)

def setup(bot):
    bot.add_cog(CommandEvents(bot))
    print("CommandEvents loaded")