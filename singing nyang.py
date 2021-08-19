import discord
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix="늅냥아 ")


@client.command()
async def 노래해(ctx, url : str):
    await ctx.send("노래 시키면 해야지 뭐..")
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("다음 음악때까지 기달려!")
        return
    
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def 따라와(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        
    await channel.connect()

@client.command()
async def 저리가(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("이미 나가있어")


@client.command()
async def 잠깐만(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("아무것도 안하고 있었는데?")


@client.command()
async def 계속해(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("하고 있었는데?")


@client.command()
async def 멈춰(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("드디어 해방이다")

client.run('Import a bot token')