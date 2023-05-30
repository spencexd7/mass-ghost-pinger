# project info

# author : https://github.com/spencexd7
# discord : https://discord.gg/gpqMWg5PAY


import discord
from discord.ext import commands
import random
import os
import asyncio
import aiohttp

os.system("clear")
print("""
        
███╗░░░███╗░█████╗░░██████╗░██████╗  ░██████╗░██╗░░██╗░█████╗░░██████╗████████╗
████╗░████║██╔══██╗██╔════╝██╔════╝  ██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝
██╔████╔██║███████║╚█████╗░╚█████╗░  ██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░
██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗  ██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░
██║░╚═╝░██║██║░░██║██████╔╝██████╔╝  ╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░

██████╗░██╗███╗░░██╗░██████╗░███████╗██████╗░
██╔══██╗██║████╗░██║██╔════╝░██╔════╝██╔══██╗
██████╔╝██║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
██╔═══╝░██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
██║░░░░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝ - made by spencexd7
""")
tk = str(input("enter your token : "))
gl = int(input("enter the guild id : "))
ch = int(input("enter the channel id : "))

max=2000

client = commands.Bot(command_prefix='spencexd7',intents=discord.Intents.all())

client._skip_check = lambda x, y: False

async def send(ids, session, channel):
  
    chunks = [ids[i:i+max] for i in range(0, len(ids), max)]
    for chunk in chunks:
        mems = [f"<@{id}>" for id in chunk]
        format = " ||-|| ".join(mems)
        msg = f"||{format}||"
        async with session.post(f"https://discord.com/api/v9/channels/{channel.id}/messages", json={"content": msg}) as response:
            if response.status == 200:
                message = await response.json()
                dll = await channel.fetch_message(int(message['id']))
                await dll.delete()

    if len(ids) % max != 0:
        left = ids[-(len(ids) % max):]
        membs = [f"<@{id}>" for id in left]
        formats = " ||-|| ".join(membs)
        message = f"||{formats}||"
        async with session.post(f"https://discord.com/api/v9/channels/{channel.id}/messages", json={"content": message}) as response:
            if response.status == 200:
                message = await response.json()
                dl = await channel.fetch_message(int(message['id']))
                await dl.delete()
                tm = random.choice(['who tf pinged', 'burh pinged', 'pong', 'wtf', 'stop bro'])
                await channel.send(tm)


headers = {'Authorization': f'{tk}'}

@client.event
async def on_ready():
  async with aiohttp.ClientSession(headers=headers, connector=None) as ss:
    guild = client.get_guild(gl)
    members = guild.members
    with open("members.txt", "w") as f:
        for member in members:
            f.write(str(member.id) + "\n")
            print(member.id)
    with open("members.txt", "r") as f:
        mids = f.read().splitlines()

        channel = client.get_channel(int(ch))
        print("starting...........")
        while True:
            await send(mids, ss, channel)
    
  
client.run(tk)
