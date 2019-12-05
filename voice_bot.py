import discord
import threading
import asyncio
import random
import youtube_dl
import xml.etree.ElementTree as ET

def read_token():
    with open("token.txt" ,"r") as f:
        lines =f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()
#Load Opus
#discord.opus.load_opus("opus")

#On Ready
@client.event
def on_ready():
	print ("Connected!")
	yield from client.change_status(game=discord.Game(name="By: @ErraticErrors"), idle=False)

voice = None
player = None

#Checks if user has perm
def has_perm(userida, level, message):
	userid = str(userida)
	permissions = ET.parse('permissions.xml')
	for user in permissions.findall("user"):
		if user.get('id') == userid and int(user.get('level')) >= int(level):
			return True;
	if level == "0":
		return True;
	yield from client.send_message(message.channel, "%s - You don't have permission" %(message.author.mention))
	return False;

def get_level(userid):
	permissions = ET.parse("permissions.xml")
	for user in permissions.findall("user"):
		if user.get('id') == userid:
			return user.get("level")
	return "0"

#Handles the voice command
def voiceHandler(message):
	global voice
	global player
	args = message.content.split(" ")
	#voice leave
	if args[2] == "leave":
		try:
			if player.is_playing():
				yield from client.send_message(message.channel, "Cannot leave while music is still playing")
		except:
			print("Exception handled")
			yield from voice.disconnect()
			yield from client.send_message(message.channel, "Left Channel")
		else:
			yield from voice.disconnect()
			yield from client.send_message(message.channel, "Left channel")
	#voice join [channel]
	if args[2] == "join":
		tocombine = args[3:]
		searchcriteria = " ".join(tocombine)
		yield from client.send_message(message.channel, "Joining Voice Channel: %s" %(searchcriteria))
		channel = discord.utils.find(lambda c: c.name == searchcriteria and c.type == discord.ChannelType.voice, message.server.channels)
		voice = yield from client.join_voice_channel(channel)
	#voice stream
	if args[2] == "stream":
		#voice stream ytube [ytube url]
		if args[3] == "ytube":
			try:
				if player.is_playing():
					yield from client.send_message(message.channel, "ErraticBot is still playing a song")
					return
				if not voice.is_connected():
					yield from client.send_message(message.channel, "Must be in a voice channel to play audio")
					return
			except:
				print ("Exception handled!")
			#voice.encoder_options(24000, 1)
			player = voice.create_ytdl_player(args[4])
			player.start()
			yield from client.send_message(message.channel, "♪ Playing from youtube source")
		if args[3] == "stop":
			player.stop()
			yield from client.send_message(message.channel, "Stream stopped")
	#voice record
	if args[2] == "record" and has_perm(message.author, "10", message):
		if args[3] == "stop":
			client.send_message("Recording stopped")
			return
		try:
			if player.is_playing():
				yield from client.send_message(message.channel, "Cannot record whilst playing audio.")
				return
			if not voice.is_connected():
				yield from client.send_message("Must join a voice channel before recording")
				return
		except:
			print ("Exception handled!")
		client.send_message(message.channel, "Max record time is 10 minutes. Do `ErraticBot, voice record stop` to stop the recording")

#All the dank memes
memes = ["( ͡° ͜ʖ ͡°)", " ¯\_(ツ)_/¯", "Such Discord, Much Gaming, Very How-To, WOW", "http://static.fjcdn.com/pictures/It+s+an+old+meme....+how+I+feel+when+I+see_e83de6_3481193.jpg", "https://s-media-cache-ak0.pinimg.com/originals/43/06/2f/43062ff5228e5a49872d5322acc0982a.jpg", "https://imgflip.com/s/meme/Creepy-Condescending-Wonka.jpg", "http://media.breitbart.com/media/2015/04/Poetin2.jpg"]
#Fake Errors
errors = ["9÷0= *oh, darn*", "Windows Vista Crashed....... *Again*", "I made Ava mad", "Damn Daniel", "404 - Error not found", "Damnit Python", "Connection problems? Check my status here: https://www.youtube.com/watch?v=dQw4w9WgXcQ&", "Discord cannot recognize your keyboard. Press Alt+F4 to fix.", "DDoSed by Mosin", "GTA You Unstable Skrub"]

@client.event
async def on_message(message):
	args = message.content.split(" ")
	print ("<%s>[%s] %s" %(message.channel, message.author, message.content))
	if message.content.startswith("ErraticBot,"):
		#Ping Command
		if message.content == "ErraticBot, ping":
            yield from message.channel.send("Pong!")
		#Meme Command
		elif message.content == "ErraticBot, meme" and has_perm(message.author, "3", message):
			yield from client.send_message(message.channel, memes[random.randint(1, len(memes)) - 1])
		#Voice Command
		elif message.content.startswith("ErraticBot, voice") and has_perm(message.author, "5", message):
			yield from voiceHandler(message)
		#Commands
		elif message.content == "ErraticBot, commands":
			yield from client.send_message(message.channel, "%s Commands:\n```\nPingCommand - ErraticBot, ping\nMemeCommand - ErraticBot, meme\nVoiceCommand - ErraticBot, voice\n```" %(message.author.mention))
		#Get user ID
		elif message.content.startswith("ErraticBot, id"):
			if len(args) == 2:
				yield from client.send_message(message.channel, message.author.id)
			else:
				yield from client.send_message(message.channel, args[2][2:-1])
		#Get permissions level
		elif message.content.startswith("ErraticBot, getperm"):
			user = discord.utils.find(lambda u: u.name == args[2] , message.server.members)
			yield from client.send_message(message.channel, "%s User level is: %s" %(message.author.mention, get_level(user.id)))
		#Avatar Command
		elif message.content.startswith("ErraticBot, avatar") and has_perm(message.author, "3", message):
			user = discord.utils.find(lambda u: u.name == args[2] , message.server.members)
			yield from client.send_message(message.channel, user.avatar_url)
		#Crash
		elif message.content == "ErraticBot, crash" and has_perm(message.author, "5", message):
			yield from client.send_message(message.channel, errors[random.randint(1, len(memes))-1])
		#Command Not found
		else:
			yield from client.send_message(message.channel, "%s Command Not Found!" %(message.author.mention))


client.run(token)