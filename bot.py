# bot.py
import os
import discord
from  recognition_trans import recognition as re

def read_token():
    with open("token.txt" ,"r") as f:
        lines =f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    id = client.get_guild(635858938352369682)
    msg_data = message.content
    Trans_msg = re.LanguageDetect(msg_data)
    if str(message.author)!="TRANS_BOT#9519":
        if Trans_msg != '' :
            await message.channel.send("@"+str(message.author)+" said: "+Trans_msg)

if __name__ == '__main__':
    client.run(token)