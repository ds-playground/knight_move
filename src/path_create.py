from typing import Union, Callable, Optional, Any, List, Tuple
from src.knight_move import all_knight_moves
from src.path_check import count_path_hit_location_list

def is_coordinate_tuple(element: Any) -> bool:
    """
    Check if an element is a valid coordinate tuple (i, j).
    
    This function validates that an element is a tuple containing exactly two
    numeric values (int or float), which represents a coordinate pair.
    
    Parameters:
    -----------
    element : Any
        The element to check for coordinate tuple validity
    
    Returns:
    --------
    bool
        True if element is a tuple with exactly 2 numeric values, False otherwise
    
    Examples:
    ---------
    >>> is_coordinate_tuple((1, 2))
    True
    
    >>> is_coordinate_tuple((1.5, 2.7))
    True
    
    >>> is_coordinate_tuple((1, 2, 3))
    False  # Too many elements
    
    >>> is_coordinate_tuple([1, 2])
    False  # List, not tuple
    
    >>> is_coordinate_tuple((1, 'a'))
    False  # Non-numeric element
    
    Notes:
    ------
    - Accepts both integers and floats as coordinate values
    - Requires exactly 2 elements in the tuple
    - Returns False for any non-tuple input
    """
    # First check: Must be a tuple type (not list, string, etc.)
    # Second check: Must have exactly 2 elements (x, y coordinates)
    # Third check: Both elements must be numeric (int or float)
    # Uses 'all()' to ensure every element in the tuple is numeric
    return (isinstance(element, tuple) and 
            len(element) == 2 and 
            all(isinstance(x, (int, float)) for x in element))

def is_list_of_coordinate_tuples(element: Any) -> bool:
    """
    Check whether an element is a list of coordinate tuples.
    
    This function validates that an element is a list where every item
    is a valid coordinate tuple (as defined by is_coordinate_tuple).
    
    Parameters:
    -----------
    element : Any
        The element to check for list of coordinate tuples validity
    
    Returns:
    --------
    bool
        True if element is a list containing only coordinate tuples, False otherwise
    
    Examples:
    ---------
    >>> is_list_of_coordinate_tuples([(1, 2), (3, 4)])
    True
    
    >>> is_list_of_coordinate_tuples([(1.5, 2.7), (3, 4)])
    True  # Mixed int and float coordinates
    
    >>> is_list_of_coordinate_tuples([])
    True  # Empty list is valid
    
    >>> is_list_of_coordinate_tuples([(1, 2), (3, 4, 5)])
    False  # Contains invalid coordinate tuple
    
    >>> is_list_of_coordinate_tuples((1, 2))
    False  # Tuple, not list
    
    Notes:
    ------
    - Empty lists return True (vacuously true)
    - All elements must pass is_coordinate_tuple validation
    - Commonly used for validating path data structures
    
    See Also:
    ---------
    is_coordinate_tuple : Validates individual coordinate tuples
    """
    # First check: Must be a list type (not tuple, set, etc.)
    # Second check: Every item in the list must be a valid coordinate tuple
    # Uses 'all()' to ensure every element passes coordinate tuple validation
    # Empty list returns True because all() is vacuously true for empty sequences
    return (isinstance(element, list) and 
            all(is_coordinate_tuple(item) for item in element))

