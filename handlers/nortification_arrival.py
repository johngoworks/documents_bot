from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext


from localization import _
from data_manager import SecureDataManager

nortification_arrival = Router()
data_manager = SecureDataManager()