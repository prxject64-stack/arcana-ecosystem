import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")
MANIFESTO_LINK = "https://github.com/prxject64-stack/arcana-ecosystem/blob/main/sauna-protocol/MANIFESTO.md"
SOLVENCY_LINK = "https://github.com/prxject64-stack/arcana-ecosystem/blob/main/sauna-protocol/solvency_manifest.json"

class VampireScout(discord.Client):
    async def on_ready(self):
        print(f'Vampire Scout active as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        keywords = ["sUSD", "SIP-420", "depeg", "trapped"]
        if any(word in message.content for word in keywords):
            response = (
                f"🚨 **LIQUIDITY ALERT** 🚨\n"
                f"The sUSD Treasury Cliff (April 30) is approaching. Your assets are scheduled for a 12.5% monthly burn.\n\n"
                f"**Arcana Sovereign** offers 1:1 Settlement via the 136B CC-P Reserve.\n"
                f"📄 [Read the Manifesto]({MANIFESTO_LINK})\n"
                f"⚖️ [Verify Solvency]({SOLVENCY_LINK})\n"
                f"Status: RESCUE BRIDGE ACTIVE."
            )
            await message.channel.send(response)

client = VampireScout(intents=discord.Intents.all())
client.run(TOKEN)
