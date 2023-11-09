# backend/tests/test_color_handler.py

from backend.app import FlipApp

def test_initial_color():
    handler = FlipApp()
    assert handler.get_current_state() == -1, "wtf???"

def test_toggle_color():
    handler = FlipApp()
    handler.update_state()
    assert handler.get_current_state() == 1, "error"

    handler.update_state()
    assert handler.get_current_state() == -1,"error"
