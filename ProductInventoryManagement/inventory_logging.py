import logging

logging.basicConfig(
    filename="inventory.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def calculate_total_price(price, quantity):
    logger.info("Calculating total price")

    if not isinstance(price, (int, float)) or isinstance(price, bool):
        logger.error("Invalid product price: %s", price)
        raise TypeError("Price must be a number")

    if not isinstance(quantity, int) or isinstance(quantity, bool):
        logger.error("Invalid quantity: %s", quantity)
        raise TypeError("Quantity must be an integer")

    if price <= 0 or quantity <= 0:
        logger.error("Price and quantity must be positive")
        raise ValueError("Price and quantity must be greater than zero")

    total = price * quantity

    logger.debug("Price: %s, Quantity: %s", price, quantity)
    logger.info("Total price calculated successfully: %s", total)

    return total


def apply_discount(total, discount_percent):
    logger.info("Applying discount")

    if not isinstance(total, (int, float)) or isinstance(total, bool):
        logger.error("Invalid total amount: %s", total)
        raise TypeError("Total must be a number")

    if not isinstance(discount_percent, (int, float)) or isinstance(discount_percent, bool):
        logger.error("Invalid discount percentage: %s", discount_percent)
        raise TypeError("Discount must be a number")

    if total < 0 or not 0 <= discount_percent <= 100:
        logger.error("Invalid total or discount percentage")
        raise ValueError("Total must be non-negative and discount must be between 0 and 100")

    discount_amount = total * discount_percent / 100
    final_amount = total - discount_amount

    logger.debug("Discount amount: %s", discount_amount)
    logger.info("Discount applied successfully: %s", final_amount)

    return final_amount


def check_stock(available_stock, requested_quantity):
    logger.info("Checking product stock")

    if not isinstance(available_stock, int) or isinstance(available_stock, bool):
        logger.error("Invalid available stock: %s", available_stock)
        raise TypeError("Available stock must be an integer")

    if not isinstance(requested_quantity, int) or isinstance(requested_quantity, bool):
        logger.error("Invalid requested quantity: %s", requested_quantity)
        raise TypeError("Requested quantity must be an integer")

    if available_stock < 0 or requested_quantity <= 0:
        logger.error("Invalid stock or requested quantity")
        raise ValueError("Stock cannot be negative and requested quantity must be positive")

    if requested_quantity > available_stock:
        logger.warning(
            "Insufficient stock. Available: %s, Requested: %s",
            available_stock,
            requested_quantity,
        )
        return False

    logger.debug("Stock validation completed")
    logger.info("Stock is available")

    return True


if __name__ == "__main__":
    try:
        total = calculate_total_price(500, 2)
        print("Total Price:", total)

        final_amount = apply_discount(total, 10)
        print("Final Price after Discount:", final_amount)

        stock_status = check_stock(10, 2)
        print("Stock Available:", stock_status)

    except (TypeError, ValueError) as error:
        logger.exception("Operation failed: %s", error)
        print("Error:", error)