from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from states.stamp_transfer import Stamp_transfer
from keyboards.stamp_transfer import get_waiting_confirm_stamp_transfer_start_keyboard
from localization import _
from data_manager import SecureDataManager

stamp_transfer_router = Router()
data_manager = SecureDataManager()


@stamp_transfer_router.callback_query(F.data == "doc_stamp_restoration")
async def handle_stamp_restoration(callback: CallbackQuery, state: FSMContext):
    """Обработка нажатия кнопки восстановления штампа"""

    # Установка состояния для передачи штампа
    await state.set_state(Stamp_transfer.waiting_confirm_stamp_transfer_start)
    lang = await state.get_data()
    lang = lang["language"]
    text = f"{_.get_text('stamp_transfer.title', lang)}\n{_.get_text('stamp_transfer.description', lang)}{_.get_text('stamp_transfer.documents_to_prepare', lang)}"
    # Отправка сообщения с клавиатурой ожидания подтверждения
    await callback.message.edit_text(
        text=text,
        reply_markup=get_waiting_confirm_stamp_transfer_start_keyboard(lang),
    )
