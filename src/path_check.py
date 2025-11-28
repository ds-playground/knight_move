from typing import List, Tuple


def check_inside_bounds(path: List[Tuple[int, int]], x_min: int, x_max: int, y_min: int, y_max: int) -> bool:
    """
    Check if all coordinates in the path are inside the specified rectangular bounds.
    
    This function validates that every coordinate in a path falls within the defined
    rectangular boundary. It's commonly used for boundary validation in grid-based
    games, pathfinding algorithms, or coordinate system constraints.
    
    Parameters:
    -----------
    path : list[tuple[int, int]]
        List of coordinate tuples representing a path or sequence of positions.
        Each tuple should be in the form (x, y) with integer coordinates.
    x_min : int
        Minimum allowed x-coordinate value (inclusive boundary)
    x_max : int
        Maximum allowed x-coordinate value (inclusive boundary)
    y_min : int
        Minimum allowed y-coordinate value (inclusive boundary)
    y_max : int
        Maximum allowed y-coordinate value (inclusive boundary)
    
    Returns:
    --------
    bool
        True if ALL coordinates in the path are within bounds (inclusive),
        False if ANY coordinate is outside the specified boundaries
    
    Examples:
    ---------
    >>> check_inside_bounds([(1,1), (2,2), (3,3)], 0, 5, 0, 5)
    True  # All coordinates within bounds 0-5 for both x and y
    
    >>> check_inside_bounds([(1,1), (6,2), (3,3)], 0, 5, 0, 5)
    False  # (6,2) has x=6 which exceeds x_max=5
    
    >>> check_inside_bounds([(2,2)], 2, 2, 2, 2)
    True  # Single coordinate exactly on boundary
    
    >>> check_inside_bounds([], 0, 5, 0, 5)
    True  # Empty path is considered valid (vacuously true)
    
    Notes:
    ------
    - Boundaries are inclusive: coordinates equal to min/max values are valid
    - Returns False immediately upon finding the first out-of-bounds coordinate
    - Empty paths return True (all zero coordinates are within bounds)
    - Time complexity: O(n) where n is the length of the path
    - Space complexity: O(1)
    
    Use Cases:
    ----------
    - Grid game validation (chess, checkers, etc.)
    - Pathfinding boundary checks
    - Coordinate system constraints
    - Input validation for grid-based algorithms
    - Collision detection preprocessing
    
    See Also:
    ---------
    check_in_avoided_coordinate : Check if path hits forbidden coordinates
    """
    for (x, y) in path:
        if x < x_min or x > x_max or y < y_min or y > y_max:
            return False
    return True

def check_in_avoided_coordinate(path: List[Tuple[int, int]], list_of_coordinates: List[Tuple[int, int]]) -> bool:
    """
    Check if any coordinate in the path intersects with a list of avoided coordinates.
    
    This function determines whether a path contains any coordinates that should be
    avoided. It's useful for pathfinding algorithms that need to avoid obstacles,
    forbidden zones, or previously visited locations.
    
    Parameters:
    -----------
    path : list[tuple[int, int]]
        List of coordinate tuples representing the path to check.
        Each tuple should be in the form (x, y) with integer coordinates.
    list_of_coordinates : list[tuple[int, int]]
        List of coordinate tuples representing forbidden or avoided positions.
        Each tuple should be in the form (x, y) with integer coordinates.
    
    Returns:
    --------
    bool
        True if ANY coordinate in the path exists in the avoided coordinates list,
        False if NO coordinates in the path match any avoided coordinates
    
    Examples:
    ---------
    >>> path = [(1,1), (2,2), (3,3)]
    >>> avoided = [(2,2), (4,4)]
    >>> check_in_avoided_coordinate(path, avoided)
    True  # (2,2) appears in both path and avoided list
    
    >>> path = [(1,1), (2,3), (3,1)]
    >>> avoided = [(2,2), (4,4)]
    >>> check_in_avoided_coordinate(path, avoided)
    False  # No coordinates match
    
    >>> path = []
    >>> avoided = [(1,1), (2,2)]
    >>> check_in_avoided_coordinate(path, avoided)
    False  # Empty path has no coordinates to avoid
    
    >>> path = [(1,1), (2,2)]
    >>> avoided = []
    >>> check_in_avoided_coordinate(path, avoided)
    False  # No coordinates to avoid
    
    Performance:
    -----------
    - Time complexity: O(n * m) where n = len(path), m = len(list_of_coordinates)
    - Space complexity: O(1)
    - Uses any() for early termination when first match is found
    - Converting list_of_coordinates to set can improve performance for large lists
    
    Notes:
    ------
    - Returns True immediately upon finding the first intersection
    - Both empty path and empty avoided list result in False
    - Coordinate comparison uses exact tuple matching
    - Function is symmetric: order of coordinates in lists doesn't matter
    
    Use Cases:
    ----------
    - Obstacle avoidance in pathfinding algorithms
    - Collision detection in grid-based games
    - Route planning with forbidden zones
    - Validation of movement constraints
    - Safety checks in automated navigation
    
    See Also:
    ---------
    check_inside_bounds : Validate path coordinates within boundaries
    count_path_hit_location_list : Count intersections with target coordinates
    """    
    return any((x, y) in list_of_coordinates for (x, y) in path)

