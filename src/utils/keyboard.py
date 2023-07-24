from types import SimpleNamespace
import telebot
import emoji
from utils.jsonio import read_json

message = read_json('message.json')

def create_keyboard(*keys):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	buttons = map(telebot.types.KeyboardButton, map(emoji.emojize, keys))
	markup.add(*buttons)
	return markup

keys = SimpleNamespace(
    random_connect=':bust_in_silhouette: Random Connect',
    settings=':gear: Settings',
    first=message['chat']['first_name'],
    last=message['chat']['last_name'],
)

keyboards = SimpleNamespace(
    main = create_keyboard(keys.random_connect, keys.settings),
    sender = create_keyboard(keys.first, keys.last),
)