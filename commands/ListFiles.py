from commands.Command import Command
import discord
import asyncio


class ListFiles(Command):
    def __init__(self):
        super().__init__(
            {
                'name': 'listfiles',
                'aliases': ['ls', 'dir'],
                'description': 'list all files in this server',
                'argc': 0
            }
        )

    async def run(self, message: discord.Message, argc: int, argv: list):
        from pathlib import Path
        from helpers.getUserFiles import getUserFiles

        emb = discord.Embed(
            title='List files',
            description='Here are all your files'
        )
        for file in getUserFiles(str(message.author)):
            emb.add_field(name=file['suffix'], value='** **')
        await message.channel.send(embed=emb)
