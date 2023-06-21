from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes

import config
from models import Base, TelegramLink


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # check start params
    if len(context.args) != 1:
        await update.message.reply_text("Неверные параметры")
        return

    # check link
    link_hex = context.args[0]
    session = Session()
    link = session.query(TelegramLink).filter_by(link_hex=link_hex).first()
    if not link:
        await update.message.reply_text("Аккаунт не найден")
        return

    # check user
    link.chat_id = update.message.chat_id
    session.commit()
    await update.message.reply_text("Аккаунт успешно привязан")


def main():
    application = (
        Application.builder().token(config.TELEGRAM_TOKEN).build()
    )

    dispatcher = application

    # Add handlers for the /start and message commands
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()


if __name__ == "__main__":
    engine = create_engine(config.DATABASE_URL)
    global Session
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    main()