def is_list_of_lists_of_coordinate_tuples(element: Any) -> bool:
    """
    Check whether an element is a list of lists of coordinate tuples.
    
    This function validates that an element is a list where every item
    is itself a valid list of coordinate tuples (as defined by is_list_of_coordinate_tuples).
    This represents a collection of paths, where each path is a sequence of coordinates.
    
    Parameters:
    -----------
    element : Any
        The element to check for list of lists of coordinate tuples validity
    
    Returns:
    --------
    bool
        True if element is a list of lists, where each inner list contains only coordinate tuples, False otherwise
    
    Examples:
    ---------
    >>> is_list_of_lists_of_coordinate_tuples([[(1, 2), (3, 4)], [(5, 6)]])
    True  # Two paths: one with 2 coordinates, one with 1
    
    >>> is_list_of_lists_of_coordinate_tuples([[], [(1, 2)]])
    True  # Empty path and single-coordinate path
    
    >>> is_list_of_lists_of_coordinate_tuples([])
    True  # Empty list of paths
    
    >>> is_list_of_lists_of_coordinate_tuples([[(1, 2)], [(3, 4, 5)]])
    False  # Contains invalid coordinate tuple (3, 4, 5)
    
    >>> is_list_of_lists_of_coordinate_tuples([(1, 2), (3, 4)])
    False  # List of tuples, not list of lists
    
    Notes:
    ------
    - Represents multiple paths, each path being a sequence of coordinates
    - Empty outer list returns True (no paths to validate)
    - Empty inner lists return True (valid empty paths)
    - All inner elements must pass is_list_of_coordinate_tuples validation
    - Commonly used for representing collections of knight move paths
    
    See Also:
    ---------
    is_list_of_coordinate_tuples : Validates individual path structures
    is_coordinate_tuple : Validates individual coordinate tuples
    """
    # First check: Must be a list type (outer container)
    # Second check: Every item must be a valid list of coordinate tuples (inner containers)
    # This creates a 2-step nested structure: list of paths, each path is a list of coordinates
    # Uses recursive validation through is_list_of_coordinate_tuples function
    return (isinstance(element, list) and 
            all(is_list_of_coordinate_tuples(item) for item in element))

def check_and_convert(element: Union[Tuple[int, int], List[Tuple[int, int]], List[List[Tuple[int, int]]]]) -> List[List[Tuple[int, int]]]:
    """
    Check and convert various input formats to a standardized list of lists of coordinate tuples.
    
    This function accepts three types of inputs and converts them as follows:
    - Coordinate tuple (i,j) -> [[coordinate tuple]]
    - List of coordinate tuples -> [list of coordinate tuples]  
    - List of lists of coordinate tuples -> returns as-is
    
    Parameters:
    -----------
    element : Union[tuple[int, int], list[tuple[int, int]], list[list[tuple[int, int]]]]
        One of the following types:
        - tuple[int, int]: A coordinate tuple in the form (i, j) where i,j are integers
        - list[tuple[int, int]]: A list of coordinate tuples [(i1,j1), (i2,j2), ...]
        - list[list[tuple[int, int]]]: A list of lists of coordinate tuples [[(i1,j1), ...], [(i2,j2), ...], ...]
    
    Returns:
    --------
    list[list[tuple[int, int]]]
        A standardized list of lists of coordinate tuples for further processing.
        Each inner list represents a path or sequence of coordinates.
    
    Raises:
    ValueError: If input is not one of the accepted formats
    
    Examples:
    >>> check_and_convert((1, 2))
    [[(1, 2)]]
    >>> check_and_convert([(1, 2), (3, 4)])
    [[(1, 2), (3, 4)]]
    >>> check_and_convert([[(1, 2)], [(3, 4)]])
    [[(1, 2)], [(3, 4)]]
    """

    # Case 1: Single coordinate tuple (x, y) -> Convert to [[(x, y)]]
    # This represents a single path with one coordinate (starting position)
    if is_coordinate_tuple(element):        
        # Wrap in double list: inner list = path, outer list = collection of paths
        return [[element]]
    
    # Case 2: List of coordinate tuples [(x1, y1), (x2, y2)] -> Convert to [[(x1, y1), (x2, y2)]]
    # This represents a single path with multiple coordinates
    elif is_list_of_coordinate_tuples(element):        
        # Wrap in outer list to make it a collection of one path
        return [element]
    
    # Case 3: Already in target format [[(x1, y1)], [(x2, y2)]] -> Return as-is
    # This represents multiple paths, each with their own coordinates
    elif is_list_of_lists_of_coordinate_tuples(element):
        # No conversion needed, already in standardized format
        return element
    
    # Case 4: Invalid input type - raise descriptive error
    else:
        raise ValueError("Input must be a coordinate tuple, list of coordinate tuples, or list of lists of coordinate tuples.")
    
