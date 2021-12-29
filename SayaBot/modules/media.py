from SayaBot.modules.disable import DisableAbleCommandHandler
from SayaBot import dispatcher

from telegram.ext import CallbackContext, Filters, CommandHandler
from SayaBot.modules.language import gs

def __help__(chat):
    return gs(chat, "media_help")

__mod_name__ = "Media"
__command_list__ = ["reverse", "tts", "song", "video"]
