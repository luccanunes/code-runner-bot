import discord
import asyncio
from os import getenv
import pathlib
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv('TOKEN')

client = discord.Client()

commands = list()

for path in pathlib.Path("./commands").iterdir():
    if path.is_file() and path.name != 'Command.py':
        cmd = getattr(__import__(
            f'commands.{path.name[:-3]}',
            fromlist=[f'commands.{path.name[:-3]}']
        ), str(path.name[:-3]))
        commands.append(cmd())


@client.event
async def on_ready():
    print('hello, programmers')


@client.event
async def on_message(message: discord.Message):
    global prefix
    log = open(r'./log.txt', 'r+')
    found_prefix = False
    for line in log.readlines():
        if str(message.guild.id) in line:
            prefix = line.split(' ')[1].replace('\n', '')
            found_prefix = True
    if not found_prefix:
        prefix = '>'

    global commands
    msg: str = message.content.strip().lower()
    invoked_cmd = msg.split(' ')[0][1:]

    for command in commands:
        if command.name == invoked_cmd or invoked_cmd in command.aliases:
            await command.run(message)


client.run(TOKEN)
