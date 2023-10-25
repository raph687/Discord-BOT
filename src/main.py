import random
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 312177765673861120  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)

@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1,6))

@bot.event
async def on_message(message):
    if message.content.lower() == "salut tout le monde":
        await message.channel.send("Salut tout seul " + message.author.mention)
    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(administrator=True)
async def admin(ctx, *, name: discord.Member = None):
    admin = discord.utils.get(ctx.guild.roles, name="Admin")

    if not admin:
        admin = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions.all())

    await name.add_roles(admin)
    await ctx.send(name.display_name + " est maintenant admin !")

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, name: discord.Member = None,*, reason=None):
    if (reason == None):
        reason = "LOL DANS LES DENTS"
    await name.ban()
    await ctx.send("Reason for ban " + reason)

@bot.command()
async def xkcd(ctx):
    await ctx.send("https://xkcd.com/" + random.randint(1, 1000).__str__())

token = ""
bot.run(token)  # Starts the bot