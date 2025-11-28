def has_exactly_two_vowels(text: str) -> bool:
    """
    Check if a string contains exactly two vowels.
    
    This function counts vowels (a, e, i, o, u) in a string, regardless of case,
    and returns True if there are exactly 2 vowels present.
    
    Parameters:
    -----------
    text : str
        The input string to check for vowels
    
    Returns:
    --------
    bool
        True if the string contains exactly 2 vowels, False otherwise
    
    Examples:
    ---------
    >>> has_exactly_two_vowels("hello")
    True  # Contains 'e' and 'o' (exactly 2 vowels)
    
    >>> has_exactly_two_vowels("world")
    False  # Contains only 'o' (1 vowel)
    
    >>> has_exactly_two_vowels("PYTHON")
    False  # Contains only 'O' (1 vowel)
    
    >>> has_exactly_two_vowels("beautiful")
    False  # Contains 'e', 'a', 'u', 'i', 'u' (5 vowels)
    
    >>> has_exactly_two_vowels("book")
    True  # Contains 'o' and 'o' (exactly 2 vowels)
    
    >>> has_exactly_two_vowels("bcdfg")
    False  # Contains no vowels
    
    >>> has_exactly_two_vowels("")
    False  # Empty string has no vowels
    
    >>> has_exactly_two_vowels("code")
    True  # Contains 'o' and 'e' (exactly 2 vowels)
    
    Notes:
    ------
    - Case-insensitive: both uppercase and lowercase vowels are counted
    - Duplicate vowels are counted separately (e.g., "book" has 2 vowels)
    - Only English vowels (a, e, i, o, u) are considered
    """
    # Define vowels (both lowercase and uppercase for efficiency)
    vowels = "aeiouAEIOU"
    
    # Count vowels in the text
    vowel_count = sum(1 for char in text if char in vowels)
    
    # Return True if exactly 2 vowels found
    return vowel_count == 2

def has_exactly_two_different_vowels(text: str) -> bool:
    """
    Check if a string contains exactly two different (unique) vowels.
    
    This function identifies unique vowels (a, e, i, o, u) in a string, regardless of case,
    and returns True if there are exactly 2 different vowels present. Unlike
    has_exactly_two_vowels(), this function counts unique vowels, not total occurrences.
    
    Parameters:
    -----------
    text : str
        The input string to check for unique vowels
    
    Returns:
    --------
    bool
        True if the string contains exactly 2 different vowels, False otherwise
    
    Examples:
    ---------
    >>> has_exactly_two_different_vowels("hello")
    True  # Contains 'e' and 'o' (2 different vowels)
    
    >>> has_exactly_two_different_vowels("book")
    False  # Contains only 'o' (1 different vowel)
    
    >>> has_exactly_two_different_vowels("education")
    False  # Contains 'e', 'u', 'a', 'i', 'o' (5 different vowels)
    
    >>> has_exactly_two_different_vowels("beautiful")
    False  # Contains 'e', 'a', 'u', 'i' (4 different vowels)
    
    >>> has_exactly_two_different_vowels("ueueue")
    True  # Contains 'u' and 'e' (2 different vowels, despite repetition)
    
    >>> has_exactly_two_different_vowels("aeiou")
    False  # Contains all 5 different vowels
    
    >>> has_exactly_two_different_vowels("bcdfg")
    False  # Contains no vowels
    
    >>> has_exactly_two_different_vowels("programming")
    False  # Contains 'o', 'a', 'i' (3 different vowels)
    
    >>> has_exactly_two_different_vowels("code")
    True  # Contains 'o' and 'e' (2 different vowels)
    
    Notes:
    ------
    - Case-insensitive: both uppercase and lowercase vowels are treated the same
    - Counts unique vowels only: "aaaeee" has 2 different vowels (a, e)
    - Only English vowels (a, e, i, o, u) are considered
    - Useful for linguistic analysis where vowel diversity matters more than frequency
    """
    # Define vowels for checking
    vowels = "aeiouAEIOU"
    
    # Find unique vowels in the text (case-insensitive)
    unique_vowels = set(char.lower() for char in text if char in vowels)
    
    # Return True if exactly 2 different vowels found
    return len(unique_vowels) == 2

