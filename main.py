import discord
import viking_secrets
from discord.ext import commands
from commands import bot_commands
from listener import bot_listener

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot_commands.setup_commands(bot)
bot_listener.setup_listener(bot)

bot.run(viking_secrets.BOT_TOKEN)