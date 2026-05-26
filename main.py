import pandas as pd
from utils.logger import logger
from utils.folder_helper import FolderHelper
from utils.email_sender import EmailSender
from utils.dashboard_capture import (
    DashboardCapture
)

from config.config import (
    INPUT_FILE,
    OUTPUT_FILE,
    RECEIVER_EMAIL
)

from utils.excel_reader import ExcelReader
from utils.data_processor import DataProcessor
from utils.formatter import Formatter
from utils.chart_generator import ChartGenerator


def main():

    try:

        FolderHelper.create_folders()

        logger.info(
            "Starting Standup Metrics Automation"
        )

        # Read Excel
        df = ExcelReader.read_excel(
            INPUT_FILE
        )

        if df is None:

            logger.error(
                "Input file loading failed"
            )

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

        logger.info(
            "Excel report generated"
        )

        # Format Excel
        Formatter.format_excel(
            OUTPUT_FILE
        )



        # Generate Chart
        # Convert DataFrame to Dictionary

        chart_data = productivity[
            "Test Cases"
        ].to_dict()

        ChartGenerator.generate_chart(
            chart_data
        )

        DashboardCapture.capture_dashboard()

        #email sender
        EmailSender.send_email(
            RECEIVER_EMAIL,
            OUTPUT_FILE,
            "reports/team_productivity.png"
        )

        logger.info(
            "Automation completed"
        )

    except Exception as e:

        logger.error(
            f"Framework execution failed: {e}"
        )


if __name__ == "__main__":

    main()