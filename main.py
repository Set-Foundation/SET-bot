import discord
from discord.ext import commands
import dotenv
from keep_alive import *

'''
SET Bot

By Mingde Yin (Itchono)

v1.1 June 4, 2020

Changelog:
1.1 - Higher Uptime
1.0 - Initial Release
'''

EULA_CHANNEL = 715709951007522878
# EULA Channel

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')  # bot token; kept private

client = commands.Bot(command_prefix="$")

client.add_cog(SelfPing(client))

@client.command()
async def info(ctx : commands.Context):
    '''
    Shows information about the bot
    '''
    await ctx.send("I am SET BOT")

@client.command()
async def numberof(ctx: commands.Context, role: discord.Role):
    '''
    Gets the number of users with a certain role
    '''
    await ctx.send(f"{len(role.members)} members have the \"{role.name}\" role.")


async def participantRole(guild: discord.Guild):
    '''
    Gets the role named "Participant"
    '''

    '''
    for role in guild.roles:
        if role.name == "Participant": return role
    return None
    ''' # previous method

    return discord.utils.get(guild.roles, name="Participant") # more elegant method


@client.event
async def on_message(message : discord.Message):
    if message.channel.id == EULA_CHANNEL and message.author != client.user:
        if message.content.lower() == "i agree":
            m = message.author
            roles = m.roles
            roles.append(await participantRole(message.guild))
            await m.edit(roles=roles)
            await message.channel.send("Thanks {}, your role has been added!".format(message.author.mention))

    await client.process_commands(message)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("SET Hacks!"))
    # change status when bot is loaded
        
keep_alive() # start internal server to keep bot loaded
client.run(TOKEN) # log into Discord
