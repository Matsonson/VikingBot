import discord
from discord.ext import tasks

def setup_listener(bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        check_activity.start()

    @bot.event
    async def on_presence_update(before, after):
        if after.activity and after.activity.name == 'Valheim':
            print(f'{after.name} is now playing Valheim')
            # Logic to log game time and award Viking coins
            log_game_time(after)

    @tasks.loop(minutes=1)
    async def check_activity():
        # Logic to check channel activities and log game time
        pass

def log_game_time(user):
    # Logic to log the game time for the user
    pass
