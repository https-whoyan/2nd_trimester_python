import asyncio
import logging
import sys

from src.bot.bot import botMain


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(botMain())
