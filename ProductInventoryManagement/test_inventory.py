"""Tests for the product inventory management functions."""

import pytest

from inventory import apply_discount, calculate_total_price, check_stock


def test_calculate_total_price_valid() -> None:
    assert calculate_total_price(100, 3) == 300


def test_calculate_total_price_rejects_negative_price() -> None:
    with pytest.raises(ValueError, match="price cannot be negative"):
        calculate_total_price(-10, 2)


def test_calculate_total_price_rejects_non_integer_quantity() -> None:
    with pytest.raises(TypeError, match="quantity must be an integer"):
        calculate_total_price(10, 2.5)


def test_apply_discount_valid() -> None:
    assert apply_discount(1000, 10) == 900


def test_apply_discount_rejects_invalid_percentage() -> None:
    with pytest.raises(ValueError, match="between 0 and 100"):
        apply_discount(1000, 120)


def test_check_stock_available() -> None:
    assert check_stock(10, 4) is True


def test_check_stock_insufficient() -> None:
    assert check_stock(2, 5) is False


def test_check_stock_rejects_negative_stock() -> None:
    with pytest.raises(ValueError, match="available_stock cannot be negative"):
        check_stock(-1, 2)
