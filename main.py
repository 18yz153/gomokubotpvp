import discord
import os
import game
import asyncio

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(m):
    if m.author == client.user:
        return
    if m.content.startswith('-p'):
        p1 = m.author
        player2l = m.mentions
        if len(player2l) == 1:
            p2 = player2l[0]
            await m.channel.send(p1.name + ' play with ' + p2.name)

            def isp1(mess):
                return mess.author == p1

            def isp2(mess):
                return mess.author == p2

            g = game.game()
            await m.channel.send(g)
            turn = 1
            while (g.iscontiune()):
                print('round')
                if turn == 1:
                    try:
                        pos = await client.wait_for('m', check=isp1, timeout=5)
                    except asyncio.TimeoutError:
                        return await m.channel.send('timeout')
                    g.addchess('●', pos)
                    turn = 0
                else:
                    try:
                        pos = await client.wait_for('m', check=isp2, timeout=5)
                    except asyncio.TimeoutError:
                        return await m.channel.send('timeout')
                    g.addchess('○', pos)
                    turn = 1
                await m.channel.send(g)


client.run(TOKEN)
