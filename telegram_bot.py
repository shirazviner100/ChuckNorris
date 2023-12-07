from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from translation import translate


class telegram_bot:
    """
    This class creating translator bot to making jokes by the jokes array that pass in the constractor
    The boot token and user name also passing in the constracor and the class returns the messages by the client wanted language
    """

    __TRANSATOR_API_KEY : Final = "63e4ed35528846ad8fff0817aba4cda6"
    __TRANSLATOR_ENDPOINT : Final = "https://api.cognitive.microsofttranslator.com/"
    __TRANSLATOR_LOCATION : Final = "eastus"
    __START_TEXT : Final = """Hello I`m a joking bot.
To know hot i work you can type /help"""
    __HELP_TEXT : Final = """To set the language please type set language LANGUAGE.
To get joke please enter a number.
Please note that the default language is English.
Have fun :)"""

    def __init__(self, token, bot_username, jokes_array) -> None:
        self.__token : Final = token
        self.__bot_username : Final = bot_username
        self.__language = "english"
        self.__jokes = jokes_array
        self.__change_language_message = "No problem."
        self.__error_message = f"Invalid input please enter a number in the range 1 to {len(jokes_array)} or request to change language."
        self.__error_change_language = "Invalid llanguage check if you spelled it well."
        self.__translator = translate(api_key= telegram_bot.__TRANSATOR_API_KEY, endpoint= telegram_bot.__TRANSLATOR_ENDPOINT, location= telegram_bot.__TRANSLATOR_LOCATION)

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(telegram_bot.__START_TEXT)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(telegram_bot.__HELP_TEXT)

    def get_current_language(self) -> str:
        return self.__language

    def handle_response(self, message: str) -> str:

        if len(message.split()) == 3 and 'set language' in message.lower():
            message_array = message.split()
            if self.__translator.check_if_language_in_iso(message_array[2]):
                result = self.__translator.translate(self.__change_language_message, message_array[2])
                self.__language = message_array[2]
                return result
            else:
                return self.__error_change_language

        if message.isnumeric() and int(message) > 0 and int(message) < len(self.__jokes):
            return self.__translator.translate(f"{message}.  {self.__jokes[int(message) - 1]}", self.__language)

        return self.__translator.translate(self.__error_message, self.__language)


    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_type: str = update.message.chat.type
        text: str = update.message.text.strip()

        print(f"user {update.message.chat.id} using {message_type} writing {text}")

        if message_type == 'group':
            if self.__bot_username in text:
                new_text: str = text.replace(self.__bot_username, '').strip()
                response: str = self.handle_response(new_text)
            else:
                return
        else:
            response: str = self.handle_response(text)

        print('Bot response:', response)
        await update.message.reply_text(response.encode('utf-8').decode('unicode-escape'))


    async def error(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f"Update {update} caused error: {context.error}")


    def starting_bot(self):
        print('Starting bot')

        app = Application.builder().token(self.__token).build()

        #commands
        app.add_handler(CommandHandler("start", self.start_command))
        app.add_handler(CommandHandler("help", self.help_command))

        #messages
        app.add_handler(MessageHandler(filters.TEXT, self.handle_message))

        #error
        app.add_error_handler(self.error)

        print('Polling...')
        app.run_polling(poll_interval=3)