from commands.Command import Command
import discord
import asyncio


class CreateFile(Command):
    def __init__(self):
        super().__init__(
            {
                'name': 'createfile',
                'aliases': ['cf', 'touch'],
                'description': 'creates a new file',
                'argc': 1
            }
        )

    async def run(self, message: discord.Message, argc: int, argv: list):
        valid_extensions = ['cpp']
        extension = argv[0]
        if extension not in valid_extensions:
            emb = discord.Embed(
                title='Error', description="Invalid file extension.", colour=discord.Color.from_rgb(255, 0, 0)
            )
            await message.channel.send(embed=emb)
            return

        emb = discord.Embed(
            title='Create File', description="File created sucessfully!"
        )
        await message.channel.send(embed=emb)
        file = open(f'./files/{message.author}.{extension}', 'w')
        file.writelines([
            '#include <bits/stdc++.h>\n\n',
            'using namespace std;\n\n',
            'int main()\n',
            '{\n',
            '   cout << "Hello, Code Runner!" << endl;\n\n'
            '   return 0;\n',
            '}\n'
        ])
        file.close()
