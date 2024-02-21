#with open('text.txt', 'r', encoding='utf-8') as f:
#    print(f.read())
import discord, random, os

imagenes_1 = random.choice(os.listdir("imagenes_1"))
with open(f'imagenes_1/{imagenes_1}', 'rb') as f:
        picture = discord.File(f)
