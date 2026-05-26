import win32com.client
import os


class EmailSender:

    @staticmethod
    def send_email(
            receiver_email,
            report_file,
            chart_file
    ):

        # Open Outlook
        outlook = win32com.client.Dispatch(
            "Outlook.Application"
        )

        # Create new email
        mail = outlook.CreateItem(0)

        # Email details
        mail.To = receiver_email

        mail.Subject = (
            "Automated Standup Metrics Report"
        )

        mail.Body = f"""
Hello Team,

Please find attached today's productivity report.

Dashboard Link:
https://appuctivity-metrics-automation-osx8dr5hquejkd72pkm7ez.streamlit.app/

Regards,
Automation Framework
"""

        # Attach Excel report
        mail.Attachments.Add(
            os.path.abspath(report_file)
        )

        # Attach chart image
        mail.Attachments.Add(
            os.path.abspath(chart_file)
        )

        # Send email
        mail.Send()

        print("Email sent successfully")