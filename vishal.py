import discord
import os


game_on = False
p1_on = False
p2_on = False
p1_name = "A"
p2_name = "B"

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # await message.channel.send(message.author)

    if 'nadaan' in message.content and 'baalak' in message.content:
        await message.channel.send('bhosadike!')

    if message.content.endswith('nga'):
        text = str(message.author)
        text = text[:-5]
        text += ' hindi seekh le chutiye'
        await message.channel.send(text)
        await message.channel.send(message.content[:-3] + 'nge')

    if(message.content.endswith('karla')):
        text = str(message.author)
        text = text[:-5]
        text += ' hindi seekh le chutiye'
        await message.channel.send(text)
        await message.channel.send(message.content[:-1] + 'e')

    if(message.content == '$game'):
        global p1_on
        await message.channel.send('player 1 send $me')
        p1_on = True

    if(message.content == '$me'):
        global game_on
        # global p1_on
        global p2_on
        global p1_name
        global p2_name
        if p1_on:
            p1_name = str(message.author)
            p1_name = p1_name[:-5]
            p1_on = False
            p2_on = True
            await message.channel.send('player 1 is ' + p1_name)
        else:
            p2_name = str(message.author)
            p2_name = p2_name[:-5]
            p2_on = False
            await message.channel.send('player 2 is ' + p2_name)

tokenfile = open('token.txt', 'r')
tokenstring = tokenfile.read()

client.run(tokenstring)