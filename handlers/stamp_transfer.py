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
    state_data = await state.get_data()
    lang = state_data["language"]
    await state.update_data(from_action="stamp_transfer_after_mvd")
    text = f"{_.get_text('stamp_transfer.title', lang)}\n{_.get_text('stamp_transfer.description', lang)}{_.get_text('stamp_transfer.documents_to_prepare', lang)}"
    # Отправка сообщения с клавиатурой ожидания подтверждения
    await callback.message.edit_text(
        text=text,
        reply_markup=get_waiting_confirm_stamp_transfer_start_keyboard(lang),
    )


@stamp_transfer_router.callback_query(F.data == "stamp_transfer_after_mvd")
async def handle_stamp_transfer_after_mvd(callback: CallbackQuery, state: FSMContext):
    """Обработка нажатия кнопки после выбора МВД для передачи штампа"""

    # Установка состояния для передачи штампа
    await state.set_state(Stamp_transfer.after_select_mvd)
    state_data = await state.get_data()
    lang = state_data["language"]
    mvd_adress = state_data.get("mvd_adress")
    session_id = state_data.get("session_id")
    user_data = {
        "mvd_adress": mvd_adress,
    }
    data_manager.save_user_data(callback.from_user.id, session_id, user_data)
