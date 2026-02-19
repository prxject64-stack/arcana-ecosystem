import discord
import os

# Use environment variable for security
TOKEN = os.getenv('DISCORD_TOKEN')

class IDScanner(discord.Client):
    async def on_ready(self):
        print(f"--- SCANNING SERVER: {self.user} ---")
        for guild in self.guilds:
            print(f"GUILD: {guild.name} (ID: {guild.id})")
            for channel in guild.text_channels:
                print(f"  #{channel.name} | ID: {channel.id}")
        await self.close()

client = IDScanner(intents=discord.Intents.default())
client.run(TOKEN)