def check_same_alternate_coordinate_exists(path: List[Tuple[int, int]]) -> bool:
    """
    Check if a knight's path contains any repeated coordinates at alternating positions.
    
    This function detects if the knight returns to a previously visited position
    with exactly one move in between. This pattern indicates potential inefficiency
    or cycles in the knight's movement strategy.
    
    The pattern being detected is: position[i] == position[i-2], meaning the knight
    was at the same location two moves ago.
    
    Parameters:
    -----------
    path : list[tuple[int, int]]
        List of coordinate tuples representing the knight's path.
        Each tuple should be in the form (x, y) with integer coordinates.
    
    Returns:
    --------
    bool
        True if any position repeats with exactly one move between occurrences,
        False otherwise
    
    Examples:
    ---------
    >>> check_same_alternate_coordinate_exists([(1,2), (2,3), (1,2), (2,3)])
    True  # Position (1,2) repeats at indices 0 and 2
    
    >>> check_same_alternate_coordinate_exists([(1,2), (2,3), (1,4), (2,3)])
    True  # Position (2,3) repeats at indices 1 and 3
    
    >>> check_same_alternate_coordinate_exists([(1,2), (2,3)])
    False  # Path too short to have alternating pattern
    
    Notes:
    ------
    - Paths with fewer than 3 positions cannot have alternating repetitions
    - This is useful for detecting back-and-forth movement patterns
    - The function uses any() for efficient early termination
    """
    # Paths with fewer than 3 positions cannot have alternating repetitions
    # Need at least positions 0, 1, 2 to compare position[2] with position[0]
    if len(path) < 3:
        return False
    
    # Check each position starting from index 2 against the position 2 steps back
    # any() returns True as soon as the first match is found (efficient)
    return any(path[i] == path[i-2] for i in range(2, len(path)))

def count_path_hit_location_list(path: List[Tuple[int, int]], location_list: List[Tuple[int, int]]) -> int:
    """
    Count the number of times any coordinate in the path hits coordinates in a specific location list.
    
    This function analyzes a path (sequence of coordinate tuples) and counts how many times
    the path visits any of the coordinates specified in the location list. Each visit to
    any location in the list increments the count by 1, so multiple visits to the same
    location or different locations all contribute to the total count.
    
    Parameters:
    -----------
    path : list[tuple[int, int]]
        A list of coordinate tuples representing the path taken.
        Each tuple should be in the form (x, y) with integer coordinates.
    location_list : list[tuple[int, int]]
        A list of coordinate tuples representing target locations to check against.
        Each tuple should be in the form (x, y) with integer coordinates.
    
    Returns:
    --------
    int
        The total number of hits - how many times any coordinate in the path
        matches any coordinate in the location list
    
    Examples:
    ---------
    >>> path = [(1,1), (2,2), (1,1), (3,3)]
    >>> targets = [(1,1), (2,2)]
    >>> count_path_hit_location_list(path, targets)
    3  # (1,1) appears twice, (2,2) appears once = 3 total hits
    
    >>> path = [(1,1), (2,3), (4,5)]
    >>> targets = [(1,1), (6,7)]
    >>> count_path_hit_location_list(path, targets)
    1  # Only (1,1) matches, appearing once
    
    >>> path = [(1,2), (3,4), (5,6)]
    >>> targets = [(7,8), (9,10)]
    >>> count_path_hit_location_list(path, targets)
    0  # No coordinates in path match any in the target list
    
    Notes:
    ------
    - Multiple visits to the same target location are counted separately
    - The function uses list comprehension with sum() for efficient counting
    - Time complexity: O(n * m) where n = len(path) and m = len(location_list)
    - Useful for analyzing knight move paths, tracking waypoint visits, or route optimization
    
    Use Cases:
    ----------
    - Knight's tour analysis: counting visits to special squares
    - Path optimization: measuring how often a route hits important waypoints  
    - Game mechanics: tracking player visits to specific game locations
    - Route analysis: counting intersections with points of interest
    """
    # Use list comprehension to check each path coordinate against all target locations
    # For each coordinate in the path, check if it exists in the location list
    # Sum up all the matches (True values are treated as 1, False as 0)
    return sum([1 for coordinate in path if coordinate in location_list])

if __name__ == "__main__":

    # Define specific locations of interest for path analysis
    # These coordinates represent important waypoints or target locations
    specific_locations = [(1,1), (1,5), (2,4), (3,5)]

    # Example path for testing the hit counting function
    # This path represents a knight's journey with some coordinates that may hit our target locations
    path = [(1, 1), (3, 2), (1, 3), (3, 4), (1, 1)]


    # Test the function with the example data
    print("Testing count_path_hit_location_list function:")
    print(f"Path: {path}")
    print(f"Target locations: {specific_locations}")

    hit_count = count_path_hit_location_list(path, specific_locations)
    print(f"Number of hits: {hit_count}")

    # Detailed analysis of which coordinates hit
    print("\nDetailed analysis:")
    for i, coord in enumerate(path):
        if coord in specific_locations:
            print(f"  Step {i+1}: {coord} - HIT! (matches target location)")
        else:
            print(f"  Step {i+1}: {coord} - miss")

    # Additional test cases to demonstrate the function
    print("\n" + "="*50)
    print("Additional test cases:")

    test_cases = [
        {
            'path': [(1,1), (2,2), (1,1), (3,3)],
            'targets': [(1,1), (2,2)],
            'description': 'Multiple visits to same target'
        },
        {
            'path': [(1,2), (3,4), (5,6)],
            'targets': [(7,8), (9,10)],
            'description': 'No matches'
        },
        {
            'path': [(1,1), (1,5), (2,4), (3,5)],
            'targets': [(1,1), (1,5), (2,4), (3,5)],
            'description': 'All coordinates match'
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = count_path_hit_location_list(test['path'], test['targets'])
        print(f"Test {i}: {test['description']}")
        print(f"  Path: {test['path']}")
        print(f"  Targets: {test['targets']}")
        print(f"  Hits: {result}")
        print()

