from typing import List, Tuple, Dict, Union, Any

def get_vowel_positions(coordinate_data: List[Tuple[int, int, str]]) -> List[Tuple[int, int]]:
    """
    Find the row and column indices where grid elements are vowels.
    
    This function scans through coordinate data and identifies positions where
    the elements are vowels (a, e, i, o, u), regardless of case. It returns
    a list of tuples containing the row and column indices of vowel elements.
    
    Parameters:
    -----------
    coordinate_data : List[Tuple[int, int, str]]
        List of coordinate tuples in format (row, column, value).
        Each tuple represents a position and its content in the grid.
    
    Returns:
    --------
    List[Tuple[int, int]]
        A list of (row, column) tuples where vowels are found.
        Each tuple represents the position of a vowel in the grid.
        Returns empty list if no vowels are found.
    
    Examples:
    ---------
    >>> data = [(1, 1, 'A'), (1, 2, 'B'), (2, 1, 'C'), (2, 2, 'E')]
    >>> get_vowel_positions(data)
    [(1, 1), (2, 2)]  # 'A' at (1,1) and 'E' at (2,2)
    
    >>> data2 = [(1, 1, 'X'), (1, 2, 'Y'), (2, 1, 'Z'), (2, 2, 'W')]
    >>> get_vowel_positions(data2)
    []  # No vowels found
    
    >>> data3 = [(1, 1, 'a'), (1, 2, '1'), (2, 1, 'O'), (2, 2, 'u')]
    >>> get_vowel_positions(data3)
    [(1, 1), (2, 1), (2, 2)]  # 'a', 'O', and 'u' are vowels
    
    Notes:
    ------
    - Case-insensitive: both uppercase and lowercase vowels are detected
    - Only considers English vowels: a, e, i, o, u
    - Non-string elements are converted to string for vowel checking
    - Only single-character elements (after string conversion) are considered
    - Returns empty list if input data is empty or contains no vowels
    
    Performance:
    -----------
    - Time complexity: O(n) where n is the number of coordinate tuples
    - Space complexity: O(k) where k is the number of vowels found
    
    Use Cases:
    ----------
    - Finding vowel positions in letter grids or word puzzles
    - Analyzing text data stored in coordinate format
    - Creating position-based filters for vowel locations
    - Text analysis and natural language processing tasks
    
    See Also:
    ---------
    get_missing_positions : Find positions with missing/empty values
    get_coordinate_bounds : Get coordinate boundaries from data
    """
    # Define vowels for checking (both cases for efficiency)
    vowels = "aeiouAEIOU"
    
    # List to store positions of vowels
    vowel_positions = []
    
    # Iterate through all coordinate tuples
    for row, col, value in coordinate_data:
        # Convert to string in case element is not a string
        value_str = str(value)
        
        # Check if the element is a single vowel
        if len(value_str) == 1 and value_str in vowels:
            vowel_positions.append((row, col))
    
    return vowel_positions

def get_missing_positions(coordinate_data: List[Tuple[int, int, str]]) -> List[Tuple[int, int]]:
    """
    Find positions in coordinate data where values are missing or effectively empty.
    
    This function identifies all positions in coordinate data that contain missing,
    null, empty, or whitespace-only values. It's useful for data quality assessment
    and preprocessing tasks where you need to locate positions that require
    imputation or special handling.
    
    Parameters:
    -----------
    coordinate_data : List[Tuple[int, int, str]]
        List of coordinate tuples in format (row, column, value).
        Each tuple represents a position and its content in the grid.
    
    Returns:
    --------
    List[Tuple[int, int]]
        A list of (row, column) tuples where missing values are found.
        Each tuple represents a position containing a missing or empty value.
        Returns empty list if no missing values are found.
    
    Missing Value Types Detected:
    -----------------------------
    - None values : Standard Python None type
    - Empty strings : ""
    - Whitespace-only strings : "   ", "\t", "\n", etc.
    - String representations of None/missing : "None", "nan", "NaN"
    
    Examples:
    ---------
    >>> data = [(1, 1, 'A'), (1, 2, ''), (2, 1, None), (2, 2, 'C')]
    >>> get_missing_positions(data)
    [(1, 2), (2, 1)]  # Empty string and None
    
    >>> data2 = [(1, 1, 'A'), (1, 2, 'B'), (2, 1, 'C'), (2, 2, 'D')]
    >>> get_missing_positions(data2)
    []  # No missing values
    
    >>> data3 = [(1, 1, '  '), (1, 2, '\t'), (2, 1, '\n'), (2, 2, '   ')]
    >>> get_missing_positions(data3)
    [(1, 1), (1, 2), (2, 1), (2, 2)]  # All whitespace strings
    
    Notes:
    ------
    - String values are stripped of whitespace before checking if empty
    - Considers only completely whitespace strings as missing (not partial whitespace)
    - Does not modify the input coordinate data
    - Handles None values and string representations of missing data
    
    Performance:
    -----------
    - Time complexity: O(n) where n is the number of coordinate tuples
    - Space complexity: O(k) where k is the number of missing values found
    
    Use Cases:
    ----------
    - Data quality assessment and validation
    - Preprocessing for analysis pipelines
    - Identifying positions for data imputation
    - Creating position-based filters for missing data
    - Quality control in data entry and import processes
    
    See Also:
    ---------
    get_vowel_positions : Find positions containing vowel characters
    get_coordinate_bounds : Get coordinate boundaries from data
    """
    
    # List to store positions of missing values
    missing_positions = []
    
    # Iterate through all coordinate tuples
    for row, col, value in coordinate_data:
        # Check for None values
        if value is None:
            missing_positions.append((row, col))
        # Check for string representations and empty/whitespace strings
        elif isinstance(value, str):
            if value == "" or value.strip() == "":
                missing_positions.append((row, col))
            # Check for string representations of missing values
            elif value.lower() in ['none', 'nan', 'null', 'na']:
                missing_positions.append((row, col))
        # Convert non-string values to string and check for missing representations
        else:
            value_str = str(value).lower()
            if value_str in ['none', 'nan', 'null', 'na']:
                missing_positions.append((row, col))
    
    return missing_positions

