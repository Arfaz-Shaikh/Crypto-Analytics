import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.error("Database connection failed.")
logger.warning("Missing values found in current_price.")
from config.logging_config import logger
logger.info("Data loaded successfully!")

