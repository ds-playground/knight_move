from typing import Union, Callable, Optional, Any, List, Tuple
from src.knight_move import all_knight_moves
from src.sequence_check import count_sequence_hit_location_list

def is_coordinate_tuple(element: Any) -> bool:
    """
    Check if an element is a valid coordinate tuple (i, j).
    """
    return (isinstance(element, tuple) and 
            len(element) == 2 and 
            all(isinstance(x, (int, float)) for x in element))

def is_list_of_coordinate_tuples(element: Any) -> bool:
    return (isinstance(element, list) and 
            all(is_coordinate_tuple(item) for item in element))

def is_list_of_lists_of_coordinate_tuples(element: Any) -> bool:
    return (isinstance(element, list) and 
            all(is_list_of_coordinate_tuples(item) for item in element))

def check_and_convert(element: Union[Tuple[int, int], List[Tuple[int, int]], List[List[Tuple[int, int]]]]) -> List[List[Tuple[int, int]]]:
    if is_coordinate_tuple(element):        
        return [[element]]
    elif is_list_of_coordinate_tuples(element):        
        return [element]
    elif is_list_of_lists_of_coordinate_tuples(element):
        return element
    else:
        raise ValueError("Input must be a coordinate tuple, list of coordinate tuples, or list of lists of coordinate tuples.")

def add_step(l_in: Union[Tuple[int, int], List[Tuple[int, int]], List[List[Tuple[int, int]]]]) -> List[List[Tuple[int, int]]]:
    l_in = check_and_convert(l_in)
    l_out = []
    for t in l_in:
        x, y = t[-1]
        for (m, n) in all_knight_moves(x, y):
            l_out += [t + [(m, n)]]
    return l_out

def get_all_sequences(
    x: int, 
    y: int, 
    n_steps: int, 
    location_list: Optional[List[Tuple[int, int]]] = None, 
    max_hit: Optional[int] = None, 
    filter: Optional[Callable[[List[Tuple[int, int]]], bool]] = None
) -> List[List[Tuple[int, int]]]:
    # Determine if hit count filtering should be applied (both location_list and max_hit must be provided)
    check_sequence_hit_count_cond = (location_list is not None) and (max_hit is not None)
    if check_sequence_hit_count_cond:
        assert ((location_list is not None) and is_list_of_coordinate_tuples(location_list)), f"'location_list' must be a list of coordinate tuples"
        assert ((max_hit is not None) and (max_hit > 0) and isinstance(max_hit, int)), f"'max_hit' must be positive integer"

    sequences = [(x, y)]

    if filter is None:
        def filter_cond(sequence: List[Tuple[int, int]]) -> bool:
            return True        
    else:
        filter_cond = filter

    if filter_cond(sequences):
        for _ in range(n_steps):
            if check_sequence_hit_count_cond:
                sequences = [seq for seq in add_step(sequences) 
                        if filter_cond(seq) and 
                        count_sequence_hit_location_list(seq, location_list) <= max_hit]
            else:
                sequences = [seq for seq in add_step(sequences) if filter_cond(seq)]
        return sequences
    else:
        return []
