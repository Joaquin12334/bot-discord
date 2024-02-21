import discord
from discord.ext import commands
import random
from bot_2 import gen_pass
from bot_3 import flip_coin, coin_sides
import os, random
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def pasw(ctx, *, message: str):
    """Generate a password."""
    try:
        length = int(message)
    except ValueError:
        await ctx.send("Por favor, proporciona un número válido para la longitud de la contraseña.")
        return
    
    if length <= 0:
        await ctx.send("La longitud debe ser mayor que cero.")
        return
    
    await ctx.send("Tu nueva clave es: " + gen_pass(length))


@bot.command()
async def ayuda(ctx):
    """Give all comands details and examples"""
    await ctx.send("""***Los comandos del bot son:*
**
*?pasw [mùmero] *= Te da una conttraseña aleatoria con la cantidad de variables que pongas despues del comando

*?coin *= Jira una moneda aleatoreamente te da el resultado (cara o sello)

*?add* [nùmero a - nùmero b] = Suma dos numeros que pongas despues del comando

*?rest* [nùmero a - nùmero b] = Resta dos numeros que pongas despues del comando

*?mult *[nùmero a - nùmero b] = Multiplica dos numeros que pongas despues del comando

*?roll* [NdN] = Lanza un dado en el formato "NdN" y muestra el resultado. Por ejemplo, ?roll 2d6 lanzará dos dados de seis caras.

*?choose* = [(opcion1) (opcion2) ...] = Elige aleatoriamente una de las opciones proporcionadas por el usuario y la muestra.

*?repeat *.= [(num de veces) (contenido a repetir)] = Repite un mensaje una cantidad de veces especificada por el usuario. El contenido del mensaje es opcional y, por defecto, es "repeating...".

*?joined* = [Miembro del servidor] = Muestra la fecha en la que se unio el miembro al servidor

*?cool* =  Comando base para verificar si un usuario es "cool". Si no se especifica un subcomando, responde que el usuario no es "cool".

*?cool bot* =  Verifica si el bot es "cool" y responde afirmativamente.""")


@bot.command()
async def coin(ctx):
    """Flip a coin."""
    await ctx.send("¡La moneda cayò!, el lado que salio es: "+flip_coin(coin_sides))


@bot.command()
async def hola(ctx):
    """Say hi."""
    await ctx.send("Mucho gusto ^^, para ver lo que puedo hacer a detalle escribe ?ayuda")


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def rest(ctx, left: int, right: int):
    """Rest two numbers together."""
    await ctx.send(left - right)


@bot.command()
async def mult(ctx, left: int, right: int):
    """X two numbers together."""
    await ctx.send(left * right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


@bot.command()
async def mem(ctx):
    imagenes_1 = random.choice(os.listdir("imagenes_1"))
    with open(f'imagenes_1/{imagenes_1}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command('reciclaje')
async def reciclaje(ctx, message: str):
    sec = (message)
    if sec == "consejos":
        consejos = random.choice(os.listdir("consejos"))
        with open(f'consejos/{consejos}', 'rb') as f:
            picture = discord.File(f)
        
    elif sec == "manualidad":
        manualidad = random.choice(os.listdir("manualidad"))
        with open(f'manualidad/{manualidad}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command('meme')
async def meme(ctx, message: str):
    sec = (message)
    no = ("Por el momento no tenemos esa categoria")
    if sec == "animales":
        animales = random.choice(os.listdir("animales"))
        with open(f'animales/{animales}', 'rb') as f:
            picture = discord.File(f)
        
    elif sec == "peliculas":
        peliculas = random.choice(os.listdir("peliculas"))
        with open(f'peliculas/{peliculas}', 'rb') as f:
            picture = discord.File(f)

    elif sec == "programacion":
        programacion = random.choice(os.listdir("programacion"))
        with open(f'programacion/{programacion}', 'rb') as f:
            picture = discord.File(f)

    elif sec == "" or sec == "random":
        memes = random.choice(os.listdir("memes"))
        with open(f'memes/{memes}', 'rb') as f:
            picture = discord.File(f)

    elif sec == "videojuegos":
        videojuegos = random.choice(os.listdir("videojuegos"))
        with open(f'videojuegos/{videojuegos}', 'rb') as f:
            picture = discord.File(f)

    elif sec == "series":
        series = random.choice(os.listdir("series"))
        with open(f'series/{series}', 'rb') as f:
            picture = discord.File(f)

    else:
        picture = no

    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('animal')
async def animal(ctx, message: str):
    ani = (message)
    if ani == "duck":
        image_url = get_duck_image_url()

    elif ani == "dog":
        image_url = get_dog_image_url()

    else:
        image_url = "Por lo pronto no tenemos ese animal en el catalogo"

    await ctx.send(image_url)


bot.run("TOKEN")
