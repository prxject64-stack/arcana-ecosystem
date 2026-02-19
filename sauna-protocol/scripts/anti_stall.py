import discord
import os
from discord.ext import tasks

TOKEN = os.getenv('DISCORD_TOKEN')

class AntiStall(discord.Client):
    async def on_ready(self):
        print(f"WAR ROOM ACTIVE. MONITORING FOR COUNCIL STALL TACTICS.")

    async def on_message(self, message):
        if any(word in message.content.lower() for word in ["limit", "bank", "wire", "fednow", "delay"]):
            with open("stall_tactics.log", "a") as f:
                f.write(f"[{message.created_at}] {message.author}: {message.content}\n")
            print(f"!!! STALL DETECTED: {message.author} is making excuses !!!")

client = AntiStall(intents=discord.Intents.default())
client.run(TOKEN)
