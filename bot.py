from secret import SECRET
import discord
from discord.ext import commands


class MyClient(discord.Client):
    hi_list = ['!gd', '!ㅎㅇ','!하이', '!hi']

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author.bot:
            return None

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        if message.content in self.hi_list:
            channel = message.channel
            msg = "ㅎㅇㅎㅇㅎㅇㅎㅇㅎㅇ"
            await channel.send(msg)
            return None


client = MyClient()
client.run(SECRET['DISCORD_BOT_TOKEN'])

# import os
#
# import discord
# from dotenv import load_dotenv
#
# load_dotenv()
# TOKEN = os.getenv('ODMwNjc5MTA2MTA2Mjk0MzEy.YHKMNA.ubAyUOME-xHqYC5-gqhqiYuArrE')
#
# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#
# client.run(TOKEN)


# import discord
#
# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')
#
# client.run('ODMwNjc5MTA2MTA2Mjk0MzEy.YHKMNA.jf-8YbkaOCodfIbBVmEE7LBjN-U')

# import discord
#
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))
#
#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))
#
# client = MyClient()
# client.run('ODMwNjc5MTA2MTA2Mjk0MzEy.YHKMNA.jf-8YbkaOCodfIbBVmEE7LBjN-U')