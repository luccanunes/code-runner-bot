from commands.Command import Command
import discord
import asyncio


class Cat(Command):
    def __init__(self):
        super().__init__(
            {
                'name': 'cat',
                'description': 'extracts the text content of your file',
                'argc': 1
            }
        )

    async def run(self, message: discord.Message, argc: int, argv: list):
        extension = argv[0]
        valid_extensions = ['cpp']
        if extension not in valid_extensions:
            emb = discord.Embed(
                title='Error', description="Invalid file extension.", colour=discord.Color.from_rgb(255, 0, 0)
            )
            await message.channel.send(embed=emb)
            return

        file = open(f'./files/{message.author}.{extension}', 'r')
        msg = '```cpp\n'
        for line in file.readlines():
            if len(line.strip()) != 0:
                msg += line
            else:
                msg += '\n'
        msg += '\n```'
        file.close()
        await message.channel.send(msg)
