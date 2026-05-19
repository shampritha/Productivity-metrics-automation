import pandas as pd


class ExcelReader:

    @staticmethod
    def read_excel(file_path):
        try:
            df = pd.read_excel(file_path) #df=dummy file
            print("Excel loaded successfully")
            return df

        except Exception as e:
            print(f"Error reading file: {e}")
            return None