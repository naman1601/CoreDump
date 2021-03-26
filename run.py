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

    if message.content.endswith('nga'):
    	await message.channel.send(message.content[:-3] + 'nge')

    if(message.content.endswith('karla')):
    	await message.channel.send(message.content[:-1] + 'e')

tokenfile = open('token.txt', 'r')
tokenstring = tokenfile.read()

client.run(tokenstring)