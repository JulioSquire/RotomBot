import discord
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')


        try:
            guild = discord.Object(id=860069193402548224)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}!')

        except Exception as e:
            print(f'Error sycning commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send(f":zap:**BZZT**:zap: Hello! **{message.author}**! I am Rotom, your interactive pokemon index!")

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('Thank you for the reaction!')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix='!ro', intents=intents)


GUILD_ID = discord.Object(id=860069193402548224)

@client.tree.command(name='hi', description='Makes Rotom say Hello!', guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello there! How are you?')

@client.tree.command(name='printer', description='Makes Rotom say what you said!', guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

client.run('MTMxMjU1NzMzMzMzOTE4MTEyNg.GlooGo.LlEaUeW18bMGA0n5CvE72tKubo-3SZpLmIAAQY')

