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

timeout = 30

image_types = ["image/png", "image/jpeg", "image/aviv", "image/webp", "image/svg+xml"]

reminder_texts = [
    "Good day! You just posted an image without a description. This makes it impossible for blind or low vision users to understand its content.",
    "Hello! This is a reminder that you just posted an image without a description. This makes it impossible for blind or low vision users to fully participate on Discord.",
    "Hey! The image you have just posted does not have a description. This excludes blind or low vision users from fully participating in this community.",
    "Hi! It looks like you forgot to include a description with your image. This makes participation easier and more pleasant for blind or low vision users.",
    "Hey! To make it easier for blind or low vision users to participate on Discord, please include a description with your image. You seem to have forgotten to do this.",
]

tutorial_string = "Please, if possible, re-post your image with an alt-text. To do this, open the image properties when you have added it to the message, and fill a text box labelled 'Description (Alt Text)'. A tutorial can be found here: https://support.discord.com/hc/en-us/articles/211866427-How-do-I-upload-images-and-GIFs-."


@bot.event
async def on_ready():
    """Gets executed once the bot is logged in."""
    print("Online.")
    # Set a bot "Playing [...]" status message.
    await bot.change_presence(activity=discord.Game("Reminding about ALT Texts!"))


@bot.event
async def on_message(message):
    """Gets executed when a message is sent in the server."""
    # Don't react to self or other bots to avoid a) recursion b) talking to a wall
    if message.author == bot.user or message.author.bot:
        return

    for attachment in message.attachments:
        if attachment.content_type in image_types:
            # Check if the image has a description.
            if not attachment.description:
                # Create and send a single, random reminder message
                # Pick a random reminder message and combine it with the tutorial_string
                message_reminder = (
                    reminder_texts[random.randint(0, len(reminder_texts) - 1)]
                    + " "
                    + tutorial_string
                )
                # Generate the message self-destruction notice so that users don't get confused.
                message_selfdestruct = (
                    " This message will delete itself in " + str(timeout) + "s."
                )
                # Finally, put the two messages together and send it as a reply to the image without alt-text
                message = await message.reply(message_reminder + message_selfdestruct)
                # Wait for $timeout seconds, then delete the message.
                await asyncio.sleep(timeout)
                await message.delete()
                break


# Connect the bot to the discord api
bot.run(__token__)
