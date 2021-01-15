import discord
from discord.ext import commands
import random
import asyncio
from PIL import Image
import os, time

# get PATH
cwd = os.getcwd()

# Bot settings
client = commands.Bot(command_prefix = '.')

# Here goes your token
myToken = 'yourToken'

@client.event
async def on_ready():
	print('Funciono :D')

@client.command()
async def chago(ctx):

	# list of images
	contenido = os.listdir(cwd + '\\imagenes')

	# Random number
	aleatorio = random.randint(1,len(contenido))

	# get the image name
	imageName = contenido[aleatorio - 1]
	imagesDir = cwd + '\\imagenes\\' + imageName
	imagen = Image.open(imagesDir)

	# Save the image
	imagen.save(imageName)

	# Display the image
	await ctx.send(file = discord.File(imageName))

	# Delete image
	time.sleep(1)
	os.remove(contenido[aleatorio - 1])

# Close the bot
@client.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def close(ctx):
    await client.close()
    print("Bot Closed")  # This is optional, but it is there to tell you.

client.run(myToken)
