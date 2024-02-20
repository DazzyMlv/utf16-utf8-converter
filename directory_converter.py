"""
Batch UTF-16 to UTF-8 CSV Converter

This script defines a Python class, DirectoryConverter, that loops through all CSV files in a specified input directory,
utilizes the UTF16toUTF8Converter class to convert each UTF-16 encoded CSV file to UTF-8, and saves them in the specified
output directory.

Usage:
1. Create an instance of DirectoryConverter with input and output directory paths.
2. Call the convert_files method to perform the batch conversion.

Note: Ensure that the input directory contains only UTF-16 encoded CSV files.

Author: Dazzy Mlv <23006212+DazzyMlv@users.noreply.github.com>
Date: February 20, 2024
"""

import os

from .utf16_utf8_converter import UTF16toUTF8Converter


class DirectoryConverter:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    def convert_files(self):
        try:
            # Ensure the output directory exists, create if not
            os.makedirs(self.output_directory, exist_ok=True)

            # Loop through files in the input directory
            for filename in os.listdir(self.input_directory):
                if filename.endswith(".csv"):
                    input_path = os.path.join(self.input_directory, filename)
                    output_path = os.path.join(
                        self.output_directory,
                        f"{os.path.splitext(filename)[0]}_utf8.csv",
                    )

                    # Use UTF16toUTF8Converter to convert each file
                    converter = UTF16toUTF8Converter(input_path, output_path)
                    converter.convert()

            print("Conversion of all files in the directory completed.")
        except Exception as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    input_dir = "input_directory"
    output_dir = "output_directory"

    directory_converter = DirectoryConverter(input_dir, output_dir)
    directory_converter.convert_files()
