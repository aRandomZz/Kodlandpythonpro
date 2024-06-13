import discord
import random
from bot_logic import gen_pass,gen_emodji, flip_coin
TOKEN='token' #security purposes
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
rps=False
rps_list=['cissors', 'rock', 'paper']
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
    await client.change_presence(activity=discord.CustomActivity(name='I AM ALIVE 🖥️'))

@client.event
async def on_message(message):
    global rps
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hi!')
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$emoji'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$rps'):
        rps=True
        await message.channel.send("Choose... I'll be waiting")
    elif rps==True and (message.content.startswith('$scissors') or message.content.startswith('$rock') or message.content.startswith('$paper')):
        if random.randint(0,2)==1:
            await message.channel.send("You won... but not for long.")
        else:
            await message.channel.send("I WON AND I WILL KILL YOUR PLUSHIES MUAJAJAJAJA")
        rps=False
    elif rps==True and not (message.content.startswith('$scissors') or message.content.startswith('$rock') or message.content.startswith('$paper')):
        await message.channel.send("You are boring...")
        rps=False
    else:
        await message.channel.send(message.content + ', siuuu')
    
    
    
client.run(TOKEN)
