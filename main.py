"""
Knight's Tour Sequence Analysis Script

This script analyzes knight move sequences on a 4x5 grid containing letters and numbers.
It finds valid sequences that avoid missing positions and limits visits to vowel locations.

The analysis includes:
- Creating a DataFrame with letters A-O and numbers 1-3
- Identifying vowel positions and missing/empty positions
- Generating knight move sequences with constraints
- Counting total valid sequences across all starting positions
"""

# Import required modules for data creation and sequence analysis
from src.table_data import get_table_data
from src.positions import get_vowel_positions, get_missing_positions, get_coordinate_bounds
from src.sequence_check import check_inside_bounds, check_in_avoided_coordinate
from src.sequence_create import get_all_sequences

if __name__ == "__main__":
    
    # =================================================================
    # STEP 1: Initialize the keypad and analyze its structure
    # =================================================================
    
    # Create the main coordinate data containing the letter/number grid
    # This creates coordinate tuples in format (row, col, value) for a 4x5 grid
    coordinate_data = get_table_data()
    print("Keypad (Coordinate Data):")
    print("First few coordinates:")
    for i, coord in enumerate(coordinate_data[:10]):
        print(f"  {coord}")
    print(f"  ... and {len(coordinate_data) - 10} more coordinates")
    print()

    # Find all missing/empty positions in the coordinate data
    # These positions will be avoided during sequence generation
    miss_pos = get_missing_positions(coordinate_data)
    print(f"Missing positions (to avoid): {miss_pos}")

    # Find all vowel positions (A, E, I, O, U) in the coordinate data  
    # These are special positions that we want to limit visits to
    vo_pos = get_vowel_positions(coordinate_data)
    print(f"Vowel positions (limited visits): {vo_pos}")

    # Extract the numeric bounds of the coordinate data
    # This gives us [x_min, x_max, y_min, y_max] for boundary checking
    bounds_dict = get_coordinate_bounds(coordinate_data)
    idx_bounds = [bounds_dict['x_min'], bounds_dict['x_max'], bounds_dict['y_min'], bounds_dict['y_max']]
    print(f"Index bounds [x_min, x_max, y_min, y_max]: {idx_bounds}")
    print()

    # =================================================================
    # STEP 2: Define sequence validation criteria
    # =================================================================
    
    # Create a filter function that validates knight move sequences
    # A valid sequence must:
    # 1. Stay within the coordinate boundaries (check_inside_bounds)
    # 2. Avoid all missing/empty positions (not check_in_avoided_coordinate)
    filter = lambda sequence: (check_inside_bounds(sequence, *idx_bounds)) and (not check_in_avoided_coordinate(sequence, miss_pos))

    # =================================================================
    # STEP 3: Generate and count valid knight move sequences
    # =================================================================
    
    # Extract bounds
    x_min, x_max = bounds_dict['x_min'], bounds_dict['x_max']
    y_min, y_max = bounds_dict['y_min'], bounds_dict['y_max']

    # Set the number of knight moves to analyze (sequence length = step + 1)
    step_i = 9
    
    # Maximum allowed visits to vowel positions
    max_hit = 2
    
    # Initialize total number of sequences counter for total valid sequences
    total_sequences = 0
    
    # Iterate through all possible starting positions on the coordinate grid
    print(f"Analyzing {step_i}-move knight sequences from all starting positions...")
    
    # Loop through all x coordinates (rows)
    for x_i in range(x_min, x_max + 1):
        # Loop through all y coordinates (columns)
        for y_i in range(y_min, y_max + 1):
            
            # Generate all valid knight move sequences from position (x_i, y_i)
            # Constraints applied:
            # - location_list=vo_pos: Track visits to vowel positions
            # - max_hit=2: Maximum 2 visits to vowel positions allowed
            # - filter=filter: Apply boundary and avoidance constraints
            all_sequence_list = get_all_sequences(
                x_i, y_i, step_i, 
                location_list=vo_pos, 
                max_hit=max_hit, 
                filter=filter
            )

            # Add the number of valid sequences from this starting position
            total_sequences += len(all_sequence_list)

            # Optional: Print progress for each starting position
            if len(all_sequence_list) > 0:
                print(f"  Starting position ({x_i},{y_i}): {len(all_sequence_list)} valid sequences")

    # =================================================================
    # STEP 4: Display final results
    # =================================================================
    
    print()
    print("="*50)
    print("ANALYSIS COMPLETE")
    print("="*50)
    print(f"Sequence length: {step_i + 1} positions")
    print("Vowel visit limit: 2 visits maximum")
    print(f"Avoided positions: {len(miss_pos)} missing positions")
    print(f"Total valid sequences found: {total_sequences}")
    print("="*50)