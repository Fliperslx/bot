import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Вставьте сюда ваш токен
TOKEN = '7943331459:AAF--6Dwka3wqc1Yv3D0CBlv-LAzGZ4ecNs'
# ID пользователя, которому будете пересылать видео
TARGET_USER_ID = '763813580'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Здравствуйте! Отправьте мне видео с текстом, и я перешлю его.')

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    video = update.message.video
    text = update.message.caption if update.message.caption else ''

    if video and text:
        await context.bot.send_video(chat_id=TARGET_USER_ID, video=video.file_id, caption=text)
        await update.message.reply_text('Видео с текстом переслано!')
    elif video and not text:
        await update.message.reply_text('Отправлено видео без текста. Пожалуйста, добавьте текст и повторите попытку.')
    elif not video and text:
        await update.message.reply_text('Отправлено только текстовое сообщение. Пожалуйста, отправьте видео и добавьте подпись')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_video))  # Обработка текстовых сообщений

    application.run_polling()

if __name__ == '__main__':
    main()




