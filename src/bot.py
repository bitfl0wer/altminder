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
