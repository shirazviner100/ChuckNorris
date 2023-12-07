from chuck_norris_jokes import chuck_norris_jokes
from typing import Final
from  telegram_bot import telegram_bot 
from translation import translate


TOKEN : Final = "6645809775:AAEUDxtb2_jxSJ-BuDwLzrcNRiLbwsg_yOw"
BOT_USERNAME : Final = "@ChuckNorrisExercise_bot"
JOKES = chuck_norris_jokes.get_chuck_norris_jokes()


if __name__ == '__main__':
    my_bot = telegram_bot(TOKEN, BOT_USERNAME, JOKES)
    my_bot.starting_bot()
