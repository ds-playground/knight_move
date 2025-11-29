from typing import List, Tuple


def check_inside_bounds(sequence: List[Tuple[int, int]], x_min: int, x_max: int, y_min: int, y_max: int) -> bool:
    for (x, y) in sequence:
        if x < x_min or x > x_max or y < y_min or y > y_max:
            return False
    return True


def check_in_avoided_coordinate(sequence: List[Tuple[int, int]], list_of_coordinates: List[Tuple[int, int]]) -> bool:
    return any((x, y) in list_of_coordinates for (x, y) in sequence)


def check_same_alternate_coordinate_exists(sequence: List[Tuple[int, int]]) -> bool:
    if len(sequence) < 3:
        return False
    return any(sequence[i] == sequence[i-2] for i in range(2, len(sequence)))


def count_sequence_hit_location_list(sequence: List[Tuple[int, int]], location_list: List[Tuple[int, int]]) -> int:
    return sum([1 for coordinate in sequence if coordinate in location_list])


if __name__ == "__main__":
    specific_locations = [(1,1), (1,5), (2,4), (3,5)]
    sequence = [(1, 1), (3, 2), (1, 3), (3, 4), (1, 1)]

    print("Testing count_sequence_hit_location_list function:")
    print(f"Sequence: {sequence}")
    print(f"Target locations: {specific_locations}")

    hit_count = count_sequence_hit_location_list(sequence, specific_locations)
    print(f"Number of hits: {hit_count}")

    print("\nDetailed analysis:")
    for i, coord in enumerate(sequence):
        if coord in specific_locations:
            print(f"  Step {i+1}: {coord} - HIT! (matches target location)")
        else:
            print(f"  Step {i+1}: {coord} - miss")
