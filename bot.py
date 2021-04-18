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

        if message.content:
            channel = message.channel
            msg = message.content
            await channel.send(msg)
            return None


client = MyClient()
client.run(SECRET['DISCORD_BOT_TOKEN'])