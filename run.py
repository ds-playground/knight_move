#!/usr/bin/env python3
"""
Simple runner script for knight move analysis with step_i = 9 (sequence length of 10).
Prints total number of sequences in a single line.
"""

from src.table_data import get_table_data
from src.positions import get_vowel_positions, get_missing_positions, get_coordinate_bounds
from src.sequence_check import check_inside_bounds, check_in_avoided_coordinate
from src.sequence_create import get_all_sequences

def main():
    # Get coordinate data and analysis parameters
    coordinate_data = get_table_data()    
    miss_pos = get_missing_positions(coordinate_data)
    vo_pos = get_vowel_positions(coordinate_data)
    bounds_dict = get_coordinate_bounds(coordinate_data)
    idx_bounds = [bounds_dict['x_min'], bounds_dict['x_max'], bounds_dict['y_min'], bounds_dict['y_max']]
    filter = lambda sequence: (check_inside_bounds(sequence, *idx_bounds)) and (not check_in_avoided_coordinate(sequence, miss_pos))
    
    # Extract bounds
    x_min, x_max = bounds_dict['x_min'], bounds_dict['x_max']
    y_min, y_max = bounds_dict['y_min'], bounds_dict['y_max']
    
    # Set the number of knight moves to analyze (sequence length = step + 1)
    step_i = 9

    # Maximum allowed visits to vowel positions
    max_hit = 2
    
    # Initialize total number of sequences counter for total valid sequences
    total_sequences = 0
    
    # Generate sequences from all starting positions
    for x_i in range(x_min, x_max + 1):
        for y_i in range(y_min, y_max + 1):
            all_sequence_list = get_all_sequences(
                x_i, y_i, step_i,
                location_list=vo_pos,
                max_hit=max_hit,
                filter=filter
            )            
            
            # Add the number of valid sequences from this starting position
            total_sequences += len(all_sequence_list)
    
    print(f"Total number of valid sequences: {total_sequences}")

if __name__ == "__main__":
    main()