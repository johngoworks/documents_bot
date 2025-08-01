from aiogram.utils.keyboard import InlineKeyboardBuilder
from localization import _


async def kbs_start_arrival():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_.get_text("consent.agree_button", lang), callback_data="consent_agree"
    )
    builder.button(
        text=_.get_text("consent.refuse_button", lang), callback_data="consent_refuse"
    )
    builder.adjust(1)
    return builder.as_markup()