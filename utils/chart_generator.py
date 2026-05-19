import os
import matplotlib.pyplot as plt


class ChartGenerator:

    @staticmethod
    def generate_chart(productivity):

        # Get current project directory
        current_dir = os.getcwd()

        # Create reports folder path
        reports_path = os.path.join(current_dir, "reports")

        # Create folder if missing
        os.makedirs(reports_path, exist_ok=True)

        # Generate chart
        productivity.plot(kind="bar")

        plt.title("Team Productivity")

        # Full image path
        image_path = os.path.join(
            reports_path,
            "team_productivity.png"
        )

        # Save chart
        plt.savefig(image_path)

        print(f"Chart saved at: {image_path}")