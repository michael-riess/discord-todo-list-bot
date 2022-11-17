from discord import Guild

# ========================================================
# Creates channel of given name in guild (server)
# TODO: error handeling
# TODO: channel name prefixes or suffixes?
# ========================================================
async def create_text_channel(guild: Guild, channel_name: str):
    channel = await guild.create_text_channel(channel_name)
    return channel