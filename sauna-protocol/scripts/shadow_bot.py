import discord
import os

TOKEN = os.getenv('DISCORD_TOKEN')
KEYWORDS = ['susd', 'sip-420', 'jubilee', 'debt trap', 'depeg']

class VampireScout(discord.Client):
    async def on_ready(self):
        print(f'Vampire Scout active: Monitoring for trapped liquidity...')

    async def on_message(self, message):
        if message.author == self.user:
            return

        content = message.content.lower()
        if any(word in content for word in KEYWORDS):
            user_id = message.author.id
            report = (
                f"🚨 **LIQUIDITY RESCUE OPPORTUNITY** 🚨\n"
                f"User <@{user_id}> is discussing trapped assets.\n"
                "**The Math:** sUSD @ $0.81 | April 30th Discount: 12.5%\n"
                "**Arcana Solution:** saUSD 1:1 Bridge + ARC Bonus.\n"
                "Safeguard your principal: `0x0165...` (Arcana Sovereign)"
            )
            await message.channel.send(report)
            print(f"[LOG] Flagged user {message.author} for migration.")

intents = discord.Intents.default()
intents.message_content = True
client = VampireScout(intents=intents)
client.run(TOKEN)
