"""
    IMPORTS:

    discord, discord.ext
        Used for: Literally everything discord-api related.

    logger.ownlogger: log
        Used for: logging, duh.

    helper_functions
        Used for: please see helper_functions.py docstrings for an explanation.
    """
from os import environ
from dotenv import load_dotenv
import discord


load_dotenv()

if "TOKEN" not in environ:
    raise RuntimeError("TOKEN environment variable not set, exiting.")

__token__ = environ.get("TOKEN")

bot = discord.Bot()


@bot.event
async def on_ready():
    """Gets executed once the bot is logged in.
    """
    await bot.change_presence(activity=discord.Game('Reminding about ALT Texts!'))


# Load all the cogs
bot.load_extension("")
# Connect the bot to the discord api
bot.run(__token__)
