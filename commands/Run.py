from commands.Command import Command
import discord
import asyncio


class Run(Command):
    def __init__(self):
        super().__init__(
            {
                'name': 'run',
                'aliases': ['r'],
                'description': 'compiles and runs the chosen program',
                'argc': 1
            }
        )

    async def run(self, message: discord.Message, argc: int, argv: list):
        import subprocess
        from helpers.getUserFiles import getUserFiles

        invokedFile = {}
        for file in getUserFiles(str(message.author)):
            if file['suffix'] == '.' + argv[0]:
                invokedFile['stem'] = file['stem']
                invokedFile['suffix'] = file['suffix']
        if invokedFile == {}:
            emb = discord.Embed(
                title='Error', description="No such file.", colour=discord.Color.from_rgb(255, 0, 0)
            )
            await message.channel.send(embed=emb)
            return

        compilation = subprocess.run([
            "g++",
            f"./files/{invokedFile['stem']}{invokedFile['suffix']}",
            '-o', f"./files/{invokedFile['stem']}"
        ], capture_output=True, text=True)

        if compilation.stderr != '':
            emb = discord.Embed(
                title='Error', description=compilation.stderr, colour=discord.Color.from_rgb(255, 0, 0)
            )
            await message.channel.send(embed=emb)
            return

        proc = subprocess.run(
            [f"./files/{invokedFile['stem']}"], capture_output=True, text=True
        )

        emb = discord.Embed(
            title=f'Output - {argv[0]}', description=proc.stdout.strip()
        )
        await message.channel.send(embed=emb)
