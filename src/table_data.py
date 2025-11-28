from typing import List, Tuple

def get_table_data() -> List[Tuple[int, int, str]]:
    """
    Create and return a list of tuples representing table data with coordinates.
    
    This function generates coordinate-based data for a 4x5 grid containing 
    letters and numbers. Each tuple contains (row, column, value) representing
    the position and content at that coordinate.
    
    Returns:
    --------
    List[Tuple[int, int, str]]
        A list of tuples where each tuple contains:
        - int: row coordinate (1-4)
        - int: column coordinate (1-5)
        - str: value at that position (letter, number, or empty string)
    
    Grid Layout:
    -----------
    The data represents a 4x5 grid:
    ```
      1   2   3   4   5
    1 A   B   C   D   E
    2 F   G   H   I   J
    3 K   L   M   N   O
    4     1   2   3    
    ```
    
    Examples:
    ---------
    >>> data = get_table_data()
    >>> len(data)
    20
    >>> data[0]
    (1, 1, 'A')
    >>> data[-1]
    (4, 5, '')
    
    Notes:
    ------
    - Total of 20 coordinate tuples (4 rows × 5 columns)
    - Letters A-O fill the first 3 rows completely
    - Row 4 has empty strings at positions (4,1) and (4,5)
    - Row 4 has numbers "1", "2", "3" at positions (4,2), (4,3), (4,4)
    - Coordinates use 1-based indexing for intuitive grid representation
    - Useful for coordinate-based operations and position analysis
    
    Use Cases:
    ----------
    - Knight move path analysis on letter/number grids
    - Position-based data processing without pandas dependency
    - Lightweight grid representation for algorithmic analysis
    """

    # Define the grid data row by row
    # Each row contains values for columns 1-5
    grid_rows = [
        ["A", "B", "C", "D", "E"],    # Row 1: Letters A-E
        ["F", "G", "H", "I", "J"],    # Row 2: Letters F-J  
        ["K", "L", "M", "N", "O"],    # Row 3: Letters K-O
        ["", "1", "2", "3", ""]       # Row 4: Numbers 1-3 with empty corners
    ]

    # Convert grid data to list of coordinate tuples
    coordinate_data = []
    
    # Iterate through each row (1-based indexing)
    for row_idx, row_data in enumerate(grid_rows, start=1):
        # Iterate through each column (1-based indexing)
        for col_idx, cell_value in enumerate(row_data, start=1):
            # Create tuple: (row, column, value)
            coordinate_tuple = (row_idx, col_idx, cell_value)
            coordinate_data.append(coordinate_tuple)
    
    return coordinate_data
    
if __name__ == "__main__":
    # Test the function and display results
    coordinate_data = get_table_data()
    
    print("Grid Data as Coordinate Tuples:")
    print("Format: (row, column, value)")
    print("-" * 30)
    
    # Display all coordinate tuples
    for i, (row, col, value) in enumerate(coordinate_data):
        # Format empty strings for better display
        display_value = f"'{value}'" if value else "''"
        print(f"[{i:2d}] ({row}, {col}) -> {display_value}")
        
        # Add row separator every 5 items (end of each row)
        if (i + 1) % 5 == 0 and i < len(coordinate_data) - 1:
            print()
    
    print(f"Total coordinates: {len(coordinate_data)}")
    print("Grid dimensions: 4 rows × 5 columns")
    
    # Show grid visualization
    print("\nGrid Visualization:")
    print("  ", end="")
    for col in range(1, 6):
        print(f"{col:^4}", end="")
    print()
    
    for row in range(1, 5):
        print(f"{row} ", end="")
        for col in range(1, 6):
            # Find the value for this coordinate
            value = next((val for r, c, val in coordinate_data if r == row and c == col), "?")
            display_val = value if value else "·"  # Use dot for empty
            print(f"{display_val:^4}", end="")
        print()
    
    # Show some specific coordinate lookups
    print("\nSample Coordinate Lookups:")
    test_coords = [(1, 1), (2, 3), (4, 2), (4, 5)]
    for test_row, test_col in test_coords:
        value = next((val for r, c, val in coordinate_data if r == test_row and c == test_col), "Not Found")
        print(f"  Position ({test_row}, {test_col}): '{value}'")
    
    # Show vowels and empty positions
    vowels = "AEIOU"
    vowel_positions = [(r, c) for r, c, val in coordinate_data if val in vowels]
    empty_positions = [(r, c) for r, c, val in coordinate_data if val == ""]
    
    print(f"\nVowel positions: {vowel_positions}")
    print(f"Empty positions: {empty_positions}")