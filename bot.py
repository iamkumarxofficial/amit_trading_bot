import os
from telebot import TeleBot
from dotenv import load_dotenv

# Load environment variables from .env (for local testing)
load_dotenv()

# ------------------------------
# Use your own IDs and token
# ------------------------------
BOT_TOKEN = "8530682759:AAFl6kEyyl2cDe1VjrybmNTMa0qRSojHKAw"
PUBLIC_CHANNEL_ID = -1002042770573        # Your public channel: Iamkumarx Trading
VIP_CHANNEL_ID = -1002627508099           # Your VIP channel: Amit fx premium
MEMBERS_GROUP_ID = -1002537709162         # Your members group: Amit trading Members
ADMIN_USER_ID = 7027393502                # Your Telegram user ID (Crypto Journey Students)
# ------------------------------

bot = TeleBot(BOT_TOKEN)

# ===== START COMMAND =====
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    welcome_text = f"Hello @{username}! Welcome to Amit Trading Bot.\n"
    welcome_text += "You will get access to the Members group once verified.\n"
    welcome_text += "Use your referral link to invite friends!"
    bot.send_message(user_id, welcome_text)
    referral_link = f"https://t.me/{bot.get_me().username}?start={user_id}"
    bot.send_message(user_id, f"Your referral link:\n{referral_link}")

# ===== ADMIN SIGNALS =====
@bot.message_handler(commands=['signal'])
def send_signal(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.send_message(message.chat.id, "You are not authorized.")
        return
    signal_text = message.text.replace('/signal', '').strip()
    if not signal_text:
        bot.send_message(message.chat.id, "Usage: /signal <message>")
        return
    bot.send_message(PUBLIC_CHANNEL_ID, signal_text)
    bot.send_message(MEMBERS_GROUP_ID, signal_text)
    bot.send_message(VIP_CHANNEL_ID, signal_text)
    bot.send_message(message.chat.id, "Signal sent to all channels/groups!")

# ===== RUN BOT =====
print("Bot is running...")
bot.infinity_polling()
