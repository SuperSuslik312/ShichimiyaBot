from gpytranslate import SyncTranslator
from SayaBot.modules.language import gs
from SayaBot.modules.disable import DisableAbleCommandHandler
from SayaBot import dispatcher

def __help__(chat):
    return gs(chat, "gtranslate_help")

__mod_name__ = "Translator"

from telegram import ParseMode, Update
from telegram.ext import CallbackContext

def translate(update: Update, context: CallbackContext):
    message = update.effective_message
    trl = SyncTranslator()
    if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
        if len(message.text.split()) == 1:
            message.delete()
            return
        target = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        detectlang = trl.detect(text)
        try:
            tekstr = trl(text, targetlang=target)
        except ValueError as err:
            message.reply_text(f"Error: `{str(err)}`", parse_mode=ParseMode.MARKDOWN)
            return
    else:
        if len(message.text.split()) <= 2:
            message.delete()
            return
        target = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
        detectlang = trl.detect(text)
        try:
            tekstr = trl(text, targetlang=target)
        except ValueError as err:
            message.reply_text("Error: `{}`".format(str(err)), parse_mode=ParseMode.MARKDOWN)
            return

    message.reply_text(f"*Translated from {detectlang}:*\n```{tekstr.text}```", parse_mode=ParseMode.MARKDOWN)

TRANSLATE_HANDLER = DisableAbleCommandHandler(["tr", "tl"], translate, run_async=True)

dispatcher.add_handler(TRANSLATE_HANDLER)

__mod_name__ = "Translator"
__command_list__ = ["tr", "tl"]
__handlers__ = [TRANSLATE_HANDLER]
