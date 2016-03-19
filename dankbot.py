import discord
import requests
import subprocess
import sys
import os
import asyncio
import random

inEmail = input("email: ")
inPassword = input("password: ")
os.system('clear')

discord.opus.load_opus
client = discord.Client()

ownerID = "125422419736395777"
with open("config/prefix.txt") as myfile:
    prefix=myfile.read().replace('\n', '')
#prefix = open("config/prefix.txt", "r")
player = ""
#memeList = open("dank.txt", "r")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):
    global vClient
    global player
    global prefix
    if message.content.startswith(prefix + "voice"):
        input_ = message.content
        input_.split(" ")
        args = input_.split(" ")[1:]
        vcommand = args[0]
        connectChannel = args[1:]
        print(connectChannel)

        if vcommand == "connect":
            if message.author.id == ownerID:
                vChannel = discord.utils.find(lambda m: m.name == (" ".join(connectChannel)), client.get_all_channels())
                vClient = await client.join_voice_channel(vChannel)
                player = vClient.create_ffmpeg_player("empty.wav")
                player.start()
            else:
                await client.send_message(message.channel, "<@" + message.author.id + "> you don't have permission to do that")


        elif vcommand == "disconnect":
            if message.author.id == ownerID:
                await vClient.disconnect()
            else:
                await client.send_message(message.channel, "<@" + message.author.id + "> you don't have permission to do that")


        elif vcommand == "play":
            trackToPlay = args[1]
            if trackToPlay == "pyro-oh-no":
                player.stop()
                player = vClient.create_ffmpeg_player("/home/thewatcher/metabot py/DankBot/Pyrocynical_-_Oh_no_OH_NO.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "mlg-k":
                player.stop()
                player = vClient.create_ffmpeg_player("Pyrocynical_-_K.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "long-k":
                player.stop()
                player = vClient.create_ffmpeg_player("Pyrocynical_-_Kkkkk.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hmmm":
                player.stop()
                player = vClient.create_ffmpeg_player("Pyrocynical_ft._Disappointed_dad_-_HM_HMMM.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "arrow":
                player.stop()
                player = vClient.create_ffmpeg_player("arrow-to-the-knee.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "airhorn":
                player.stop()
                player = vClient.create_ffmpeg_player("airhorn-mgl.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "alluha-akbar":
                player.stop()
                player = vClient.create_ffmpeg_player("alluha-ackbar.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "combo-breaker":
                player.stop()
                player = vClient.create_ffmpeg_player("combo-breaker.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "damn-son":
                player.stop()
                player = vClient.create_ffmpeg_player("damn-son-whered-you-find-this.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "sandstorm":
                player.stop()
                player = vClient.create_ffmpeg_player("darude-sandstorm.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "barrel-roll":
                player.stop()
                player = vClient.create_ffmpeg_player("do-a-barrel-rol.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "dun-dun-dun":
                player.stop()
                player = vClient.create_ffmpeg_player("dun-dun-dun.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "fatality":
                player.stop()
                player = vClient.create_ffmpeg_player("fatality.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "get-noscoped":
                player.stop()
                player = vClient.create_ffmpeg_player("get-noscoped.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hasta-la-vista":
                player.stop()
                player = vClient.create_ffmpeg_player("hasta-la-vista.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hax":
                player.stop()
                player = vClient.create_ffmpeg_player("hax.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "headshot":
                player.stop()
                player = vClient.create_ffmpeg_player("headshot.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hitmarker":
                player.stop()
                player = vClient.create_ffmpeg_player("hitmarker.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "inception":
                player.stop()
                player = vClient.create_ffmpeg_player("inception-horn.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "its-a-trap":
                player.stop()
                player = vClient.create_ffmpeg_player("its-a-trap.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "9000":
                player.stop()
                player = vClient.create_ffmpeg_player("its-over-9000.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "its-time-to-stop":
                player.stop()
                player = vClient.create_ffmpeg_player("its-time-to-stop.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "john-cena":
                player.stop()
                player = vClient.create_ffmpeg_player("john-cena.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "kazoo":
                player.stop()
                player = vClient.create_ffmpeg_player("kazoo-kid-trap-remix.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "here-we-go":
                player.stop()
                player = vClient.create_ffmpeg_player("mario-here-we-go.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "jeff":
                player.stop()
                player = vClient.create_ffmpeg_player("my-name-is-jeff.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "rickroll":
                player.stop()
                player = vClient.create_ffmpeg_player("rickroll.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "small-loan":
                player.stop()
                player = vClient.create_ffmpeg_player("small-loan-of-a-million-dollars.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "weed":
                player.stop()
                player = vClient.create_ffmpeg_player("smoke-weed-everyday.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "surprise":
                player.stop()
                player = vClient.create_ffmpeg_player("surprise-motherfucker.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "tadaah":
                player.stop()
                player = vClient.create_ffmpeg_player("tadaah.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "racist":
                player.stop()
                player = vClient.create_ffmpeg_player("thats-racist.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "sparta":
                player.stop()
                player = vClient.create_ffmpeg_player("this-is-sparta.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "thomas":
                player.stop()
                player = vClient.create_ffmpeg_player("thomas-tank-engine.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "what-is-love":
                player.stop()
                player = vClient.create_ffmpeg_player("what-is-love-haddaway.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "what-is-this":
                player.stop()
                player = vClient.create_ffmpeg_player("what-is-this.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "wtf":
                player.stop()
                player = vClient.create_ffmpeg_player("wtf.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "you-shall-not-pass":
                player.stop()
                player = vClient.create_ffmpeg_player("you-shall-not-pass.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "im-blue":
                player.stop()
                player = vClient.create_ffmpeg_player("im-blue.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()

    if message.content.startswith(prefix + "meme"):
        memeList = open("dank.txt", "r")
        memeLines = memeList.readlines()
        memeToSend = random.choice(memeLines)
        await client.send_message(message.channel, memeToSend)
        memeList.close()

    if message.content.startswith(prefix + "logout"):
        if message.author.id == ownerID:
            player.stop()
            await vClient.disconnect()
            await client.logout()
        else:
            await client.send_message(message.channel, "<@" + message.author.id + "> you don't have permission to do that")


    if message.content.startswith(prefix + "prefix"):
        if message.author.id == ownerID:
            input_ = message.content
            input_.split(" ")
            args = input_.split(" ")[1:]
            setPrefixTo = args[0]
            prefixFile = open("config/prefix.txt", "w")
            prefixFile.write(setPrefixTo)
            prefixFile.close()
            with open("config/prefix.txt") as myfile:
                prefix=myfile.read().replace('\n', '')
            await client.send_message(message.channel, client.user.name + "'s prefix has changed to " + setPrefixTo)
        else:
            await client.send_message(message.channel, "<@" + message.author.id + "> you don't have permission to do that")




client.run(inEmail, inPassword)
