  
import discord
import os
import game
import asyncio

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def embedg(g,player):
  embedVar = discord.Embed(title="The game",description=str(g), color=0x66ccff)
  embedVar.add_field(name="Next turn", value=player.name, inline=False)
  return embedVar

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
                return mess.author == p1 and ',' in mess.content

            def isp2(mess):
                return mess.author == p2 and ',' in mess.content

            g = game.game()
            embedver=embedg(g,p1)
            await m.channel.send(embed=embedver)
            turn = 1
            while (g.iscontiune()):
                print('round')
                if turn == 1:
                    try:
                        posmsg = await client.wait_for('message', check=isp1)
                    except asyncio.TimeoutError:
                        return await m.channel.send(p1.name +' timeout')
                    pos=posmsg.content.split(',')
                    try:
                        g.addchess('● ', pos)
                        turn = 0
                        embedver=embedg(g,p1)
                        await m.channel.send(embed=embedver)
                    except:
                        turn = 1
                        await m.channel.send(p1.name +' put koma failed')
                else:
                    try:
                        posmsg = await client.wait_for('message', check=isp2)
                    except asyncio.TimeoutError:
                        return await m.channel.send(p2.name +' timeout')
                    pos=posmsg.content.split(',')
                    try:
                        g.addchess('○ ', pos)
                        turn = 1
                        embedver=embedg(g,p2)
                        await m.channel.send(embed=embedver)
                    except:
                        turn = 0
                        await m.channel.send(p2.name +' put koma failed')
            await m.channel.send('game ended')
        else:
            await m.channel.send('Use -p @user to play the game.')
    if m.content.startswith('-invitelink'):
        await m.channel.send('https://discord.com/api/oauth2/authorize?client_id=831894161434083358&permissions=2148005952&scope=bot')




client.run(TOKEN)
