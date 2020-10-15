from commands.Command import Command
import discord
import asyncio


class ListFiles(Command):
    def __init__(self):
        super().__init__(
            {
                'name': 'listfiles',
                'aliases': ['ls'],
                'description': 'list all files in this server'
            }
        )

    async def run(self, message: discord.Message):
        await message.channel.send('listing all files')
