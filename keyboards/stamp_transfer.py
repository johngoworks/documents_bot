from aiogram.utils.keyboard import InlineKeyboardBuilder
from localization import _


def get_waiting_confirm_stamp_transfer_start_keyboard(lang: str = "ru"):
    """Клавиатура ожидания подтверждения начала передачи штампа"""
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_.get_text("stamp_transfer.confirm_start_button", lang),
        callback_data="select_region_and_mvd",
    )
    builder.button(
        text=_.get_text("stamp_transfer.cancel_button", lang),
        callback_data="main_menu",
    )
    builder.adjust(1)
    return builder.as_markup()


def stamp_transfer_passport_start_keyboard(lang: str = "ru"):
    """Клавиатура для начала передачи паспорта"""
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_.get_text("stamp_transfer_passport_start.passport_photo", lang),
        callback_data="passport_photo_start",
    )
    builder.button(
        text=_.get_text("stamp_transfer_passport_start.passport_manual", lang),
        callback_data="passport_manual_start",
    )
    builder.adjust(1)
    return builder.as_markup()
