from commands.Command import Command
import discord
import asyncio


class CreateFile(Command):
    def __init__(self):
        super().__init__(
            {
                'name': 'createfile',
                'aliases': ['cf'],
                'description': 'creates a new file'
            }
        )

    async def run(self, message: discord.Message):
        await message.channel.send('creating file')
