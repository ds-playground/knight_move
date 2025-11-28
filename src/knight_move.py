from typing import List, Tuple


def knight_move(x_i: int, y_i: int, move_direction: int) -> Tuple[int, int]:
    """
    Make a knight move from initial position (x_i, y_i).
    
    This function calculates the final position after making a specific knight move
    from a given starting position. Knight moves follow the standard chess pattern
    of moving in an L-shape (2 squares in one direction, 1 square perpendicular).
    
    Parameters:
    -----------
    x_i : int
        Initial x-coordinate (row position)
    y_i : int
        Initial y-coordinate (column position)
    move_direction : int
        Integer from 1-8 representing one of the 8 possible knight moves:
        1: 2 right, 1 up    |  2: 2 right, 1 down
        3: 2 left, 1 up     |  4: 2 left, 1 down
        5: 1 right, 2 up    |  6: 1 right, 2 down
        7: 1 left, 2 up     |  8: 1 left, 2 down
    
    Returns:
    --------
    tuple[int, int]
        A tuple containing the final coordinates (x_f, y_f) after the knight move
    
    Raises:
    -------
    ValueError
        If move_direction is not between 1 and 8 (inclusive)
    
    Examples:
    ---------
    >>> knight_move(3, 3, 1)
    (5, 4)  # From (3,3), move 2 right and 1 up
    
    >>> knight_move(1, 1, 5)
    (2, 3)  # From (1,1), move 1 right and 2 up
    
    Notes:
    ------
    - No boundary checking is performed; coordinates can be negative or exceed board limits
    - Use with appropriate boundary validation for specific board sizes
    - Move directions are numbered consistently for easy reference
    """
    
    # Define all 8 possible knight moves (dx, dy)
    knight_moves = [
        (2, 1),   # Move 1: 2 right, 1 up
        (2, -1),  # Move 2: 2 right, 1 down
        (-2, 1),  # Move 3: 2 left, 1 up
        (-2, -1), # Move 4: 2 left, 1 down
        (1, 2),   # Move 5: 1 right, 2 up
        (1, -2),  # Move 6: 1 right, 2 down
        (-1, 2),  # Move 7: 1 left, 2 up
        (-1, -2)  # Move 8: 1 left, 2 down
    ]
    
    if move_direction < 1 or move_direction > 8:
        raise ValueError("move_direction must be between 1 and 8")
    
    # Get the move offset
    dx, dy = knight_moves[move_direction - 1]
    
    # Calculate final position
    x_f = x_i + dx
    y_f = y_i + dy
    
    return x_f, y_f

# Alternative function that returns all possible knight moves
def all_knight_moves(x_i: int, y_i: int) -> List[Tuple[int, int]]:
    """
    Generate all possible knight moves from initial position (x_i, y_i).
    
    This function calculates all 8 possible knight moves from a given starting
    position and returns them as a list of coordinate pairs. Each move follows
    the standard chess knight movement pattern (L-shaped moves).
    
    Parameters:
    -----------
    x_i : int
        Initial x-coordinate (row position) of the knight
    y_i : int
        Initial y-coordinate (column position) of the knight
    
    Returns:
    --------
    list[tuple[int, int]]
        A list containing 8 tuples, where each tuple represents the final
        coordinates (x_f, y_f) for one of the 8 possible knight moves.
        The moves are ordered by move_direction (1-8) as defined in knight_move().
    
    Examples:
    ---------
    >>> all_knight_moves(3, 3)
    [(5, 4), (5, 2), (1, 4), (1, 2), (4, 5), (4, 1), (2, 5), (2, 1)]
    
    >>> all_knight_moves(0, 0)
    [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    Notes:
    ------
    - Always returns exactly 8 moves regardless of board boundaries
    - No filtering for valid board positions is performed
    - Resulting coordinates may be negative or exceed intended board limits
    - Use with boundary checking functions for specific game implementations
    - Move order corresponds to knight_move() direction numbering (1-8)
    
    See Also:
    ---------
    knight_move : Calculate a single knight move in a specific direction
    """
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    possible_moves = []
    for dx, dy in knight_moves:
        x_f = x_i + dx
        y_f = y_i + dy
        possible_moves.append((x_f, y_f))
    
    return possible_moves

if __name__ == "__main__":

    # Example usage
    print("Knight Move Examples:")
    print("Starting position: (3, 3)")
    print(f"Move 1 (2 right, 1 up): {knight_move(3, 3, 1)}")
    print(f"Move 5 (1 right, 2 up): {knight_move(3, 3, 5)}")
    print(f"All possible moves from (3, 3): {all_knight_moves(3, 3)}")