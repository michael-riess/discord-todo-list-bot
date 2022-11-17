import os
from discord import Client
from discord.ext import commands
from discord.ext.commands import Context
from keep_alive import keep_alive
from channel import *
from guild import *
from notebook import notebook

client = Client()
# make prefix an environment variable
bot = commands.Bot(command_prefix="/")

@bot.group(fallback="help")
async def todo(ctx: Context, command):
    await ctx.send(f'Unknown command "{command}"')
    await ctx.send(f'Type "/todo help" for a list of all commands')


@todo.command()
async def help(ctx: Context):
    await ctx.send(f'NOT YET IMPLEMENTED!')

@todo.command()
async def createlist(ctx: Context, label: str):
    # TODO: see if this permissions check can be abstracted out ot a decorator that mangages role gating / throw permission error
    if ctx.message.author.guild_permission.manage_messages:
        # create channel
        new_list_channel = await create_text_channel(ctx.guild, label)
        # add channel to list table
        channel_id = ''
        notebook.create_list(new_list_channel.id, label)

@todo.command()
async def additem(ctx: Context, label):
    notebook.add_item()

@todo.command()
async def removeitem(ctx: Context, label):
    notebook.remove_item()

# TODO: determine if it should be completeitem instead
@todo.command()
async def crossitem(ctx: Context, label):
    notebook.cross_item()


# ========================================================
# Executes whenever bot goes live in server
# ========================================================
async def process_command(message):
    text = message.content.split('/todo ', 1)[1]
    if text.startswith('set-language'):
        code = text.split('set-language ', 1)[1]

        if code == 'none':
            old_code = get_channel_lang(message.channel.id)
            try:
                remove_channel_lang(message.channel.id)
                await say(message.channel, "I am no longer enforcing [language]-only use for this channel.", [locales.languages[old_code]])
            except:
                print('Error occurred while removing channel language')

        elif code == None or Language.get(code).is_valid() == False:
            await say(message.channel, "I'm sorry, that doesn't seem to be a valid language.")
        else:
            code = standardize_tag(code)
            set_channel_lang(message.channel.id, code)
            await say(message.channel, "I am now enforcing [language]-only use for this channel.", [locales.languages[code]])
    else:
        await say(message.channel, "I'm sorry, I didn't recognize that command.")


# --------------------------------------------------------
# handlers
# --------------------------------------------------------

# ========================================================
# Executes whenever bot goes live in server
# ========================================================
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# ========================================================
# Executes whenever a message is sent in discord server
# ========================================================
@client.event
async def on_message(message):
    # ignore bot's own messages
    if message.author == client.user:
        return

    # handle bot command
    elif message.content.startswith('/todo'):
        await process_command(message)

# --------------------------------------------------------
# init
# --------------------------------------------------------
keep_alive()
client.run(os.getenv('DISCORD_BOT_TOKEN'))