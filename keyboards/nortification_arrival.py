from aiogram.utils.keyboard import InlineKeyboardBuilder
from localization import _

async def kbs_start_arrival(lang = "ru"):
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_.get_text("startarrival.start_btn", lang), callback_data="consent_agree"
    )
    builder.button(
        text=_.get_text("startarrival.cancel_button", lang), callback_data="consent_refuse"
    )
    builder.adjust(1)
    return builder.as_markup()