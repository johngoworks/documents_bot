from aiogram.fsm.state import State, StatesGroup


class Stamp_transfer(StatesGroup):
    """States for stamp transfer process"""

    waiting_confirm_stamp_transfer_start = State()
