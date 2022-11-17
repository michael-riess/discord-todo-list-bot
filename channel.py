from replit import db
from locales import locales

# ========================================================
# Posts message to discord channel (translated according to channel)
# ========================================================
async def say(channel, message, arguments=None):
  message = locales.get(get_channel_lang(channel.id), message)
  if arguments is not None:
    await channel.send(message.format(*arguments))
  else:
    await channel.send(message)

# ========================================================
# Sets the language for the given channel
# ========================================================
def set_channel_lang(channel, code):
  db[channel] = code

# ========================================================
# Gets the language for the given channel
# ========================================================
def get_channel_lang(channel):
  try:
    return db[channel]
  except:
    return 'en'

# ========================================================
# Removes channel lanaguage association
# ========================================================
def remove_channel_lang(channel):
  if channel_has_lang(channel):
    del db[channel]

# ========================================================
# Determine if channel has language
# ========================================================
def channel_has_lang(channel):
  return channel in db.keys()