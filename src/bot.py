# altminder https://github.com/bitfl0wer/altminder
# Published under the GNU AGPL-3.0 License
# A project that aims to make Discord a tiny bit more accessible for vision impaired users.

from os import environ
from sys import flags
from dotenv import load_dotenv
import discord
import random
import asyncio

load_dotenv()

if "TOKEN" not in environ:
    raise RuntimeError("TOKEN environment variable not set, exiting.")

__token__ = environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

image_types = [
    "image/png",
    "image/jpeg",
    "image/aviv",
    "image/webp",
    "image/svg+xml"
]

reminder_texts = [
    "Good day! You just posted an image without a description. This makes it impossible for blind or low vision users to understand its content.",
    "Hello! This is a reminder that you just posted an image without a description. This makes it impossible for blind or low vision users to fully participate on Discord.",
    "Hey! The image you have just posted does not have a description. This excludes blind or low vision users from fully participating in this community.",
    "Hi! It looks like you forgot to include a description with your image. This makes participation easier and more pleasant for blind or low vision users.",
    "Hey! To make it easier for blind or low vision users to participate on Discord, please include a description with your image. You seem to have forgotten to do this."
]

tutorial_string = "Please, if possible, re-post your image with an alt-text. To do this, open the image properties when you have added it to the message, and fill a text box labelled 'Description (Alt Text)'."


@bot.event
async def on_ready():
    """Gets executed once the bot is logged in.
    """
    await bot.change_presence(activity=discord.Game('Reminding about ALT Texts!'))


@bot.event
async def on_message(message):
    """Gets executed when a message is sent in the server.
    """
    if message.author == bot.user or message.author.bot:
        return

    attachments = message.attachments
    for attachment in attachments:
        if attachment.content_type in image_types:
            # Check if the image has a description.
            if not attachment.description:
                # Send a single random reminder message.
                message = await message.reply(reminder_texts[random.randint(0, len(reminder_texts) - 1)])
                await asyncio.sleep(30)
                await message.delete()
                break
# Load all the cogs
# Connect the bot to the discord api
bot.run(__token__)
