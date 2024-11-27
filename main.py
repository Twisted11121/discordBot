import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    request = message.content.lower()
    
    if request.startswith("!gif"):
        await gif(message)
    
    elif request.startswith("!"):
        await calc(message)
    

async def gif(message):
    folder = "gifs"
    gifs = os.listdir(folder)
    random_gif = random.choice(gifs)
    
    request = message.content
    
    if request.startswith("!gif"):
        return await message.channel.send(file=discord.File(f'{folder}/{random_gif}'))
   
async def calc(message):
    if message.author == client.user:
        return
    
    data_og = message.content
    
    math_operations = {
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/",
    "**": "**",
    "%": "%",
    "//": "//"
    }
 
    data = []
    operation = ""
    number=""
    
    for item in data_og[1:]:
        if item in math_operations:
            operation = item
            if number:
                data.append(int(number))
                number = ""
        else:
            number += item
    
    if number:
        data.append(int(number))
    
    if data_og.startswith("!"):
        result = eval(f"{data[0]} {operation} {data[1]}")
        return await message.channel.send(f"{data[0]} {operation} {data[1]} = {result}")
        exit
 

 
   


client.run('')