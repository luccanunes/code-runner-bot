from commands.Command import Command
import discord
import asyncio


class Edit(Command):
    def __init__(self):
        super().__init__(
            {
                'name': 'edit',
                'description': 'edits the specified file',
                'argc': -1,
                'aliases': ['e']
            }
        )

    async def run(self, message: discord.Message, argc: int, argv: list):
        if argc <= 1:
            emb = discord.Embed(
                title='Error', description="Too few arguments.", colour=discord.Color.from_rgb(255, 0, 0)
            )
            await message.channel.send(embed=emb)
            return
        extension = argv[0]
        valid_extensions = ['cpp']
        if extension not in valid_extensions:
            emb = discord.Embed(
                title='Error', description="Invalid file extension.", colour=discord.Color.from_rgb(255, 0, 0)
            )
            await message.channel.send(embed=emb)
            return

        file = open(f'./files/{message.author}.{extension}', 'w')
        lines = message.content.replace('`', '').split('\n')[1:]
        for i in range(1, len(lines)):
            file.write(lines[i] + '\n')
        file.close()

        await message.channel.send(embed=discord.Embed(title='Edit', description='Sucessfully edited file!'))
