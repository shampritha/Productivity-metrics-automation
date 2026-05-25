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

        mail.Body = """
Hello Team,

Please find attached:

1. Daily Standup Report
2. Productivity Dashboard

Generated automatically by the
Productivity Metrics Automation Framework.

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