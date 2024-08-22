
# 0x04. UTF-8 Validation

## Project Overview

The "0x04. UTF-8 Validation" project aims to validate whether a given dataset represents valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. The validation involves checking if the byte sequences conform to UTF-8 encoding rules.

## Concepts Covered

- **Bitwise Operations:** Manipulating bits using AND, OR, XOR, NOT operations, and bit shifts.
- **UTF-8 Encoding Scheme:** Understanding how characters are encoded into one or more bytes and recognizing valid byte patterns.
- **Data Representation:** Working with data at the byte level and simulating byte data.
- **List Manipulation:** Iterating through lists and accessing elements.
- **Boolean Logic:** Applying logical operations for decision-making.

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/utf-8-validation.git
   cd utf-8-validation
   ```

2. **Run the Validation Script:**

   Make sure you have Python 3.x installed. Run the following command:

   ```bash
   python validate_utf8.py <input_file>
   ```

   Replace `<input_file>` with the path to your file containing the byte sequences to validate.

## Example

If you have a file `input.txt` with the following content:

```
0xE2 0x82 0xAC
```
