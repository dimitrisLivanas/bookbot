# BookBot

#### BookBot is a Python script that analyzes a text file for word and character statistics. It reads a specified book file, counts the number of words, and tallies the occurrences of each alphabetical character, then generates a simple report.

#### BookBot is a guided project; part of the Back-end developer career path on [boot.dev](https://www.boot.dev)

## Features

- **Word Count**: Counts the total number of words in the text.
- **Character Frequency**: Counts the frequency of each alphabetical character, ignoring case.
- **Report Generation**: Produces a textual report showing the total word count and character frequencies.

## Usage

1. Clone the repository:
```bash
git clone https://github.com/dimitrisLivanas/bookbot.git
```

2. Navigate to the project directory:

```bash
cd bookbot
```

3. Place your book text file in the `books` directory and name it `frankenstein.txt` (or adjust the `book_path` in the code to match your file’s name).
   
4. Run the script:
```bash
python bookbot.py
```

## Code Overview

- ``main()``: The entry point of the script. Reads the book text, calculates word and character counts, and prints the report.
- ``get_num_words(text)``: Counts the number of words in the provided text.
- ``get_num_chars(text)``: Counts the occurrences of each alphabetical character (case-insensitive).
- ``get_book_text(path)``: Reads the text from a file specified by the path.
- ``convert_dict_to_list(dict)``: Converts a dictionary of character counts to a sorted list of dictionaries.
- ``print_report(path, words, list)``: Prints a report of the word count and character frequencies.

## Customization

- **Book File Path**: Adjust the `book_path` variable in the `main()` function to point to your text file if it's named differently or located elsewhere.
- **Character Case Handling**: The character counting is case-insensitive. Modify `get_num_chars()` if you need case-sensitive counts.
