from datetime import datetime

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

INPUT_FILE = "input/tickets.xlsx"

OUTPUT_FILE = (
    f"output/daily_report_{timestamp}.xlsx"
)

RECEIVER_EMAIL = "Anirudh-Reddy.H-K@akkodis.com"