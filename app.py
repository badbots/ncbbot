import discord
import yaml
import random
import os

with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

TOKEN = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('🍄') or message.content.startswith('🍆'):
        nice = random.choice(config['nice'])
        cock = random.choice(config['cock'])
        bro = random.choice(config['bro'])
        msg = nice + ' ' + cock + ' ' + bro
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)