def get_unique_vowels(text: str) -> set[str]:
    """
    Get the set of unique vowels in a string.
    
    This helper function returns the actual set of unique vowels found in the input string,
    which is useful for debugging, analysis, or when you need to see which specific vowels
    are present rather than just counting them.
    
    Parameters:
    -----------
    text : str
        The input string to analyze for unique vowels. Can be any string including empty string.
    
    Returns:
    --------
    set[str]
        Set of unique vowels found in the string (all lowercase).
        Returns empty set if no vowels are found.
    
    Examples:
    ---------
    >>> get_unique_vowels("hello")
    {'e', 'o'}
    
    >>> get_unique_vowels("beautiful")
    {'a', 'e', 'i', 'u'}
    
    >>> get_unique_vowels("EDUCATION")
    {'a', 'e', 'i', 'o', 'u'}  # All vowels, case-insensitive
    
    >>> get_unique_vowels("bcdfg")
    set()  # No vowels
    
    >>> get_unique_vowels("aaaeeee")
    {'a', 'e'}  # Duplicates removed
    
    >>> get_unique_vowels("")
    set()  # Empty string
    
    Notes:
    ------
    - Case-insensitive: returns all vowels in lowercase
    - Duplicates are automatically removed (set behavior)
    - Only English vowels (a, e, i, o, u) are considered
    - Non-alphabetic characters are ignored
    - Useful for vowel diversity analysis
    
    See Also:
    ---------
    has_exactly_two_different_vowels : Check for exactly 2 unique vowels
    has_at_least_two_different_vowels : Check for 2+ unique vowels
    """
    vowels = "aeiouAEIOU"
    return set(char.lower() for char in text if char in vowels)

def has_at_least_two_different_vowels(text: str) -> bool:
    """
    Check if a string contains at least two different (unique) vowels.
    
    This function identifies unique vowels (a, e, i, o, u) in a string, regardless of case,
    and returns True if there are at least 2 different vowels present. This function
    focuses on vowel diversity rather than total vowel count.
    
    Parameters:
    -----------
    text : str
        The input string to check for unique vowels
    
    Returns:
    --------
    bool
        True if the string contains 2 or more different vowels, False otherwise
    
    Examples:
    ---------
    >>> has_at_least_two_different_vowels("hello")
    True  # Contains 'e' and 'o' (2 different vowels)
    
    >>> has_at_least_two_different_vowels("book")
    False  # Contains only 'o' (1 different vowel)
    
    >>> has_at_least_two_different_vowels("beautiful")
    True  # Contains 'e', 'a', 'u', 'i' (4 different vowels)
    
    >>> has_at_least_two_different_vowels("education")
    True  # Contains 'e', 'u', 'a', 'i', 'o' (5 different vowels)
    
    >>> has_at_least_two_different_vowels("aaaeeee")
    True  # Contains 'a' and 'e' (2 different vowels, despite repetition)
    
    >>> has_at_least_two_different_vowels("programming")
    True  # Contains 'o', 'a', 'i' (3 different vowels)
    
    >>> has_at_least_two_different_vowels("rhythm")
    False  # Contains no vowels
    
    >>> has_at_least_two_different_vowels("cat")
    False  # Contains only 'a' (1 different vowel)
    
    >>> has_at_least_two_different_vowels("queue")
    True  # Contains 'u' and 'e' (2 different vowels)
    
    >>> has_at_least_two_different_vowels("")
    False  # Empty string has no vowels
    
    Notes:
    ------
    - Case-insensitive: both uppercase and lowercase vowels are treated the same
    - Counts unique vowels only: "aaaeeeiii" has 3 different vowels (a, e, i)
    - Only English vowels (a, e, i, o, u) are considered
    - Useful for linguistic analysis focusing on vowel diversity
    - Returns True for words with 2, 3, 4, or 5 different vowels
    """
    # Define vowels for checking
    vowels = "aeiouAEIOU"
    
    # Find unique vowels in the text (case-insensitive)
    unique_vowels = set(char.lower() for char in text if char in vowels)
    
    # Return True if at least 2 different vowels found
    return len(unique_vowels) >= 2



