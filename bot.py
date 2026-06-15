import os
import joblib

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

load_dotenv()

TOKEN = os.getenv(
    "BOT_TOKEN"
)

model = joblib.load(
    "news_classifier.pkl"
)


async def classify(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    pred = model.predict(
        [text]
    )[0]

    if pred == "sport":
        answer = "🏆 Սպորտային լուր"
    else:
        answer = "🏛️ Քաղաքական լուր"

    await update.message.reply_text(
        answer
    )


app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

app.add_handler(
    MessageHandler(
        filters.TEXT,
        classify
    )
)

print("BOT STARTED")

app.run_polling()