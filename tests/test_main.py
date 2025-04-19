import pytest
from OptimalCenterFinder import (
    calculate_square_corners,
    attempt_clipboard_center
)

def test_calculate_square_corners_odd():
    center = (0, 64, 0)
    size = 5  # odd
    expected = ((-2, 64, -2), (2, 64, 2))
    result = calculate_square_corners(center, size)
    assert result == expected

def test_calculate_square_corners_even():
    center = (10, 70, -5)
    size = 4  # even
    expected = ((8, 70, -7), (12, 70, -3))
    result = calculate_square_corners(center, size)
    assert result == expected

def test_clipboard_center_valid(monkeypatch):
    monkeypatch.setattr("pyperclip.paste", lambda: "123, 64, -321")
    result = attempt_clipboard_center()
    assert result == (123, 64, -321)

def test_clipboard_center_valid_with_spaces(monkeypatch):
    monkeypatch.setattr("pyperclip.paste", lambda: "123 64 -321")
    result = attempt_clipboard_center()
    assert result == (123, 64, -321)

def test_clipboard_center_invalid(monkeypatch):
    monkeypatch.setattr("pyperclip.paste", lambda: "hello world")
    result = attempt_clipboard_center()
    assert result is None

def test_clipboard_empty(monkeypatch):
    monkeypatch.setattr("pyperclip.paste", lambda: "")
    result = attempt_clipboard_center()
    assert result is None