def get_coordinate_bounds(coordinate_data: List[Tuple[int, int, str]]) -> Dict[str, Any]:
    """
    Get the minimum and maximum values of x and y coordinates from coordinate data.
    
    This function analyzes coordinate data and returns comprehensive bounds information
    for both x and y coordinates. This is useful for understanding the range
    and structure of grid coordinates, coordinate systems, and data boundaries.
    
    Parameters:
    -----------
    coordinate_data : List[Tuple[int, int, str]]
        List of coordinate tuples in format (x, y, value).
        Each tuple represents a position and its content in the grid.
        Must be non-empty to avoid errors.
    
    Returns:
    --------
    Dict[str, Any]
        A dictionary containing bounds information with the following keys:
        - 'x_min': int - minimum x coordinate value
        - 'x_max': int - maximum x coordinate value  
        - 'y_min': int - minimum y coordinate value
        - 'y_max': int - maximum y coordinate value
        - 'x_range': Tuple[int, int] - (x_min, x_max)
        - 'y_range': Tuple[int, int] - (y_min, y_max)
    
    Examples:
    ---------
    >>> data = [(1, 1, 'A'), (1, 2, 'B'), (2, 1, 'C'), (3, 3, 'D')]
    >>> bounds = get_coordinate_bounds(data)
    >>> bounds['x_range']
    (1, 3)
    >>> bounds['y_range']
    (1, 3)
    
    >>> data2 = [(5, 10, 'X'), (5, 20, 'Y'), (5, 30, 'Z')]
    >>> get_coordinate_bounds(data2)
    {'x_min': 5, 'x_max': 5, 'y_min': 10, 'y_max': 30,
     'x_range': (5, 5), 'y_range': (10, 30)}
    
    >>> data3 = [(42, 100, 'single')]
    >>> get_coordinate_bounds(data3)  # Single element
    {'x_min': 42, 'x_max': 42, 'y_min': 100, 'y_max': 100,
     'x_range': (42, 42), 'y_range': (100, 100)}
    
    Notes:
    ------
    - Works with integer coordinate systems
    - Single-coordinate datasets return identical min/max values
    - Performance is O(n) where n is the number of coordinate tuples
    
    Raises:
    -------
    ValueError
        If the input coordinate data is empty
    
    Use Cases:
    ----------
    - Understanding grid structure and coordinate bounds
    - Validating coordinate ranges before processing operations
    - Setting up coordinate systems, grids, or plotting boundaries
    - Preparing data for mathematical operations requiring bounds
    - Quality assurance checks for expected coordinate ranges
    - Configuring iterative algorithms that need coordinate limits
    
    Performance:
    -----------
    - Time complexity: O(n) where n is number of coordinate tuples
    - Space complexity: O(1) excluding the returned dictionary
    
    See Also:
    ---------
    get_vowel_positions : Find specific element positions in coordinate data
    get_missing_positions : Find missing value positions in coordinate data
    """
    
    # Check if coordinate data is empty
    if not coordinate_data:
        raise ValueError("Cannot get bounds from empty coordinate data")
    
    # Extract all x and y coordinates
    x_coords = [x for x, y, value in coordinate_data]
    y_coords = [y for x, y, value in coordinate_data]
    
    # Get bounds
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    
    # Return comprehensive bounds information
    bounds = {
        'x_min': x_min,
        'x_max': x_max,
        'y_min': y_min,
        'y_max': y_max,
        'x_range': (x_min, x_max),
        'y_range': (y_min, y_max)
    }
    
    return bounds

