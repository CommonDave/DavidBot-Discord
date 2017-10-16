import logging
import discord
import asyncio
import random
import opuslib
import ctypes
from discord.ext import commands

discord.opus.load_opus(ctypes.util.find_library('opus'))

logging.basicConfig(level=logging.INFO)

client = commands.Bot(command_prefix="d.")
@client.event
async def on_ready():
    print('Logged in as: ')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client)
    if discord.opus.is_loaded() == True:
        print("Opus is loaded")
    else:
        print("Opus is not loaded")
    await client.change_presence(game=discord.Game(name='with dicks'))

@client.command(pass_context=True)
async def play(ctx, youtube_url):
    channel = ctx.message.author.voice.voice_channel
    if channel is not None:
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                return await x.disconnect()
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player(youtube_url)
        player.start()
    else:
        voice = await client.join_voice_channel(channel)
        player = await voice.create_ytdl_player(youtube_url)
        player.start()


@client.command(pass_context=True)
async def gay(ctx):
        await client.send_message(ctx.message.channel, 'lol ur gay')

@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not connected to any voice channel on this server!")

@client.command(pass_context = True)
async def heil(ctx):
    await client.send_file(ctx.message.channel, 'hitler-getty.jpg')

@client.command(pass_context = True)
async def playing(ctx):
    np = str(await client.player.yt())
    await client.send_message(context.message.channel, np)

bot_prefix = "d."
client.run("INSERT_TOKEN_HERE")
