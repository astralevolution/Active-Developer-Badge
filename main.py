import discord
import os
from discord import Embed, app_commands
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents, heartbeat_timeout=60)
TOKEN = os.getenv('DISCORD_TOKEN')  
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Active Develpoer Badge"))

@bot.hybrid_command(
    name="activedevbadge",
    description="Complete the requirements for the Active Developer Badge!")
async def activedevbadge(ctx):
  embed = discord.Embed(title="Active Developer Badge", color=0x03a64b)
  embed.set_thumbnail(url=bot.user.avatar.url)
  embed.set_footer(text="Requirement Met Successfully.")
  embed.add_field(
      name="Command Successful!",
      value=
      "Now that a command has been ran, you can now claim the Active Developer Badge! Claim it at https://discord.com/developers/active-developer",
      inline=False)

  await ctx.send(embed=embed)

bot.run(TOKEN)
