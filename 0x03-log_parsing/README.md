# 0x03. Log Parsing

## Overview

This repository contains my solution for the "0x03. Log Parsing" project, where I applied my Python programming skills to parse and process real-time data streams. The project involved reading data from standard input (stdin), extracting specific information, performing calculations, and handling various edge cases such as exceptions and interruptions.

## Learning Objectives

In this project, I utilized the following Python concepts and techniques:

- **File I/O in Python**: Learned how to read data line by line from `sys.stdin` to process incoming data streams.
- **Signal Handling**: Implemented signal handling to manage keyboard interruptions (e.g., CTRL + C) gracefully using Python's signal module.
- **Data Processing**: Parsed strings to extract specific data points such as file sizes and HTTP status codes. Aggregated this data to compute summaries and provide meaningful output.
- **Regular Expressions**: Used regular expressions to validate the format of each line, ensuring that only correctly formatted data was processed.
- **Dictionaries in Python**: Employed dictionaries to count occurrences of HTTP status codes and accumulate the total file size processed.
- **Exception Handling**: Handled potential exceptions that could arise during file reading, data processing, and type conversions.

## Project Structure

The project is structured as follows:

- **`log_parser.py`**: The main script that reads from stdin, processes each line of input, and outputs the required summary statistics.
- **`test_logs.txt`**: Sample log file for testing the script.

## How It Works

The script processes log entries in real-time, each formatted as follows:

```
<IP Address> - [<Date>] "GET /path HTTP/1.1" <Status Code> <File Size>
```

For each line of input:
1. The script extracts the IP address, status code, and file size using string parsing and regular expressions.
2. It aggregates the total file size and counts the occurrences of each status code.
3. Every 10 lines or upon receiving a keyboard interruption (CTRL + C), the script outputs:
   - The total file size processed.
   - A summary of the count of each status code encountered.

### Example Output

```
File size: 51234
200: 12
301: 2
404: 4
500: 1
```

## Prerequisites

To run the script, you will need:

- Python 3.x installed on your machine.
- Basic understanding of Python programming, especially related to file I/O, regular expressions, and exception handling.

## How to Run the Script

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/log_parsing.git
   cd log_parsing
   ```

2. **Run the script**:
   ```bash
   cat test_logs.txt | python3 log_parser.py
   ```
   Alternatively, you can run the script and input logs manually.

3. **Terminate with CTRL + C**: The script will output the aggregated results upon receiving an interruption signal.

## Concepts and Resources

These are the key concepts and resources that were instrumental in completing this project:

1. **File I/O in Python**:
   - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

2. **Signal Handling in Python**:
   - [Python Signal Handling](https://docs.python.org/3/library/signal.html)

3. **Data Processing**:
   - [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
   
4. **Regular Expressions**:
   - [Python Regular Expressions](https://docs.python.org/3/library/re.html)

5. **Dictionaries in Python**:
   - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

6. **Exception Handling**:
   - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Conclusion

This project was a great exercise in applying Python for real-time data processing. By leveraging a variety of Python features such as regular expressions, dictionaries, and signal handling, I was able to build a robust log parser that can handle continuous data streams and produce meaningful summaries.

---
### Author
* **Zaid Mohammed Said** - (https://github.com/zaidsaid-007)
