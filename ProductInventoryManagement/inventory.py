"""Core functions for a simple product inventory management system."""

import logging

logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def calculate_total_price(price: float, quantity: int) -> float:
    """Return the total price for a product and quantity."""
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        logger.error("Invalid price type: %r", price)
        raise TypeError("price must be a number")
    if price < 0:
        logger.error("Negative price supplied: %s", price)
        raise ValueError("price cannot be negative")
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        logger.error("Invalid quantity type: %r", quantity)
        raise TypeError("quantity must be an integer")
    if quantity <= 0:
        logger.error("Invalid quantity supplied: %s", quantity)
        raise ValueError("quantity must be greater than zero")

    total = price * quantity
    logger.info("Calculated total price: %.2f", total)
    return total


def apply_discount(total: float, discount_percent: float) -> float:
    """Return the total after applying a percentage discount."""
    if isinstance(total, bool) or not isinstance(total, (int, float)):
        logger.error("Invalid total type: %r", total)
        raise TypeError("total must be a number")
    if total < 0:
        logger.error("Negative total supplied: %s", total)
        raise ValueError("total cannot be negative")
    if isinstance(discount_percent, bool) or not isinstance(
        discount_percent, (int, float)
    ):
        logger.error("Invalid discount type: %r", discount_percent)
        raise TypeError("discount_percent must be a number")
    if not 0 <= discount_percent <= 100:
        logger.error("Discount outside valid range: %s", discount_percent)
        raise ValueError("discount_percent must be between 0 and 100")

    discounted_total = total - (total * discount_percent / 100)
    logger.info(
        "Applied %.2f%% discount; final total: %.2f",
        discount_percent,
        discounted_total,
    )
    return discounted_total


def check_stock(available_stock: int, requested_quantity: int) -> bool:
    """Return True when enough stock is available; otherwise return False."""
    for name, value in (
        ("available_stock", available_stock),
        ("requested_quantity", requested_quantity),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            logger.error("Invalid %s type: %r", name, value)
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            logger.error("Negative %s supplied: %s", name, value)
            raise ValueError(f"{name} cannot be negative")

    if requested_quantity == 0:
        logger.error("Requested quantity must be greater than zero")
        raise ValueError("requested_quantity must be greater than zero")

    is_available = available_stock >= requested_quantity
    logger.info(
        "Stock check: available=%d, requested=%d, result=%s",
        available_stock,
        requested_quantity,
        is_available,
    )
    return is_available
