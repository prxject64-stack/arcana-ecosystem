import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class GovClient(discord.Client):
    async def on_message(self, message):
        # Alert if a Council member replies to the Jones notice
        if message.channel.name == "governance" and any(word in message.content for word in ["10M", "Jones", "Redemption"]):
            print(f"!!! GOVERNANCE RESPONSE DETECTED !!!")
            print(f"[{message.author}]: {message.content}")
            with open("gov_response.log", "a") as f:
                f.write(f"{message.author}: {message.content}\n")

intents = discord.Intents.default()
intents.message_content = True
client = GovClient(intents=intents)
client.run(TOKEN)
