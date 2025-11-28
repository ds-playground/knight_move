def has_at_most_two_vowels(text: str) -> bool:
    """
    Check if a string contains at most two vowels.
    
    This function counts vowels (a, e, i, o, u) in a string, regardless of case,
    and returns True if there are 2 or fewer vowels present.
    
    Parameters:
    -----------
    text : str
        The input string to check for vowels. Can be any string including empty string.
    
    Returns:
    --------
    bool
        True if the string contains 2 or fewer vowels, False if it contains 3 or more vowels
    
    Examples:
    ---------
    >>> has_at_most_two_vowels("hello")
    True  # Contains 'e' and 'o' (2 vowels)
    
    >>> has_at_most_two_vowels("world")
    True  # Contains only 'o' (1 vowel)
    
    >>> has_at_most_two_vowels("PYTHON")
    True  # Contains only 'O' (1 vowel)
    
    >>> has_at_most_two_vowels("beautiful")
    False  # Contains 'e', 'a', 'u', 'i', 'u' (5 vowels)
    
    >>> has_at_most_two_vowels("bcdfg")
    True  # Contains no vowels
    
    >>> has_at_most_two_vowels("")
    True  # Empty string has no vowels
    
    >>> has_at_most_two_vowels("programming")
    False  # Contains 'o', 'a', 'i' (3 vowels)
    
    Notes:
    ------
    - Case-insensitive: both uppercase and lowercase vowels are counted
    - Duplicate vowels are counted separately (e.g., "book" has 2 vowels)
    - Only English vowels (a, e, i, o, u) are considered
    - Empty string returns True (0 vowels <= 2)
    
    See Also:
    ---------
    count_vowels : Get the exact number of vowels in a string
    """
    # Define vowels (both lowercase and uppercase for efficiency)
    vowels = "aeiouAEIOU"
    
    # Count vowels in the text
    vowel_count = sum(1 for char in text if char in vowels)
    
    # Return True if 2 or less vowels found
    return vowel_count <= 2


def count_vowels(text: str) -> int:
    """
    Count the total number of vowels in a string.
    
    This helper function returns the exact count of vowels found in the input string.
    It's useful for debugging, analysis, or when you need the precise vowel count
    rather than just a boolean check.
    
    Parameters:
    -----------
    text : str
        The input string to count vowels in. Can be any string including empty string.
    
    Returns:
    --------
    int
        The total number of vowels found in the string. Returns 0 for strings
        with no vowels or empty strings.
    
    Examples:
    ---------
    >>> count_vowels("hello")
    2  # 'e' and 'o'
    
    >>> count_vowels("beautiful")
    5  # 'e', 'a', 'u', 'i', 'u'
    
    >>> count_vowels("bcdfg")
    0  # No vowels
    
    >>> count_vowels("EDUCATION")
    5  # 'E', 'u', 'a', 'i', 'o' (case-insensitive)
    
    >>> count_vowels("")
    0  # Empty string
    
    >>> count_vowels("aeiou")
    5  # All vowels
    
    Notes:
    ------
    - Case-insensitive: both uppercase and lowercase vowels are counted
    - Duplicate vowels are counted separately (e.g., "book" returns 2)
    - Only English vowels (a, e, i, o, u) are considered
    - Non-alphabetic characters are ignored
    
    See Also:
    ---------
    has_at_most_two_vowels : Check if string has 2 or fewer vowels
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":

    # Test the functions with various examples
    print("Testing vowel counting functions:")
    print()

    test_strings = [
        "hello",        # 2 vowels: e, o
        "world",        # 1 vowel: o
        "PYTHON",       # 1 vowel: O
        "beautiful",    # 5 vowels: e, a, u, i, u
        "bcdfg",        # 0 vowels
        "",             # 0 vowels (empty string)
        "aeiou",        # 5 vowels: all vowels
        "programming",  # 3 vowels: o, a, i
        "rhythm",       # 0 vowels
        "Education",    # 5 vowels: E, u, a, i, o
    ]

    for test_str in test_strings:
        vowel_count = count_vowels(test_str)
        has_multiple = has_at_most_two_vowels(test_str)
        
        print(f"'{test_str}': {vowel_count} vowels, has ≤2 vowels: {has_multiple}")
    print("\nSummary:")
    strings_with_at_most_2_vowels = [s for s in test_strings if has_at_most_two_vowels(s)]
    print(f"Strings with ≤2 vowels: {strings_with_at_most_2_vowels}")
    print(f"Total: {len(strings_with_at_most_2_vowels)} out of {len(test_strings)} strings")