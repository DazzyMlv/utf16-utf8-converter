"""
Batch UTF-16 to UTF-8 CSV Converter

This script defines a Python class, DirectoryConverter, that loops through all CSV files in a specified input directory,
utilizes the UTF16toUTF8Converter class to convert each UTF-16 encoded CSV file to UTF-8, and saves them in the specified
output directory.

Usage:
python .\converter.py --input_dir <input_directory> --output_dir <output_directory>

Note: Ensure that the input directory contains only UTF-16 encoded CSV files.

Author: Dazzy Mlv <23006212+DazzyMlv@users.noreply.github.com>
Date: February 20, 2024
"""

import argparse
import csv
import os


class UTF16toUTF8Converter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        try:
            with open(self.input_file, "r", encoding="utf-16") as utf16_file:
                # Read CSV using utf-16 encoding
                reader = csv.reader(
                    utf16_file, delimiter="\t"
                )  # Update delimiter if needed

                # Write CSV using utf-8 encoding
                with open(
                    self.output_file, "w", encoding="utf-8", newline=""
                ) as utf8_file:
                    writer = csv.writer(utf8_file)

                    for row in reader:
                        writer.writerow(row)

            print(
                f"Conversion from {self.input_file} to {self.output_file} successful."
            )
        except Exception as e:
            print(f"Error: {e}")


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


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Batch UTF-16 to UTF-8 CSV Converter")

    # Add input directory argument
    parser.add_argument(
        "--input_dir",
        required=True,
        help="Path to the input directory containing UTF-16 encoded CSV files.",
    )

    # Add output directory argument
    parser.add_argument(
        "--output_dir",
        required=True,
        help="Path to the output directory where converted UTF-8 CSV files will be saved.",
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Create DirectoryConverter instance and perform conversion
    directory_converter = DirectoryConverter(args.input_dir, args.output_dir)
    directory_converter.convert_files()


# Run the script if executed directly
if __name__ == "__main__":
    main()
