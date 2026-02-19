import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class ShadowClient(discord.Client):
    async def on_ready(self):
        print(f'VAMPIRE SCOUT ACTIVE. Monitoring for April 30th Decay risk.')

    async def on_message(self, message):
        if any(word in message.content.lower() for word in ["jones", "10m", "redemption"]):
            with open("council_shadow.log", "a") as f:
                f.write(f"[{message.created_at}] {message.author}: {message.content}\n")
            print(f"!!! ALERT: COUNCIL MENTIONED TARGET !!!")

intents = discord.Intents.default()
intents.message_content = True
client = ShadowClient(intents=intents)
client.run(TOKEN)
