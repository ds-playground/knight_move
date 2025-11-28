Knight Move Analysis Project - Code Structure
=============================================

This project analyzes knight moves on a 4x5 grid keypad using pure Python.

QUICK START
-----------
To get the total number of valid paths for step 9 (sequence of 10):
    python run.py

This will output a single number representing the total valid paths.

CODE STRUCTURE
--------------
src/
├── table_data.py      - Creates the 4x5 grid coordinate data
├── positions.py       - Analyzes grid positions (vowels, missing, bounds)
├── knight_move.py     - Implements knight movement logic
├── path_create.py     - Generates multi-step knight move paths
├── path_check.py      - Validates paths against constraints
├── vowel_check.py     - Checks vowel limits in path strings

Main Files:
├── run.py            - Simple script to run step 9 analysis (USE THIS!)
├── main.py           - Comprehensive analysis with detailed output
├── knight_move_on_keypad.ipynb - Interactive Jupyter notebook

Documentation:
├── README.md         - Detailed project documentation
├── requirements.txt  - Dependencies (optional, pure Python implementation)

GRID LAYOUT
-----------
The 4x5 grid contains:
A B C D E
F G H I J
K L M N O
1 2 3 * *

Where * represents missing positions that paths must avoid.

CONSTRAINTS
-----------
- Knight moves only (L-shaped: 2+1 or 1+2 squares)
- Stay within grid boundaries
- Avoid missing positions (4,1) and (4,5)
- Maximum 2 vowel hits per path (A, E, I, O, U)

DEPENDENCIES
------------
- Python 3.9+ (standard library only)
- No external packages required for main functionality
- Optional: jupyter for interactive notebook

For more details, see README.md