def add_step(l_in: Union[Tuple[int, int], List[Tuple[int, int]], List[List[Tuple[int, int]]]]) -> List[List[Tuple[int, int]]]:
    """
    Add one step of knight moves to existing paths.
    
    This function takes existing paths and extends each path by adding all possible
    knight moves from the last position of each path. It effectively generates
    all possible continuations of the given paths by one knight move.
    
    Parameters:
    -----------
    l_in : Union[tuple[int, int], list[tuple[int, int]], list[list[tuple[int, int]]]]
        Input paths in any of the supported formats:
        - Single coordinate tuple: starting position
        - List of coordinates: single path
        - List of lists: multiple paths
    
    Returns:
    --------
    list[list[tuple[int, int]]]
        A list of extended paths, where each original path is extended by
        all possible knight moves from its last position. If an input path
        had n coordinates, each output path will have n+1 coordinates.
    
    Examples:
    ---------
    >>> add_step((1, 1))
    [[(1, 1), (3, 2)], [(1, 1), (3, 0)], ...] # All 8 possible moves from (1,1)
    
    >>> add_step([(1, 1), (3, 2)])
    [[(1, 1), (3, 2), (5, 3)], [(1, 1), (3, 2), (5, 1)], ...] # All moves from (3,2)
    
    Notes:
    ------
    - Uses all_knight_moves to generate possible moves from the last position
    - Each input path generates 8 output paths (one for each knight move)
    - Input is automatically converted to standard format using check_and_convert
    - Time complexity: O(8 * number_of_input_paths)
    
    See Also:
    ---------
    all_knight_moves : Generates all possible knight moves from a position
    check_and_convert : Converts input to standardized format
    """

    # Standardize input format to list of lists of coordinate tuples
    # This ensures we always work with the same data structure regardless of input type
    l_in = check_and_convert(l_in)

    # Initialize output list to collect all extended paths
    l_out = []
    
    # Process each existing path in the input
    for t in l_in:
        # Get the last coordinate of the current path (knight's current position)
        # t[-1] gets the last element, which is a coordinate tuple (x, y)
        x, y = t[-1]        
        
        # Generate all 8 possible knight moves from the current position
        # all_knight_moves returns a list of 8 coordinate tuples
        for (m, n) in all_knight_moves(x, y):
            # Extend the current path by appending the new coordinate
            # t + [(m, n)] creates a new path with one additional move
            # Add this extended path to the output collection
            l_out += [t + [(m, n)]]

    # Return all extended paths
    # If input had N paths, output will have N * 8 paths (8 moves per path)
    return l_out

