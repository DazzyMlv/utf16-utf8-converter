# Batch UTF-16 to UTF-8 CSV Converter

This Python script allows you to batch convert UTF-16 encoded CSV files to UTF-8 in a specified input directory, saving the converted files in an output directory.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/DazzyMlv/utf16-utf8-converter.git
   ```

2. Clone the repository:

   ```bash
   cd utf16-utf8-converter
   ```

3. Run the script with the following command, replacing <input_directory> and <output_directory> with your actual directory paths:

   ```bash
   python converter.py --input_dir <input_directory> --output_dir <output_directory>

   ```

   Example:

   ```bash
   python converter.py --input_dir input_data --output_dir output_data

   ```

## Requirements

- [Python 3.x](https://www.python.org/)

## Script Details

- The script uses the argparse module to accept input and output directories from the command line.
- It includes a UTF16toUTF8Converter class for converting individual CSV files.
- The DirectoryConverter class loops through all CSV files in the input directory and utilizes the UTF16toUTF8Converter class for batch conversion.

## Author

Dazzy Mlv <23006212+DazzyMlv@users.noreply.github.com>

## License

This project is licensed under the [MIT License](LICENSE).
