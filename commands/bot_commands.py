from discord.ext import commands

def setup_commands(bot):
    @bot.command(name='ping')
    async def ping(ctx):
        await ctx.send('pong')

    @bot.command(name='coins')
    async def coins(ctx):
        # Logic to check and return the user's Viking coins
        await ctx.send(f'{ctx.author.name}, you have X Viking coins.')