def get_all_paths(
    x: int, 
    y: int, 
    n_steps: int, 
    location_list: Optional[List[Tuple[int, int]]] = None, 
    max_hit: Optional[int] = None, 
    filter: Optional[Callable[[List[Tuple[int, int]]], bool]] = None
) -> List[List[Tuple[int, int]]]:
    """
    Generate all possible knight move paths from an initial position with optional filtering.
    
    This function generates all possible sequences of knight moves starting from
    position (x, y) for a specified number of steps. It supports various filtering
    options including hit count limits and custom filter functions.
    
    Parameters:
    -----------
    x : int
        Initial x-coordinate of the starting position
    y : int
        Initial y-coordinate of the starting position
    n_steps : int
        Number of knight move steps to generate. Each step adds one more move
        to each path, so final paths will have n_steps + 1 coordinates
    location_list : Optional[list[tuple[int, int]]], default=None
        List of special coordinates to track hits against. Used with max_hit
        parameter for filtering paths based on location intersections
    max_hit : Optional[int], default=None
        Maximum number of hits allowed against location_list. Paths exceeding
        this limit are filtered out. Requires location_list to be specified
    filter : Optional[Callable[[list[tuple[int, int]]], bool]], default=None
        Custom filter function that takes a path and returns True if the path
        should be kept, False if it should be filtered out
    
    Returns:
    --------
    list[list[tuple[int, int]]]
        List of all valid paths, where each path is a list of coordinate tuples.
        Each path starts with (x, y) and contains exactly n_steps + 1 coordinates.
        Returns empty list if initial position fails filter conditions.
    
    Examples:
    ---------
    >>> get_all_paths(1, 1, 1)
    [[(1, 1), (3, 2)], [(1, 1), (3, 0)], ...] # All 8 possible 1-move paths
    
    >>> get_all_paths(1, 1, 2, location_list=[(3, 2)], max_hit=1)
    # Only paths that hit (3, 2) at most once
    
    >>> def boundary_filter(path):
    ...     return all(0 <= x <= 10 and 0 <= y <= 10 for x, y in path)
    >>> get_all_paths(5, 5, 2, filter=boundary_filter)
    # Only paths that stay within 10x10 grid
    
    Filtering Behavior:
    ------------------
    - If filter function is provided, it's applied to every generated path
    - If location_list and max_hit are both provided, paths are filtered by hit count
    - Both filters can be used simultaneously (AND logic)
    - If initial position fails filter, returns empty list immediately
    
    Performance Notes:
    -----------------
    - Time complexity: O(8^n_steps * filter_cost) where filter_cost depends on filter complexity
    - Space complexity: O(8^n_steps * path_length) for storing all valid paths
    - Large n_steps can generate extremely large numbers of paths
    
    Raises:
    -------
    AssertionError
        If location_list is provided but is not a valid list of coordinate tuples,
        or if max_hit is provided but is not a positive integer
    
    Notes:
    ------
    - Uses exponential branching: each path can generate up to 8 new paths per step
    - Filtering is applied at each step to prevent exponential explosion
    - Hit counting uses count_path_hit_location_list for intersection analysis
    - Default filter function always returns True (no filtering)
    
    Use Cases:
    ----------
    - Knight's tour problem solving
    - Pathfinding with constraints
    - Game AI move generation
    - Combinatorial path analysis
    - Route optimization with waypoints
    
    See Also:
    ---------
    add_step : Extends paths by one knight move step
    count_path_hit_location_list : Counts path intersections with target locations
    all_knight_moves : Generates possible moves from a single position
    """

    # Determine if hit count filtering should be applied
    # Both location_list and max_hit must be provided for hit count filtering
    check_path_hit_count_cond = (location_list is not None) and (max_hit is not None)
    
    # Validate hit count filtering parameters if they're being used
    if check_path_hit_count_cond:
        # Ensure location_list is properly formatted list of coordinate tuples
        assert ((location_list is not None) and is_list_of_coordinate_tuples(location_list)), f"'location_list' must be a list of coordinate tuples"
        # Ensure max_hit is a positive integer (can't have negative or zero hit limits)
        assert ((max_hit is not None) and (max_hit > 0) and isinstance(max_hit, int)), f"'max_hit' must be positive integer"
    
    # Initialize the path collection with just the starting position
    # This creates a single path containing only the initial coordinate
    paths = [(x, y)]

    # Set up the filter function for path validation
    if filter is None:
        # Default filter: accept all paths (no filtering)
        # This function always returns True, allowing all paths through
        def filter_cond(path: List[Tuple[int, int]]) -> bool:
            return True        
    else:
        # Use the custom filter function provided by the caller
        # This allows for boundary checks, obstacle avoidance, etc.
        filter_cond = filter

    # Check if the starting position passes the filter condition
    # If the initial position is invalid, return empty list immediately
    if filter_cond(paths):
    
        # Generate paths step by step (iterative expansion)
        # Each iteration adds one more knight move to all existing paths
        for _ in range(n_steps):
            # Apply filtering based on whether hit count filtering is enabled
            if check_path_hit_count_cond:
                # Dual filtering: custom filter AND hit count limit
                # add_level() generates all possible extensions (8x expansion per path)
                # Filter keeps only paths that satisfy both conditions
                paths = [path for path in add_step(paths) 
                        if filter_cond(path) and 
                        count_path_hit_location_list(path, location_list) <= max_hit]
            else:
                # Single filtering: only custom filter (no hit count restriction)
                # Keep paths that pass the custom filter condition
                paths = [path for path in add_step(paths) if filter_cond(path)]

        # Return all valid paths after n_steps of expansion
        # Each path will have exactly (n_steps + 1) coordinates
        return paths

    else:
        # Starting position failed filter condition
        # Return empty list since no valid paths can be generated
        return []