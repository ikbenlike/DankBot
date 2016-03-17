import discord
import requests
import subprocess
import sys
import os
import asyncio

inEmail = input("email: ")
inPassword = input("password: ")
os.system('clear')

discord.opus.load_opus
client = discord.Client()

prefix = "$"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):
    global vClient
    if message.content.startswith(prefix + "voice"):
        input_ = message.content
        input_.split(" ")
        args = input_.split(" ")[1:]
        vcommand = args[0]
        connectChannel = args[1:]
        print(connectChannel)
        if vcommand == "connect":
            vChannel = discord.utils.find(lambda m: m.name == (" ".join(connectChannel)), client.get_all_channels())
            vClient = await client.join_voice_channel(vChannel)
        elif vcommand == "disconnect":
            await vClient.disconnect()
        elif vcommand == "play":
            trackToPlay = args[1]
            if trackToPlay == "pyro-oh-no":
                player = vClient.create_ffmpeg_player("Pyrocynical_-_Oh_no_OH_NO.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "mlg-k":
                player = vClient.create_ffmpeg_player("Pyrocynical_-_K.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "long-k":
                player = vClient.create_ffmpeg_player("Pyrocynical_-_Kkkkk.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hmmm":
                player = vClient.create_ffmpeg_player("Pyrocynical_ft._Disappointed_dad_-_HM_HMMM.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "arrow":
                player = vClient.create_ffmpeg_player("arrow-to-the-knee.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "airhorn":
                player = vClient.create_ffmpeg_player("airhorn-mgl.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "alluha-akbar":
                player = vClient.create_ffmpeg_player("alluha-ackbar.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "combo-breaker":
                player = vClient.create_ffmpeg_player("combo-breaker.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "damn-son":
                player = vClient.create_ffmpeg_player("damn-son-whered-you-find-this.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "sandstorm":
                player = vClient.create_ffmpeg_player("darude-sandstorm.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "barrel-roll":
                player = vClient.create_ffmpeg_player("do-a-barrel-rol.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "dun-dun-dun":
                player = vClient.create_ffmpeg_player("dun-dun-dun.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "fatality":
                player = vClient.create_ffmpeg_player("fatality.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "get-noscoped":
                player = vClient.create_ffmpeg_player("get-noscoped.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hasta-la-vista":
                player = vClient.create_ffmpeg_player("hasta-la-vista.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hax":
                player = vClient.create_ffmpeg_player("hax.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "headshot":
                player = vClient.create_ffmpeg_player("headshot.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "hitmarker":
                player = vClient.create_ffmpeg_player("hitmarker.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "inception":
                player = vClient.create_ffmpeg_player("inception-horn.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "its-a-trap":
                player = vClient.create_ffmpeg_player("its-a-trap.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "9000":
                player = vClient.create_ffmpeg_player("its-over-9000.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "its-time-to-stop":
                player = vClient.create_ffmpeg_player("its-time-to-stop.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "john-cena":
                player = vClient.create_ffmpeg_player("john-cena.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "kazoo":
                player = vClient.create_ffmpeg_player("kazoo-kid-trap-remix.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "here-we-go":
                player = vClient.create_ffmpeg_player("mario-here-we-go.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "jeff":
                player = vClient.create_ffmpeg_player("my-name-is-jeff.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "rickroll":
                player = vClient.create_ffmpeg_player("rickroll.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "small-loan":
                player = vClient.create_ffmpeg_player("a-small-loan-of-a-million-dollars.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "weed":
                player = vClient.create_ffmpeg_player("smoke-weed-everyday.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "surprise":
                player = vClient.create_ffmpeg_player("surprise-motherfucker.wav")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "tadaah":
                player = vClient.create_ffmpeg_player("tadaah.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "racist":
                player = vClient.create_ffmpeg_player("thats-racist.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "sparta":
                player = vClient.create_ffmpeg_player("this-is-sparta.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "thomas":
                player = vClient.create_ffmpeg_player("thomas-tank-engine.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "what-is-love":
                player = vClient.create_ffmpeg_player("what-is-love-haddaway.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "what-is-this":
                player = vClient.create_ffmpeg_player("what-is-this.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "wtf":
                player = vClient.create_ffmpeg_player("wtf.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()
            if trackToPlay == "you-shall-not-pass":
                player = vClient.create_ffmpeg_player("you-shall-not-pass.mp3")
                player.start()
                if player.is_playing() == False:
                    player.stop()

    if message.content.startswith(prefix + "logout"):
        await vClient.disconnect()
        await client.logout()



client.run(inEmail, inPassword)
