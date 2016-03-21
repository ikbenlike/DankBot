import discord
import requests
import subprocess
import sys
import os
import asyncio
import random

logFile = open("logs.txt", "a")

tLog = True

def commandLog(message):
	msgData = message.author.name + " - " + message.author.id + " - " + message.content + "\n"
	msgData = msgData.replace("\n", "\n        ")
	if tLog == True:
		print(msgData)
	logFile.write(msgData)


logInFromFile = False


if logInFromFile == False:
	inEmail = input("email: ")
	inPassword = input("password: ")
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system('clear')
elif logInFromFile == True:
	with open("config/inemail.txt") as loginemail:
		inEmail = loginemail.read().replace('\n', '')
	with open("config/inpassword.txt") as loginpassword:
		inPassword = loginpassword.read().replace('\n', '')


discord.opus.load_opus
client = discord.Client()


ownerID = "125422419736395777"
with open("config/prefix.txt") as myfile:
	prefix=myfile.read().replace('\n', '')

modIDList = open("config/mods.txt", "r")
modIDs = modIDList.read().replace("\n", " ")

#player = ""

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
	global modIDs
	global modIDList
	if message.content.startswith(prefix + "voice"):
		commandLog(message)
		input_ = message.content
		input_.split(" ")
		args = input_.split(" ")[1:]
		vcommand = args[0]
		connectChannel = args[1:]
		print(connectChannel)


		if vcommand == "connect":
			if message.author.id in modIDs:
				vChannel = discord.utils.find(lambda m: m.name == (" ".join(connectChannel)), client.get_all_channels())
				vClient = await client.join_voice_channel(vChannel)
				player = vClient.create_ffmpeg_player("sounds/empty.wav")
				player.start()
			else:
				await client.send_message(message.channel, message.author.mention + " you don't have permission to do that")


		elif vcommand == "disconnect":
			if message.author.id in modIDs:
				await vClient.disconnect()
			else:
				await client.send_message(message.channel, message.author.mention + " you don't have permission to do that")


		elif vcommand == "play":
			trackToPlay = args[1]
			if trackToPlay == "pyro-oh-no":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/Pyrocynical_-_Oh_no_OH_NO.wav")
					player.start()
			elif trackToPlay == "mlg-k":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/Pyrocynical_-_K.wav")
					player.start()
			elif trackToPlay == "long-k":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/Pyrocynical_-_Kkkkk.wav")
					player.start()
			elif trackToPlay == "hmmm":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/Pyrocynical_ft._Disappointed_dad_-_HM_HMMM.wav")
					player.start()
			elif trackToPlay == "arrow":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/arrow-to-the-knee.mp3")
					player.start()
			elif trackToPlay == "airhorn":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/airhorn-mgl.mp3")
					player.start()
			elif trackToPlay == "alluha-akbar":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/alluha-ackbar.mp3")
					player.start()
			elif trackToPlay == "combo-breaker":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/combo-breaker.mp3")
					player.start()
			elif trackToPlay == "damn-son":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/damn-son-whered-you-find-this.mp3")
					player.start()
			elif trackToPlay == "sandstorm":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/darude-sandstorm.mp3")
					player.start()
			elif trackToPlay == "barrel-roll":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/do-a-barrel-rol.mp3")
					player.start()
			elif trackToPlay == "dun-dun-dun":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/dun-dun-dun.mp3")
					player.start()
			elif trackToPlay == "fatality":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/fatality.wav")
					player.start()
			elif trackToPlay == "get-noscoped":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/get-noscoped.mp3")
					player.start()
			elif trackToPlay == "hasta-la-vista":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/hasta-la-vista.mp3")
					player.start()
			elif trackToPlay == "hax":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/hax.wav")
					player.start()
			elif trackToPlay == "headshot":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/headshot.wav")
					player.start()
			elif trackToPlay == "hitmarker":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/hitmarker.wav")
					player.start()
			elif trackToPlay == "inception":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/inception-horn.mp3")
					player.start()
			elif trackToPlay == "its-a-trap":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/its-a-trap.mp3")
					player.start()
			elif trackToPlay == "9000":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/its-over-9000.mp3")
					player.start()
			elif trackToPlay == "its-time-to-stop":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/its-time-to-stop.mp3")
					player.start()
			elif trackToPlay == "john-cena":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/john-cena.mp3")
					player.start()
			elif trackToPlay == "kazoo":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/kazoo-kid-trap-remix.mp3")
					player.start()
			elif trackToPlay == "here-we-go":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/mario-here-we-go.wav")
					player.start()
			elif trackToPlay == "jeff":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/my-name-is-jeff.mp3")
					player.start()
			elif trackToPlay == "rickroll":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/rickroll.mp3")
					player.start()
			elif trackToPlay == "small-loan":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/small-loan-of-a-million-dollars.mp3")
					player.start()
			elif trackToPlay == "weed":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/smoke-weed-everyday.mp3")
					player.start()
			elif trackToPlay == "surprise":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/surprise-motherfucker.wav")
					player.start()
			elif trackToPlay == "tadaah":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/tadaah.mp3")
					player.start()
			elif trackToPlay == "racist":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/thats-racist.mp3")
					player.start()
			elif trackToPlay == "sparta":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/this-is-sparta.mp3")
					player.start()
			elif trackToPlay == "thomas":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/thomas-tank-engine.mp3")
					player.start()
			elif trackToPlay == "what-is-love":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/what-is-love-haddaway.mp3")
					player.start()
			elif trackToPlay == "what-is-this":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/what-is-this.mp3")
					player.start()
			elif trackToPlay == "wtf":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/wtf.mp3")
					player.start()
			elif trackToPlay == "you-shall-not-pass":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/you-shall-not-pass.mp3")
					player.start()
			elif trackToPlay == "im-blue":
				try:
					player.stop()
				finally:
					player = vClient.create_ffmpeg_player("sounds/im-blue.mp3")
					player.start()

		elif vcommand == "yt":
			urlToPlay = args[1]
			try:
				player.stop()
			finally:
				player = await vClient.create_ytdl_player(urlToPlay)
				player.start()


	elif message.content.startswith(prefix + "meme"):
		commandLog(message)
		memeList = open("config/dank.txt", "r")
		memeLines = memeList.readlines()
		memeToSend = random.choice(memeLines)
		await client.send_message(message.channel, memeToSend)
		memeList.close()

	elif message.content.startswith(prefix + "logout"):
		commandLog(message)
		if message.author.id in modIDs:
			try:
				player.stop()
				await vClient.disconnect()
			finally:
				await client.logout()
		else:
			await client.send_message(message.channel, message.author.mention + " you don't have permission to do that")


	elif message.content.startswith(prefix + "prefix"):
		commandLog(message)
		if message.author.id in modIDs:
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
			await client.send_message(message.channel, message.author.mention + " you don't have permission to do that")


	elif message.content.startswith(prefix + "game"):
		commandLog(message)
		if message.author.id in modIDs:
			input_ = message.content
			input_.split(" ")
			stuff = input_.split(" ")[1:]
			game = discord.Game()
			gameName = (" ".join(stuff))
			game.name = gameName
			await client.change_status(game=game)
			await client.send_message(message.channel, client.user.name + "'s game has been set to " + gameName)
		else:
			await client.send_message(message.channel, message.author.mention + " you don't have permission to do that")


	if '<@' + client.user.id + '>' in message.content:
		with open("config/prefix.txt") as myfile:
			sayPrefix=myfile.read().replace('\n', '')
		await client.send_message(message.channel, "Hi there! My prefix is " + sayPrefix + ". Type `" + sayPrefix + "commands` to see my commands")



client.run(inEmail, inPassword)
