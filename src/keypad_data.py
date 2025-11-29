from typing import List, Tuple

def get_keypad_data() -> List[Tuple[int, int, str]]:
    """
    Create and return a list of tuples representing keypad data with coordinates.
    
    This function generates coordinate-based data for a 4x5 keypad containing 
    letters and numbers. Each tuple contains (row, column, value) representing
    the position and content at that coordinate.
    """

    grid_rows = [
        ["A", "B", "C", "D", "E"],    # Row 1: Letters A-E
        ["F", "G", "H", "I", "J"],    # Row 2: Letters F-J  
        ["K", "L", "M", "N", "O"],    # Row 3: Letters K-O
        ["", "1", "2", "3", ""]       # Row 4: Numbers 1-3 with empty corners
    ]

    coordinate_data = []
    for row_idx, row_data in enumerate(grid_rows, start=1):
        for col_idx, cell_value in enumerate(row_data, start=1):
            coordinate_data.append((row_idx, col_idx, cell_value))

    return coordinate_data


if __name__ == "__main__":
    data = get_keypad_data()
    print(f"Loaded keypad data with {len(data)} coordinates")
