# SWYNEX Python Automation Tool

## Project Title

Python File Organizer Automation Tool

## Objective

The objective of this project is to automate the repetitive task of organizing files based on their file extensions.

## Problem Statement

Manually organizing files is time-consuming and repetitive. This project uses Python to automatically identify different file types and move them into appropriate folders.

## Technologies Used

- Python
- OS module
- Shutil module
- Git
- GitHub

## Features

- Scans files automatically
- Identifies file extensions
- Creates folders automatically
- Moves files into appropriate folders
- Handles unknown file types

## How It Works

1. The program scans the test_files folder.
2. It identifies the extension of each file.
3. It matches the extension with a category.
4. It creates the required folder.
5. It moves the file into that folder.

## Example

Before running the program:

    test_files/
    ├── photo.jpg
    ├── resume.pdf
    ├── program.py
    └── song.mp3

After running the program:

    test_files/
    ├── Images/
    ├── Documents/
    ├── Python/
    └── Audio/

## How to Run

Run the following command:

    python automation.py

## Learning Outcomes

- Python file handling
- Directory management
- File organization
- Python automation
- Git and GitHub