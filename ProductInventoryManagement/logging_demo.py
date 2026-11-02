import logging

logging.basicConfig(
   filename="application.log",
   level=logging.DEBUG,
   format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def process_order(order_id, amount):
   logger.info("Processing order %s", order_id)

   if amount <= 0:
       logger.error("Order %s has an invalid amount: %s", order_id, amount)
       return False

   if amount < 100:
       logger.warning("Order %s has a low order amount: %s", order_id, amount)

   logger.debug("Validating order amount for order %s", order_id)
   logger.info("Order %s processed successfully", order_id)
   return True


process_order("ORD101", 1500)
process_order("ORD102", 50)
process_order("ORD103", -10)