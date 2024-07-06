import discord
import random
import asyncio
from discord.ext import commands
TOKEN='your token here'
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
client = discord.Client(intents=intents)
#consejos
COMPOSTING=[
    'Even paper plates and uncoated napkins can be used for compost!',
    'Make sure your wastes don\'t have any chemical in them.',
    'Food scraps are found anywhere, but they are very nourishing for plants!'
]
RECYCLING=[
    'The sky is the limit for kids! Give a kid a recycled toy and they will have lots of adventures.',
    'Lithium batteries can be recycled for making a big robot.',
    'Toilet paper rolls are the best round recyclable material you will find, apart from tires.',
    'Give your plants brand new looks with stylish recycled planter pots!',
    'Don\'t know what to do with paper scraps? Make bricks by stuffing them into a plastic bottle.'
]


@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
    await client.change_presence(activity=discord.Game(name='caring for the environment'))

@client.event
async def on_message(message):
    if message.content.startswith('$tip'):
        channel= message.channel
        await message.channel.send("Choose the area of your choosing: **composting** and **recycling**")
        def check_c(m):
            return (m.content == 'composting' or m.content== 'recycling') and m.channel == channel
        try:
            msg = await client.wait_for('message', check=check_c, timeout=10)
            #commands.client.add_listener(function, 'on_message')
        except asyncio.TimeoutError:
            await message.channel.send("Too slow!")
        else:
            if msg.content=="composting":
                embed = discord.Embed(
                        title=("COMPOSTING ADVICE 🟫"), color=0x008000)
                embed.set_thumbnail(url=msg.author.avatar.url)
                embed.add_field(
                        name='Special advice:',
                        value=random.choice(COMPOSTING),
                        inline=False)

                await message.channel.send(embed=embed)
            elif msg.content=="recycling":
                embed = discord.Embed(
                        title=("RECYCLING ADVICE ♻️"), color=0x008000)
                embed.set_thumbnail(url=msg.author.avatar.url)
                embed.add_field(
                        name='Special advice:',
                        value=random.choice(RECYCLING),
                        inline=False)
                await message.channel.send(embed=embed)


client.run(TOKEN)
