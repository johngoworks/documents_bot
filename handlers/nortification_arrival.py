from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from states.arrival import Arrival_transfer
from states.passport_manual import PassportManualStates

from keyboards.nortification_arrival import *

from localization import _
from data_manager import SecureDataManager

nortification_arrival = Router()
data_manager = SecureDataManager()


@nortification_arrival.callback_query(F.data == "doc_migration_notice")
async def arrival_start(callback: CallbackQuery, state: FSMContext):
    """Обработка нажатия кнопки по миграционному учету"""

    # Установка состояния
    await state.set_state(Arrival_transfer.waiting_confirm_start)
    state_data = await state.get_data()
    lang = state_data.get("language")
    await state.update_data(from_action="")
    text = f"{_.get_text('startarrival.title', lang)}\n{_.get_text('startarrival.description', lang)}"
    # Отправка сообщения с клавиатурой ожидания подтверждения
    await callback.message.edit_text(
        text=text,
        reply_markup=kbs_start_arrival(lang),
    )