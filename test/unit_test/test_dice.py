"""Make test for function dice."""
from unittest import mock

from src import dice


@mock.patch("src.dice.dice_roll")
@mock.patch("src.dice.print_value")
def test_main_good_choice(mock_print_value, mock_dice_roll, monkeypatch):
    """Test main."""
    monkeypatch.setattr("builtins.input", lambda _: "6")
    mock_dice_roll.return_value = 5
    result = dice.main()
    assert result is None


def test_main_bad_choice(monkeypatch):
    """Test main."""
    monkeypatch.setattr("builtins.input", lambda _: "5")
    result = dice.main()
    assert result == 1


def test_print_value():
    """Test final print value."""
    mock_dice_value = 6
    result = dice.print_value(mock_dice_value)
    assert result is None


@mock.patch("src.dice.random")
def test_dice_roll(mock_random):
    """Test function dice_roll."""
    mock_type_of_dice = 6
    mock_random.randint.return_value = 5
    result = dice.dice_roll(mock_type_of_dice)
    assert result == 5
