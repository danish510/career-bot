import discord
from discord.ext import commands
from config import DISCORD_TOKEN
from ai_handler import get_career_advice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot login sebagai {bot.user}")

@bot.command()
async def career(ctx, *, cerita=None):

    if cerita is None:
        await ctx.send(
            "Silakan ceritakan minat kamu setelah command.\n\n"
            "Contoh:\n"
            "!career saya suka teknologi dan matematika"
        )
        return

    await ctx.send("Sedang menganalisis dengan AI...")

    try:
        response = get_career_advice(cerita)

        if len(response) > 2000:
            response = response[:1990] + "..."

        await ctx.send(response)

    except Exception as e:
        print(e)
        await ctx.send("Terjadi kesalahan saat mengambil saran karir.")

bot.run(DISCORD_TOKEN)
