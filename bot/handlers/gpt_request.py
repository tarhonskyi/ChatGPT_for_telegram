from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from utils.openai_gpt.gpt_request import generate_turbo_response

router = Router()


@router.message(Command(commands="gpt"))
async def echo(message: Message, command: CommandObject):
    request = generate_turbo_response(f"{command.args}")
    await message.answer(f"GPT: '{request}'")
