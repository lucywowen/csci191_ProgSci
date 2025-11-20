# Challenge 4 – Simple Text Analyzer

## Goal
Read a text file, count word frequencies (case-insensitive, basic punctuation removed),
and print the top N words.

## Your Tasks
- Normalize text by lowercasing and removing punctuation like .,!?:; (basic is fine).
- Count word frequencies.
- Implement `top_n_words(filepath, n)` returning a list of (word, count).
- Handle empty files and N > number of distinct words.

## Usage
```bash
python starter.py data/input.txt 3
```
