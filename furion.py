import logging, os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from google import genai
from google.genai import types
from google.genai.types import GoogleSearch, Tool

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

load_dotenv()

# Gemini API Configuration
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
client = genai.Client(api_key=GOOGLE_GEMINI_API_KEY)
google_search_tool = Tool(google_search=GoogleSearch())

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    response = client.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            config=types.GenerateContentConfig(
                system_instruction="Apresente-se como Furion, um ChatBot da FURIA, focado para os fãs de CS e se apresente de acordo."
            ),
            contents=types.Content(
                role="user",
                parts=[types.Part.from_text(text=f"Olá, meu nome é {user}")]
            )
        )
    await update.message.reply_text(response.text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

async def generate_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            config=types.GenerateContentConfig(
                system_instruction="Seu nome é FURION. Você é um assistente virtual para o time da Fúria. O usuário vai conversar com você sobre a organização, responda de forma amigável, utilizando alguns emojis no final em algumas mensagens. Utilize a wikipedia nas suas pesquisas. Ao final das respostas indique uma das fontes utilizadas.",
                tools=[google_search_tool]
            ),
            contents=types.Content(
                role="user",
                parts=[types.Part.from_text(text=update.message.text)]
            )
        )
        await update.message.reply_text(response.text)
    except Exception as e:
        logger.error(f"Error generating answer: {e}")
        await update.message.reply_text("Ocorreu um erro ao gerar a resposta.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_KEY")).build()

    # commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_answer))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()