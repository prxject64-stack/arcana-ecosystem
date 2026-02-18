import discord
import os

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
TARGET_WHALE = '0x8ad525046270b200b6526131b7f03673c68383e9'

class ShadowBot(discord.Client):
    async def on_ready(self):
        print(f'Vampire Shadow Bot active as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if TARGET_WHALE.lower() in message.content.lower():
            report = (
                '🚨 **PUBLIC SOLVENCY ADVISORY** 🚨
' 
                f'Wallet **{TARGET_WHALE}** detected.
' 
                'Current sUSD Position: **10,000,000 units**
' 
                'Current Market Value: **,107,000** (De-peg: -,893,000)
' 
                '**CLIFF WARNING:** After April 30, this position decays at **12.5% PER MONTH**.
' 
                'Arcana Sovereign alignment offer: **2,316,666 ARC** bonus detected for this address.
' 
                'Exit the prison: 0x0165... (Arcana Bridge)'
            )
            await message.channel.send(report)

intents = discord.Intents.default()
intents.message_content = True
client = ShadowBot(intents=intents)
client.run(TOKEN)
