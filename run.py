#!/usr/bin/env python3
"""
Simple runner script for knight move analysis with step_i = 9 (path length of 10).
Prints total number of paths in a single line.
"""

from src.table_data import get_table_data
from src.positions import get_vowel_positions, get_missing_positions, get_coordinate_bounds
from src.path_check import check_inside_bounds, check_inside_bounds, check_in_avoided_coordinate
from src.path_create import get_all_paths

def main():
    # Get coordinate data and analysis parameters
    coordinate_data = get_table_data()    
    miss_pos = get_missing_positions(coordinate_data)
    vo_pos = get_vowel_positions(coordinate_data)
    bounds_dict = get_coordinate_bounds(coordinate_data)
    idx_bounds = [bounds_dict['x_min'], bounds_dict['x_max'], bounds_dict['y_min'], bounds_dict['y_max']]
    filter = lambda path: (check_inside_bounds(path, *idx_bounds)) and (not check_in_avoided_coordinate(path, miss_pos))
    
    # Extract bounds
    x_min, x_max = bounds_dict['x_min'], bounds_dict['x_max']
    y_min, y_max = bounds_dict['y_min'], bounds_dict['y_max']
    
    # Set the number of knight moves to analyze (path length = step + 1)
    step_i = 9

    # Maximum allowed visits to vowel positions
    max_hit = 2
    
    # Initialize total number of paths counter for total valid paths
    total_paths = 0
    
    # Generate paths from all starting positions
    for x_i in range(x_min, x_max + 1):
        for y_i in range(y_min, y_max + 1):
            all_path_list = get_all_paths(
                x_i, y_i, step_i,
                location_list=vo_pos,
                max_hit=max_hit,
                filter=filter
            )            
            
            # Add the number of valid paths from this starting position
            total_paths += len(all_path_list)
    
    print(f"Total number of valid paths: {total_paths}")

if __name__ == "__main__":
    main()