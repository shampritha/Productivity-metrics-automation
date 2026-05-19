import pandas as pd

from config.config import (
    INPUT_FILE,
    OUTPUT_FILE
)

from utils.excel_reader import ExcelReader
from utils.data_processor import DataProcessor
from utils.formatter import Formatter
from utils.chart_generator import ChartGenerator


def main():

    print(
        "Starting Standup Metrics Automation"
    )

    # Read Excel
    df = ExcelReader.read_excel(INPUT_FILE)

    if df is None:

        print("Input file failed")

        return

    # Process Data
    summary, productivity = (
        DataProcessor.generate_summary(df)
    )

    # Save Report
    with pd.ExcelWriter(
            OUTPUT_FILE,
            engine='openpyxl'
    ) as writer:

        summary.to_excel(
            writer,
            sheet_name="Ticket Summary"
        )

        productivity.to_excel(
            writer,
            sheet_name="Productivity"
        )

    print("Excel report generated")

    # Apply Formatting
    Formatter.format_excel(OUTPUT_FILE)

    # Generate Chart
    ChartGenerator.generate_chart(
        productivity
    )

    print("Automation completed")


if __name__ == "__main__":

    main()