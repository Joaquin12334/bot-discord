import discord
from bot_2 import gen_pass
from bot_3 import flip_coin, coin_sides

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$contraseña"):
        await message.channel.send("tu nueva clave es: "+gen_pass(10))
    elif message.content.startswith("$moneda"):
        await message.channel.send("¡La moneda cayò!, el lado que salio es: "+flip_coin(coin_sides))
    else:
        await message.channel.send(message.content)

client.run("MTIwMTU3MjczMDI4NjM3NDkxMg.GlpX4x.6Br3m1kmcCM4jYtMLa2R2YQDSxzqge5OhXv5LA")
pass
