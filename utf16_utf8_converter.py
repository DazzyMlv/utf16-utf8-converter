"""
UTF-16 to UTF-8 CSV Converter

This script defines a Python class, UTF16toUTF8Converter, that converts a UTF-16 encoded CSV file to UTF-8 encoding.
The class takes the input and output file names as parameters and provides a convert method for the conversion process.

Usage:
1. Create an instance of UTF16toUTF8Converter with input and output file names.
2. Call the convert method to perform the conversion.

Note: Update the delimiter parameter in csv.reader based on your CSV file format.

Author: Dazzy Mlv <23006212+DazzyMlv@users.noreply.github.com>
Date: February 20, 2024
"""

import csv


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


# Example usage
if __name__ == "__main__":
    input_csv = "input_utf16.csv"
    output_csv = "output_utf8.csv"

    converter = UTF16toUTF8Converter(input_csv, output_csv)
    converter.convert()
