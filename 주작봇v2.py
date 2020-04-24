import random

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("주작할준비")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("=주작"):
        team = message.content[4:]
        peopleteam = team.split(" / ")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        embed = discord.Embed(title="주작을 완료했다옹..!!", description="", color=0x62c1cc)
        for i in range(0, len(person)):
            embed.add_field(name=person[i], value=teamname[i], inline=True)
        embed.set_footer(text="1번부터 빠르게 보상을 골라야 한다냥....!!")
        await message.channel.send(embed=embed)




client.run("Njk4OTQ5MzI0NDAyNDU4NjI1.XpNRVA.mAx_8HCQNjJhRlnKiNy108vlj0o")