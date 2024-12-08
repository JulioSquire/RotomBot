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

        if message.content.startswith('!ro pokemon'):
            await message.channel.send("Pokémon are mysterious creatures. They reside in every corner of our world. From the skies, to the forrest, and even the mountains. Humans and Pokémon share a mutualistic relationship, coexisting and helping one another to live and thrive!")
            await message.channel.send("In short, Pokémon are our companions!")

        if message.content.startswith('!ro entries'):
            await message.channel.send("Currently, I have dex entries for these Pokémon:")
            await message.channel.send("Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Chikorita, Bayleef, Meganium, Cyndaquil, Quilava, Typhlosion, Totodile, Croconaw, Feraligatr.")
            await message.channel.send("To ask for an entry for a Pokémon, say '!ro' along with the name of the pokémon in all lowercase letters!")
            await message.channel.send("For example, you could say **'!ro bulbasaur'** !")


        #Gen 1 Starters
        if message.content.startswith('!ro bulbasaur'):
            await message.channel.send("Bulbasaur, the Grass/Poison type Pokémon.")
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
            await message.channel.send("Venusaur, the Grass/Poison type Pokémon.")
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
            await message.channel.send("Charmander, the Fire type Pokémon.")
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
            await message.channel.send("Charmeleon, the Fire type Pokémon.")
            await message.channel.send("Pokédex entry NO.005")
            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Charmeleon are hotheaded by nature, constantly looking for opponents to fight.")
                await message.channel.send("Exceptionally strong pokemon excites them, even causing them to spout bluish-white flames!")

            if num == 2:
                await message.channel.send("Although they are known to be aggressive, they tend to relax after they win a battle.")

            if num == 3:
                await message.channel.send("A Charmeleon will use the fire on its tail to raise the temperature around it, tormenting the opponent with a hot atmosphere!")

        if message.content.startswith('!ro charizard'):
            await message.channel.send("Charizard, the Fire/Flying type Pokémon")
            await message.channel.send("Pokédex entry NO.006")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Charizard tend to live in mountains and even inhabit volcanoes with others of its species!")

            if num == 2:
                await message.channel.send("Charizard fly around in search of strong opponents, with its fire on its tail burning brighter with gained experience!")
                await message.channel.send("They will never fight anything weaker than themselves.")

            if num == 3:
                await message.channel.send("A Charizard's fiery breath can melt boulders and huge glaciers.")
                await message.channel.send("It's also been known to accidentally start forrest fires!")

        if message.content.startswith('!ro squirtle'):
            await message.channel.send("Squirtle, the Water type Pokémon.")
            await message.channel.send("Pokédex entry NO.007")

            num = random.randint(1, 4)

            if num == 1:
                await message.channel.send("At birth, a squirtle's shell is really soft.")
                await message.channel.send("But, moments after its birth, it hardens and becomes super resilient!")

            if num == 2:
                await message.channel.send("The shape of a squirtle's shell is water resistant, allowing them to swim at high speeds!")

            if num == 3:
                await message.channel.send("Squirtle are able to shoot water from their mouths with high accuracy.")

            if num == 4:
                await message.channel.send("When they sleep, squirtle withdraw into their shells.")
                await message.channel.send("They do this as protection from predators as they rest.")
                await message.channel.send("They even sometimes rock back and forth in their shells when content!")

        if message.content.startswith('!ro wartortle'):
            await message.channel.send("Wartortle, the Water type Pokémon")
            await message.channel.send("Pokédex entry NO.008")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Wartortle's flowing tail is a symbol of longevity and good fortune, which makes it popular among elderly people!")

            if num == 2:
                await message.channel.send("Because they're bigger than their previous form, they have a harder time finding balance.")
                await message.channel.send("To counteract this, they use their fluffy ears to keep upright, and they do this both on land and in water!")

            if num == 3:
                await message.channel.send("As it sleeps, it keeps its furry tail poking out of its shell,")
                await message.channel.send("It does this to feel out its surroundings in case of danger!")

        if message.content.startswith('!ro blastoise'):
            await message.channel.send("Blastoise, the Water type Pokémon.")
            await message.channel.send("Pokédex entry NO.009")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("A shoot from the cannon of a blastoise is enough to pierce steel and concrete!")

            if num == 2:
                await message.channel.send("Blastoise have sturdy legs and backs,")
                await message.channel.send("This allows them to withstand the recoil that their cannons produce!")

            if num == 3:
                await message.channel.send("Blastoise are able to propel themselves forward with their cannons, allowing for a devastating tackle!")

        #Gen 2 Starters
        if message.content.startswith("!ro chikorita"):
            await message.channel.send("Chikorita, the Grass type Pokémon")
            await message.channel.send("Pokédex entry NO.152")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Chikorita use the leaf on their heads to seek out warm places to sleep!")

            if num == 2:
                await message.channel.send("The leaf on a chikorita gives off a pleasant aroma able to calm down battling pokémon!")

            if num == 3:
                await message.channel.send("Chikorita love to sunbathe, making it common to see them in grassy fields on a sunny day!")

        if message.content.startswith("!ro bayleef"):
            await message.channel.send("Bayleef, the Grass type Pokémon")
            await message.channel.send("Pokédex entry NO.153")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Its leaves give off a spicy scent which has many benefits.")
                await message.channel.send("These benefits include a boost in energy and health!")

            if num == 2:
                await message.channel.send("Pokémon that rest near bayleef usually tend to feel energized and ready to fight!")

            if num == 3:
                await message.channel.send("It's rumored that a bayleef bud's properties contrast to actual bay leaves!")

        if message.content.startswith("!ro meganium"):
            await message.channel.send("Meganium, the Grass type Pokémon.")
            await message.channel.send("Pokédex entry NO.154")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Meganium give off a pleasant aroma that's said to make someone feel as if they're in the soothing atmosphere of a forest!")

            if num == 2:
                await message.channel.send("Its breath contains the power to revive plants and nature that have withered away!")

            if num == 3:
                await message.channel.send("Meganium tend to be very docile, and are known to be peacemakers!")

        if message.content.startswith("!ro cyndaquil"):
            await message.channel.send("Cyndaquil, the Fire type Pokémon.")
            await message.channel.send("Pokédex entry NO.155")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Cyndaquil shoot flames out of their backs when startled or angered.")
                await message.channel.send("These flames intimidate their foes!")

            if num == 2:
                await message.channel.send("Cyndaquil are usually hunch over.")
                await message.channel.send("They do this as they tend to curl up when they feel intimidated.")

            if num == 3:
                await message.channel.send("Cyndaquil like to curl up when they sleep, and occasionally spout flames in their slumber!")

        if message.content.startswith("!ro quilava"):
            await message.channel.send("Quilava, the Fire type Pokémon.")
            await message.channel.send("Pokédex entry NO.156")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Before battle, quilava like to show off how fierce the fire on their backs can burn!")

            if num == 2:
                await message.channel.send("The fur of this pokémon is said to never burn, and can protect it from other fire attacks!")

            if num == 3:
                await message.channel.send("As they sleep, the flames on their back burn bright!")

        if message.content.startswith("!ro typhlosion"):
            await message.channel.send("Typhlosion, the Fire type Pokémon.")
            await message.channel.send("Pokédex entry NO.157")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("When a typhlosion's anger peaks, it is able to become so hot that anything that it comes in contact with will instantly burn up!")

            if num == 2:
                await message.channel.send("Typhlosion are able to create a shimmering haze that they use to hide themselves during battle!")

            if num == 3:
                await message.channel.send("It's recommended to avoid a typhlosion that's asleep, as they tend to accidentally shoot fire from their backs!")

        if message.content.startswith("!ro totodile"):
            await message.channel.send("Totodile, the Water type Pokémon.")
            await message.channel.send("Pokédex entry NO.158")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("Totodile tend to bite down on anything they see, even their own trainer!")

            if num == 2:
                await message.channel.send("A totodile's bite force is enough to bite through anything, which can cause devastating injuries!")

            if num == 3:
                await message.channel.send("Totodile tend to sleep with one eye open and rest only half of their brain at a time!")
                await message.channel.send("This is a practice known as unihemispheric sleep!")

        if message.content.startswith("!ro croconaw"):
            await message.channel.send("Croconaw, the Water type Pokémon.")
            await message.channel.send("Pokédex entry NO.159")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("The tips of a croconaw's fangs are slanted backward, allowing no chance of escape for its prey!")

            if num == 2:
                await message.channel.send("A croconaw is able to regrow its teeth in the case it loses some in an encounter!")
                await message.channel.send("There seems to be no limit to how many times they can grow back!")

            if num == 3:
                await message.channel.send("Although it may seem that they only have 6 sharp teeth, a croconaw's mouth is lined with a total of 48 fangs!")

        if message.content.startswith("!ro feraligatr"):
            await message.channel.send("Feraligatr, the Water type Pokémon")
            await message.channel.send("Pokédex entry NO.160")

            num = random.randint(1, 3)

            if num == 1:
                await message.channel.send("When a feraligatr bits into its opponent, it viciously whips its head around to tear them apart!")

            if num == 2:
                await message.channel.send("Its powerful hind legs allow it to quickly move around on both land and in water!")

            if num == 3:
                await message.channel.send("Feraligatr continues to practice unihemispheric sleep, keeping watch of its surroundings and charging towards any threats it may sense!")

    #    if message.content.startswith("!ro past typhlosion"):

    #éééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééééé

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

token = os.getenv("DISCORD_TOKEN")

client.run(token)

