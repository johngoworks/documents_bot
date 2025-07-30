from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from states.passport_manual import PassportManualStates

from localization import _
from data_manager import SecureDataManager

passport_manual_router = Router()
data_manager = SecureDataManager()


@passport_manual_router.callback_query(F.data == "passport_manual_start")
async def handle_passport_manual_start(callback: CallbackQuery, state: FSMContext):
    """Handle the start of manual passport input."""

    # Set the state for manual passport handling
    await state.set_state(PassportManualStates.full_name_input)

    # Get the user's language preference from state data
    state_data = await state.get_data()
    lang = state_data.get("language")
    passport_title = state_data.get("passport_title", "")

    # Prepare the initial message for manual passport input
    text = f"{_.get_text(passport_title, lang)}\n\n{_.get_text('passport_manual_full_name.description', lang)}"

    # Update the state with the action context
    await state.set_state(PassportManualStates.birth_date_input)
    # Send the initial message to the user
    await callback.message.edit_text(
        text=text, reply_markup=None  # No keyboard for this step
    )


@passport_manual_router.message(PassportManualStates.birth_date_input)
async def request_birth_date_input(message: Message, state: FSMContext):
    """Handle the input of the birth date in manual passport handling."""
    passport_data = {}
    full_name = message.text.strip()
    passport_data["full_name"] = full_name
    # Get the user's language preference from state data
    state_data = await state.get_data()
    lang = state_data.get("language")
    # Update the state with the full name
    await state.update_data(passport_data=passport_data)
    user_data = {
        "passport_data": passport_data,
    }
    session_id = state_data.get("session_id")
    data_manager.save_user_data(message.from_user.id, session_id, user_data)

    text = f"{_.get_text("passport_manual_birth_date.title", lang)}\n{_.get_text("passport_manual_birth_date.example_text", lang)}"
    await message.answer(text=text, reply_markup=None)  # No keyboard for this step
    # Move to the next state
    await state.set_state(PassportManualStates.citizenship_input)


@passport_manual_router.message(PassportManualStates.citizenship_input)
async def handle_birth_date_input(message: Message, state: FSMContext):
    """Handle the input of the birth date in manual passport handling."""
    passport_data = await state.get_data()
    passport_data = passport_data.get("passport_data")
    birth_date = message.text.strip()
    passport_data["birth_date"] = birth_date

    # Get the user's language preference from state data
    state_data = await state.get_data()
    lang = state_data.get("language")

    # Update the state with the birth date
    await state.update_data(passport_data=passport_data)
    user_data = {
        "passport_data": passport_data,
    }
    session_id = state_data.get("session_id")
    data_manager.save_user_data(message.from_user.id, session_id, user_data)

    text = f"{_.get_text('passport_manual_citizenship.title', lang)}\n{_.get_text('passport_manual_citizenship.example_text', lang)}"
    await message.answer(text=text, reply_markup=None)

    await state.set_state(PassportManualStates.passport_serial_number_input)


@passport_manual_router.message(PassportManualStates.passport_serial_number_input)
async def handle_citizenship_input(message: Message, state: FSMContext):
    """Handle the input of the citizenship in manual passport handling."""
    passport_data = await state.get_data()
    passport_data = passport_data.get("passport_data")
    citizenship = message.text.strip()
    passport_data["citizenship"] = citizenship

    # Get the user's language preference from state data
    state_data = await state.get_data()
    lang = state_data.get("language")

    # Update the state with the citizenship
    await state.update_data(passport_data=passport_data)
    user_data = {
        "passport_data": passport_data,
    }
    session_id = state_data.get("session_id")
    data_manager.save_user_data(message.from_user.id, session_id, user_data)

    text = f"{_.get_text('passport_manual_serial_input.title', lang)}\n{_.get_text('passport_manual_serial_input.example_text', lang)}"
    await message.answer(text=text, reply_markup=None)

    await state.set_state(PassportManualStates.passport_issue_date_input)


@passport_manual_router.message(PassportManualStates.passport_issue_date_input)
async def handle_passport_serial_number_input(message: Message, state: FSMContext):
    """Handle the input of the passport serial number in manual passport handling."""
    passport_data = await state.get_data()
    passport_data = passport_data.get("passport_data")
    passport_serial_number = message.text.strip()
    passport_data["passport_serial_number"] = passport_serial_number

    # Get the user's language preference from state data
    state_data = await state.get_data()
    lang = state_data.get("language")

    # Update the state with the passport serial number
    await state.update_data(passport_data=passport_data)
    user_data = {
        "passport_data": passport_data,
    }
    session_id = state_data.get("session_id")
    data_manager.save_user_data(message.from_user.id, session_id, user_data)

    text = f"{_.get_text('passport_manual_issue_date.title', lang)}\n{_.get_text('passport_manual_issue_date.example_text', lang)}"
    await message.answer(text=text, reply_markup=None)

    await state.set_state(PassportManualStates.passport_expiry_date_input)


@passport_manual_router.message(PassportManualStates.passport_expiry_date_input)
async def handle_passport_issue_date_input(message: Message, state: FSMContext):
    """Handle the input of the passport issue date in manual passport handling."""
    passport_data = await state.get_data()
    passport_data = passport_data.get("passport_data")
    passport_issue_date = message.text.strip()
    passport_data["passport_issue_date"] = passport_issue_date

    # Get the user's language preference from state data
    state_data = await state.get_data()
    lang = state_data.get("language")

    # Update the state with the passport issue date
    await state.update_data(passport_data=passport_data)
    user_data = {
        "passport_data": passport_data,
    }
    session_id = state_data.get("session_id")
    data_manager.save_user_data(message.from_user.id, session_id, user_data)

    text = f"{_.get_text('passport_manual_expire_date.title', lang)}\n{_.get_text('passport_manual_expire_date.example_text', lang)}"
    await message.answer(text=text, reply_markup=None)

    await state.set_state(PassportManualStates.passport_issue_place_input)


@passport_manual_router.message(PassportManualStates.passport_issue_place_input)
async def handle_passport_expiry_date_input(message: Message, state: FSMContext):
    """Handle the input of the passport expiry date in manual passport handling."""
    passport_data = await state.get_data()
    passport_data = passport_data.get("passport_data")
    passport_expiry_date = message.text.strip()
    passport_data["passport_expiry_date"] = passport_expiry_date

    # Get the user's language preference from state data
    state_data = await state.get_data()
    lang = state_data.get("language")

    # Update the state with the passport expiry date
    await state.update_data(passport_data=passport_data)
    user_data = {
        "passport_data": passport_data,
    }
    session_id = state_data.get("session_id")
    data_manager.save_user_data(message.from_user.id, session_id, user_data)
    end_state = state_data.get("from_action")
    text = f"{_.get_text('passport_manual_issue_place.title', lang)}\n{_.get_text('passport_manual_issue_place.example_text', lang)}"
    await message.answer(text=text, reply_markup=None)

    await state.set_state(end_state)
