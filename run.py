import discord
import random
import os


game_on = False
p1_on = False
p2_on = False
p1_name = ''
p2_name = ''
score = 0
turn = 1
win_limit = 0
moves_options = 0

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    global game_on
    global p1_on
    global p2_on
    global p1_name
    global p2_name
    global score
    global turn
    global win_limit
    global moves_options

    if message.author == client.user:
        return

    # await message.channel.send(message.author)

    if message.content == '$exit':

    	if game_on == True:

    		await message.channel.send(':catok:')
    		game_on = False
    		p1_on = False
    		p2_on = False
    		turn = 0

    	else:
    		await message.channel.send('are kehna kya chahte ho')


    if message.content == '$game':

        if game_on == True:
            await message.channel.send('a game is already on, calm down!')

        else:
            await message.channel.send('player 1 send $me')
            p1_on = True


    if(message.content == '$me'):
        if game_on == True:
            await message.channel.send('a game is already on, calm down!')

        else:
            if p1_on == True:
                p1_name = str(message.author)
                p1_name = p1_name[:-5]
                p1_on = False
                p2_on = True
                await message.channel.send('player 1 is ' + p1_name)
                await message.channel.send('player 2 send $me')
            else:
                p2_name = str(message.author)
                p2_name = p2_name[:-5]
                p2_on = False
                game_on = True
                turn = 1
                await message.channel.send('player 2 is ' + p2_name)

                win_limit = random.randint(10, 35)
                moves_options = random.randint(2, int(win_limit / 2))
                await message.channel.send('turn of ' + p1_name + '; send your choice in format +x where x is from 1 to ' + str(moves_options))
                await message.channel.send('your target is to hit ' + str(win_limit ))


    if message.content.startswith('+') and game_on == True:
        increase = int(str(message.content[1:]))

        if turn == 1:

            cur_player = str(message.author)
            cur_player = cur_player[:-5]

            score += increase
            turn = 2

            if cur_player != p1_name:
                await message.channel.send('teri turn nahi hai lodu')
                score -= increase
                turn = 1

            elif increase > moves_options or increase < 1:
                await message.channel.send('cheater :(')
                score -= increase
                turn = 1

            else:
                await message.channel.send('score: ' + str(score) + ', target: ' + str(win_limit))


            if score == win_limit:
                game_on = False
                score = 0
                await message.channel.send('congratulations!! ' + p1_name)
                await message.channel.send('big brain ' + p2_name)
        
        else:

            cur_player = str(message.author)
            cur_player = cur_player[:-5]

            score += increase
            turn = 1

            if cur_player != p2_name:
                await message.channel.send('teri turn nahi hai lodu')
                score -= increase
                turn = 2

            elif increase > moves_options or increase < 1:
                await message.channel.send('cheater :(')
                score -= increase
                turn = 2

            else:
                await message.channel.send('score: ' + str(score) + ', target: ' + str(win_limit))


            if score == win_limit:
                game_on = False
                score = 0
                await message.channel.send('congratulations!! ' + p2_name)
                await message.channel.send('what a dum-dum ' + p1_name)


tokenfile = open('token.txt', 'r')
tokenstring = tokenfile.read()

client.run(tokenstring)