if __name__ == "__main__":

    # Test the new function
    print("Testing has_exactly_two_vowels function:")
    print()

    test_cases = [
        "hello",        # 2 vowels: e, o -> True
        "world",        # 1 vowel: o -> False
        "PYTHON",       # 1 vowel: O -> False
        "beautiful",    # 5 vowels: e, a, u, i, u -> False
        "book",         # 2 vowels: o, o -> True
        "code",         # 2 vowels: o, e -> True
        "cat",          # 1 vowel: a -> False
        "bcdfg",        # 0 vowels -> False
        "",             # 0 vowels -> False
        "aeiou",        # 5 vowels -> False
        "up",           # 1 vowel: u -> False
        "tree",         # 2 vowels: e, e -> True
    ]

    for test_word in test_cases:
        result = has_exactly_two_vowels(test_word)
        vowel_count = sum(1 for char in test_word if char.lower() in "aeiou")
        print(f"'{test_word}': {vowel_count} vowels -> has_exactly_two_vowels = {result}")

    print()
    exactly_two_vowel_words = [word for word in test_cases if has_exactly_two_vowels(word)]
    print(f"Words with exactly 2 vowels: {exactly_two_vowel_words}")
    print(f"Count: {len(exactly_two_vowel_words)} out of {len(test_cases)} test cases")

    # Test the new function with various examples
    print("Testing has_exactly_two_different_vowels function:")
    print()

    test_cases = [
        "hello",        # e, o -> 2 different -> True
        "book",         # o -> 1 different -> False
        "code",         # o, e -> 2 different -> True
        "beautiful",    # e, a, u, i -> 4 different -> False
        "education",    # e, u, a, i, o -> 5 different -> False
        "programming",  # o, a, i -> 3 different -> False
        "queueue",      # u, e -> 2 different -> True
        "aeiou",        # a, e, i, o, u -> 5 different -> False
        "bcdfg",        # none -> 0 different -> False
        "cat",          # a -> 1 different -> False
        "tree",         # e -> 1 different -> False
        "area",         # a, e -> 2 different -> True
        "about",        # a, o, u -> 3 different -> False
        "auto",         # a, u, o -> 3 different -> False
        "queue",        # u, e -> 2 different -> True
        "",             # none -> 0 different -> False
    ]

    for test_word in test_cases:
        unique_vowels = get_unique_vowels(test_word)
        result = has_exactly_two_different_vowels(test_word)
        vowel_list = sorted(list(unique_vowels))
        
        print(f"'{test_word}': {vowel_list} ({len(unique_vowels)} different) -> {result}")

    print()
    two_different_vowel_words = [word for word in test_cases if has_exactly_two_different_vowels(word)]
    print(f"Words with exactly 2 different vowels: {two_different_vowel_words}")
    print(f"Count: {len(two_different_vowel_words)} out of {len(test_cases)} test cases")

    print()
    print("Comparison: Total vowels vs Different vowels")
    print("Word".ljust(12), "Total".ljust(6), "Different".ljust(10), "=2 Total".ljust(9), "=2 Different")
    print("-" * 55)
    for word in ["hello", "book", "queue", "beautiful", "area"]:
        total_vowels = sum(1 for char in word if char.lower() in "aeiou")
        different_vowels = len(get_unique_vowels(word))
        has_2_total = has_exactly_two_vowels(word)
        has_2_different = has_exactly_two_different_vowels(word)
        
        print(f"{word.ljust(12)} {str(total_vowels).ljust(6)} {str(different_vowels).ljust(10)} {str(has_2_total).ljust(9)} {has_2_different}")


    # Test the new function with comprehensive examples
    print("Testing has_at_least_two_different_vowels function:")
    print()

    test_cases = [
        "hello",        # e, o -> 2 different -> True
        "book",         # o -> 1 different -> False
        "code",         # o, e -> 2 different -> True
        "beautiful",    # e, a, u, i -> 4 different -> True
        "education",    # e, u, a, i, o -> 5 different -> True
        "programming",  # o, a, i -> 3 different -> True
        "aaaeeee",      # a, e -> 2 different -> True
        "aeiou",        # a, e, i, o, u -> 5 different -> True
        "rhythm",       # none -> 0 different -> False
        "cat",          # a -> 1 different -> False
        "tree",         # e -> 1 different -> False
        "area",         # a, e -> 2 different -> True
        "about",        # a, o, u -> 3 different -> True
        "queue",        # u, e -> 2 different -> True
        "bcdfg",        # none -> 0 different -> False
        "",             # none -> 0 different -> False
        "world",        # o -> 1 different -> False
        "python",       # o -> 1 different -> False
        "house",        # o, u, e -> 3 different -> True
    ]

    for test_word in test_cases:
        unique_vowels = get_unique_vowels(test_word)
        result = has_at_least_two_different_vowels(test_word)
        vowel_list = sorted(list(unique_vowels))
        
        print(f"'{test_word}': {vowel_list} ({len(unique_vowels)} different) -> {result}")

    print()
    at_least_two_different_vowel_words = [word for word in test_cases if has_at_least_two_different_vowels(word)]
    print(f"Words with at least 2 different vowels: {at_least_two_different_vowel_words}")
    print(f"Count: {len(at_least_two_different_vowel_words)} out of {len(test_cases)} test cases")

    print()
    print("Comprehensive Comparison of Vowel Functions")
    print("Word".ljust(12), "Unique".ljust(8), "≥2 Diff".ljust(8), "=2 Diff".ljust(8), "Total".ljust(6), "≥2 Total".ljust(9), "=2 Total")
    print("-" * 65)
    comparison_words = ["hello", "book", "queue", "beautiful", "area", "cat", "programming"]
    for word in comparison_words:
        unique_vowels = get_unique_vowels(word)
        unique_count = len(unique_vowels)
        total_vowels = sum(1 for char in word if char.lower() in "aeiou")
        
        has_at_least_2_diff = has_at_least_two_different_vowels(word)
        has_exactly_2_diff = has_exactly_two_different_vowels(word)
        has_at_least_2_total = total_vowels >= 2
        has_exactly_2_total = has_exactly_two_vowels(word)
        
        print(f"{word.ljust(12)} {str(unique_count).ljust(8)} {str(has_at_least_2_diff).ljust(8)} {str(has_exactly_2_diff).ljust(8)} {str(total_vowels).ljust(6)} {str(has_at_least_2_total).ljust(9)} {has_exactly_2_total}")