if __name__ == "__main__":

    print("Testing get_vowel_positions function:")
    print("Testing with coordinate data:")
    test_data = [
        (1, 1, 'A'), (1, 2, 'B'), (1, 3, 'C'), (1, 4, 'D'), (1, 5, 'E'),
        (2, 1, 'F'), (2, 2, 'G'), (2, 3, 'H'), (2, 4, 'I'), (2, 5, 'J'),
        (3, 1, 'K'), (3, 2, 'L'), (3, 3, 'M'), (3, 4, 'N'), (3, 5, 'O'),
        (4, 1, 'P'), (4, 2, 'Q'), (4, 3, 'R'), (4, 4, 'S'), (4, 5, 'U')
    ]

    print("Test coordinate data (showing first few items):")
    for i, item in enumerate(test_data[:5]):
        print(f"  {item}")
    print(f"  ... and {len(test_data) - 5} more items")
    print()

    test_vowel_positions = get_vowel_positions(test_data)
    print(f"Vowel positions in test data: {test_vowel_positions}")
    print()

    # Show which letters are vowels
    print("Vowels found:")
    vowel_lookup = {(row, col): value for row, col, value in test_data}
    for row, col in test_vowel_positions:
        letter = vowel_lookup[(row, col)]
        print(f"  '{letter}' at position ({row}, {col})")

    print()
    print("="*50)

    # Test with mixed case and special elements
    print("Testing with mixed case coordinate data:")
    mixed_data = [
        (1, 1, 'a'), (1, 2, 'B'), (1, 3, '3'), (1, 4, 'E'),
        (2, 1, 'f'), (2, 2, 'G'), (2, 3, 'i'), (2, 4, 'J'),
        (3, 1, 'K'), (3, 2, ''), (3, 3, 'O'), (3, 4, 'u')
    ]

    print("Mixed coordinate data:")
    for item in mixed_data:
        print(f"  {item}")
    print()

    mixed_vowel_positions = get_vowel_positions(mixed_data)
    print(f"Vowel positions in mixed data: {mixed_vowel_positions}")
    print()

    print("Analysis:")
    mixed_lookup = {(row, col): value for row, col, value in mixed_data}
    for row, col in mixed_vowel_positions:
        element = mixed_lookup[(row, col)]
        print(f"  Element '{element}' (type: {type(element)}) at ({row}, {col}) is a vowel")

    print()
    print("="*60)

    # Test get_missing_positions function
    print("Testing get_missing_positions function:")
    print("Testing with missing values coordinate data:")
    
    test_missing_data = [
        (1, 1, 'A'), (1, 2, 'B'), (1, 3, ''), (1, 4, 'D'), (1, 5, 'E'),
        (2, 1, 'F'), (2, 2, None), (2, 3, 'H'), (2, 4, '   '), (2, 5, 'J'),
        (3, 1, None), (3, 2, 'L'), (3, 3, 'M'), (3, 4, None), (3, 5, ''),
        (4, 1, 'P'), (4, 2, 'Q'), (4, 3, 'R'), (4, 4, 'S'), (4, 5, 'T')
    ]

    print("Test missing values coordinate data:")
    for item in test_missing_data:
        print(f"  {item}")
    print()

    missing_positions = get_missing_positions(test_missing_data)
    print(f"Missing value positions: {missing_positions}")
    print()

    print("Missing values found:")
    missing_lookup = {(row, col): value for row, col, value in test_missing_data}
    for row, col in missing_positions:
        element = missing_lookup[(row, col)]
        element_type = type(element)
        # Check what type of missing value it is
        if element is None:
            missing_type = "None"
        elif element == "":
            missing_type = "Empty string"
        elif isinstance(element, str) and element.strip() == "":
            missing_type = "Whitespace-only string"
        else:
            missing_type = "Other"
        print(f"  {missing_type}: '{element}' (type: {element_type}) at position ({row}, {col})")

    print()
    print("="*60)

    # Test get_coordinate_bounds function
    print("Testing get_coordinate_bounds function:")
    
    print("Test 1: Numeric coordinate data")
    numeric_data = [
        (10, 100, '1'), (10, 50, '2'), (10, 200, '3'),
        (5, 100, '4'), (5, 50, '5'), (5, 200, '6'),
        (20, 100, '7'), (20, 50, '8'), (20, 200, '9')
    ]
    
    numeric_bounds = get_coordinate_bounds(numeric_data)
    print(f"Numeric coordinate bounds: {numeric_bounds}")
    print()

    print("Test 2: Single coordinate data")
    single_data = [(42, 100, 'single')]
    
    single_bounds = get_coordinate_bounds(single_data)
    print(f"Single coordinate bounds: {single_bounds}")
    print()

    print("Test 3: Default-style coordinate data")
    default_data = [
        (0, 0, 'a'), (0, 1, 'b'),
        (1, 0, 'c'), (1, 1, 'd'),
        (2, 0, 'e'), (2, 1, 'f')
    ]
    
    default_bounds = get_coordinate_bounds(default_data)
    print(f"Default-style bounds: {default_bounds}")
    print()

    print("Testing complete!")