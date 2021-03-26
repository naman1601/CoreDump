import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'nadaan' in message.content and 'baalak' in message.content:
        await message.channel.send('bhosadike!')

client.run("token")