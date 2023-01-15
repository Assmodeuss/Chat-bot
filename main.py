import discord
from discord.ext import commands, tasks
import os
import aiohttp
import requests
import json

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()

        super().__init__(command_prefix=commands.when_mentioned_or(">"), intents=intents)
        async def on_ready(self):
            print("Chat module is up and running")
            print("-------------------------------")

ai_chat = Bot()
api_key = os.environ.get('API_KEY')

@ai_chat.event
async def on_message(message):
  if message.channel.id == 1060675394585505904 and not message.author.id == ai_chat.application_id: #use ur channel id
    try:
        headers = {"Authorization": api_key}
        params = {"user_id": message.author.id, "message": message.content}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get("https://v6.rsa-api.xyz/ai/response", params=params) as resp:
                json_response = await resp.json()
                message1 = json_response["message"]
                msg = await message.reply(message1)
    except Exception as e:
      msg = await message.reply(e)


ai_chat.run(os.environ.get('TOKEN'))
