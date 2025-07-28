from aiogram.utils.keyboard import InlineKeyboardBuilder
from localization import _


def get_waiting_confirm_stamp_transfer_start_keyboard(lang: str = "ru"):
    """Клавиатура ожидания подтверждения начала передачи штампа"""
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_.get_text("stamp_transfer.confirm_start_button", lang),
        callback_data="confirm_stamp_transfer_start",
    )
    builder.button(
        text=_.get_text("stamp_transfer.cancel_button", lang),
        callback_data="main_menu",
    )
    builder.adjust(1)
    return builder.as_markup()
