import discord
from discord.ext import commands
from discord import app_commands
from imports import *

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

        if message.content.startswith('!ro hello'):
            await message.channel.send(f":zap:**BZZT**:zap: Hello, **{message.author}**! I am Rotom, your personal Pokédex!")

        if message.content.startswith('!ro pokedex'):
            await message.channel.send("filler for later")

        if message.content.startswith('!ro bulbasaur'):
            await message.channel.send("Bulbasaur, the Grass/Poison type pokémon.")
            await message.channel.send("Pokédex entry NO.001")
            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("The bulb on its back acts as a built-in energy source, allowing it to go long periods without food!")

            if num == 2:
                await message.channel.send("The bulb on its back is known to have been there since birth, growing alongside it!")

            if num == 3:
                await message.channel.send("To keep its bulb full of energy, bulbasaur tend to sleep in sunny spaces!")

        if message.content.startswith('!ro ivysaur'):
            await message.channel.send("Ivysaur, the Grass/Poison type Pokémon.")
            await message.channel.send("Pokédex entry NO.002")
            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("The weight of an Ivysaur's bulb prevents it from running fast or standing on its hind legs,")
                await message.channel.send("forcing its legs to grow sturdy.")

            if num == 2:
                await message.channel.send("Ivysaur tend to spend more time in sunlight, preparing for their upcoming evolution!")

            if num == 3:
                await message.channel.send("When an Ivysaur's flower is ready to bloom, it will give off a sweet-smelling scent and will start to swell.")

        if message.content.startswith('!ro venusaur'):
            await message.channel.send("Venusaur, the Grass/Poison type pokémon.")
            await message.channel.send("Pokédex entry NO.003")
            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("The scent that emanates from a Venusaur's bulb can attract pokémon and calm emotions!")
                await message.channel.send("This scent becomes stronger after a rainy day!")

            if num == 2:
                await message.channel.send("Venusaur tend be stronger during the summertime, as there is more sunlight for them to absorb during that time.")

            if num == 3:
                await message.channel.send("Venusaur can shoot out huge amounts of pollen from their bulbs.")
                await message.channel.send("Breathing in too much can cause you to faint, so be careful!")

        if message.content.startswith('!ro charmander'):
            await message.channel.send("Charmander, the Fire type pokémon.")
            await message.channel.send("Pokédex entry NO.004")
            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Charmander and the flame on their tail are interconnected,")
                await message.channel.send("reflecting its life force to how bright the flame burns!")

            if num == 2:
                await message.channel.send("As they sleep, Charmander supposedly draw heat from their tails for warmth!")

            if num == 3:
                await message.channel.send("Charmander like to behave in packs, finding food and making sure each other's tails stay lit!")

        if message.content.startswith('!ro charmeleon'):
            await message.channel.send("Charmeleon, the Fire type Pokémon!")
            await message.channel.send("Pokédex entry NO.005")
            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Charmeleon are hotheaded by nature, constantly looking for opponents to fight.")
                await message.channel.send("Exceptionally strong pokemon excites them, even causing them to spout bluish-white flames!")

            if num == 2:
                await message.channel.send("Although they are known to be aggressive, they tend to relax after they win a battle.")

            if num == 3:
                await message.channel.send("A Charmeleon will use the fire on its tail to raise the temperature around it, tormenting the opponent with a hot atmosphere!")

        if message.content.startswith('!ro charizard'): #Charizard
            #Charizard Dex Entry
            await message.channel.send("Charizard, the Fire/Flying type Pokemon")
            await message.channel.send("Dex entry NO.006")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Charizard tend to live in mountains and even inhabit volcanoes with others of its species!")

            if num == 2:
                await message.channel.send("Charizard fly around in search of strong opponents, with its fire on its tail burning brighter with gained experience!")
                await message.channel.send("They will never fight anything weaker than themselves.")

            if num == 3:
                await message.channel.send("A Charizard's fiery breath can melt boulders and huge glaciers.")
                await message.channel.send("It's also been known to accidentally start forrest fires!")





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

client.run('')

