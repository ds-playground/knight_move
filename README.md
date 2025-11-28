# Knight's Tour Path Analysis

A comprehensive Python project for analyzing knight move patterns on a customizable grid with constraints and filtering capabilities.

## Project Overview

This project implements a sophisticated knight move analysis system that generates and validates paths on a 4x5 grid containing letters and numbers. The system uses pure Python data structures (tuples and lists) without external dependencies like pandas or numpy. It can apply various constraints including boundary checking, position avoidance, and visit limitations to specific coordinates.

## Features

### Core Functionality
- **Knight Move Generation**: Generate all possible knight moves from any position
- **Path Analysis**: Create and analyze multi-step knight move paths
- **Constraint Filtering**: Apply boundary, avoidance, and visit limit constraints
- **Vowel Tracking**: Special handling for vowel positions with hit counting
- **Grid Analysis**: Comprehensive coordinate-based analysis with position identification
- **Pure Python Implementation**: No external dependencies - uses native tuple/list data structures

### Advanced Capabilities
- **Type Safety**: Full type annotations throughout the codebase
- **Performance Analysis**: Built-in timing and performance measurement tools
- **Modular Design**: Clean separation of concerns across multiple modules
- **Lightweight Architecture**: Pure Python implementation with minimal dependencies
- **Coordinate-Based Processing**: Efficient tuple-based data structures
- **Comprehensive Testing**: Extensive test cases and validation functions

## Project Structure

```
knight-move-analysis/
├── main.py                     # Main analysis script and entry point
├── README.md                   # Project documentation (this file)
├── requirements.txt            # Python dependencies
├── knight_move_on_key_pad.ipynb # Jupyter notebook for interactive analysis
└── src/                        # Source code modules
    ├── __init__.py            # Package initialization
    ├── knight_move.py         # Core knight movement algorithms
    ├── path_check.py          # Path validation and constraint checking
    ├── path_create.py         # Path generation and filtering systems
    ├── positions.py           # Coordinate analysis and position utilities
    ├── table_data.py          # Grid data creation and coordinate management
    ├── vowel_check.py         # Basic vowel counting and validation
    └── vowel_check_additional.py # Extended vowel analysis functions
```

## Installation

### Prerequisites
- Python 3.9 or higher (with typing support)
- No external dependencies required (pure Python implementation)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd knight-move-analysis
   ```

2. **Install dependencies** (optional - only needed for Jupyter notebook)
   ```bash
   pip install -r requirements.txt  # Only for Jupyter notebook support
   ```

3. **Verify installation**
   ```bash
   python main.py
   ```

## Usage

### Running the Main Analysis

Execute the complete knight path analysis:

```bash
python main.py
```

This will:
- Create a 4x5 coordinate grid with letters A-O and numbers 1-3
- Generate coordinate tuples in format (row, column, value)
- Identify vowel positions and missing coordinates
- Generate all valid 9-move knight paths from each starting position
- Apply constraints (boundary limits, position avoidance, vowel visit limits)
- Display comprehensive analysis results

### Interactive Analysis

For interactive exploration, use the Jupyter notebook:

```bash
jupyter notebook knight_move_on_key_pad.ipynb
```

### Module Usage Examples

#### Knight Move Generation
```python
from src.knight_move import knight_move, all_knight_moves

# Single knight move
final_pos = knight_move(3, 3, 1)  # Move from (3,3) in direction 1
print(f"Final position: {final_pos}")

# All possible moves
all_moves = all_knight_moves(3, 3)
print(f"All possible moves: {all_moves}")
```

#### Path Generation with Constraints
```python
from src.path_create import get_all_paths

# Generate 3-step paths with custom filter
def boundary_filter(path):
    return all(1 <= x <= 4 and 1 <= y <= 5 for x, y in path)

paths = get_all_paths(
    x=2, y=2, n_steps=3,
    location_list=[(2, 3), (4, 1)],  # Special positions
    max_hit=1,                       # Maximum visits to special positions
    filter=boundary_filter           # Custom constraint function
)
```

#### Coordinate-Based Analysis
```python
from src.table_data import get_table_data
from src.positions import get_vowel_positions, get_missing_positions, get_coordinate_bounds

# Create and analyze the coordinate grid
coordinate_data = get_table_data()  # Returns List[Tuple[int, int, str]]
vowel_positions = get_vowel_positions(coordinate_data)
missing_positions = get_missing_positions(coordinate_data)
bounds = get_coordinate_bounds(coordinate_data)

print(f"Grid data format: {coordinate_data[:3]}...")  # Show first 3 coordinates
print(f"Vowels found at: {vowel_positions}")
print(f"Missing positions: {missing_positions}")
print(f"Coordinate bounds: {bounds}")
```

## Algorithm Details

### Knight Move System
- **Standard Chess Rules**: Implements L-shaped moves (2+1 or 1+2 squares)
- **8-Direction Support**: All eight possible knight move directions
- **Coordinate System**: Integer-based (x, y) coordinate pairs

### Path Generation Algorithm
- **Exponential Expansion**: Each path can branch into 8 new paths per step
- **Step-by-Step Processing**: Iterative expansion with filtering at each stage
- **Memory Optimization**: Filters applied during generation to prevent explosion

### Constraint System
- **Boundary Validation**: Ensures paths stay within specified coordinate ranges
- **Position Avoidance**: Excludes paths that visit forbidden coordinates
- **Visit Counting**: Tracks and limits visits to special positions
- **Custom Filters**: Support for user-defined validation functions

## Configuration Options

### Grid Customization
Modify `src/table_data.py` to change:
- Grid dimensions (currently 4x5)
- Cell contents (letters, numbers, symbols)
- Coordinate ranges and values
- Tuple format: (row, column, value)

### Analysis Parameters
Adjust in `main.py`:
- **Path Length**: Change `step_i` for different analysis depths
- **Vowel Visit Limit**: Modify `max_hit` parameter
- **Starting Positions**: Customize the range iteration
- **Constraint Functions**: Define custom validation logic

### Performance Tuning
- **Early Filtering**: Apply constraints as early as possible
- **Path Length Limits**: Shorter paths reduce exponential growth
- **Selective Starting Points**: Analyze subset of positions for faster results

## Performance Characteristics

### Time Complexity
- **Path Generation**: O(8^n) where n is the number of steps
- **Constraint Checking**: O(p×c) where p is paths and c is constraint cost
- **Overall**: Exponential growth managed through strategic filtering

### Space Complexity
- **Path Storage**: O(8^n × path_length) for storing all valid paths
- **Memory Management**: Paths filtered at each step to control memory usage

### Scalability Recommendations
- **Step Limits**: Keep path length ≤ 12 for reasonable performance
- **Aggressive Filtering**: Use strict constraints to reduce path explosion
- **Parallel Processing**: Consider multiprocessing for large-scale analysis

## Contributing

### Code Standards
- **Type Annotations**: All functions must include comprehensive type hints
- **Documentation**: Docstrings required for all public functions
- **Testing**: Include test cases for new functionality
- **Performance**: Consider algorithmic complexity in implementations

### Development Setup
1. Install development dependencies: `pip install -r requirements-dev.txt`
2. Run tests: `python -m pytest tests/`
3. Check type annotations: `mypy src/`
4. Format code: `black src/`

## Examples and Use Cases

### Game Development
- **Pathfinding AI**: Knight movement in chess-like games
- **Puzzle Solving**: Knight's tour and similar challenges
- **Movement Validation**: Legal move checking in grid-based games

### Mathematical Analysis
- **Combinatorial Studies**: Path counting and enumeration
- **Graph Theory**: Knight's graph analysis and properties
- **Optimization Problems**: Constrained pathfinding scenarios

### Educational Applications
- **Algorithm Learning**: Backtracking and constraint satisfaction
- **Chess Instruction**: Knight movement pattern understanding
- **Programming Concepts**: Recursion, filtering, and optimization

## Troubleshooting

### Common Issues

**Memory Errors with Large Paths**
- Reduce `step_i` (path length) in main.py
- Apply more aggressive filtering constraints
- Consider analyzing subset of starting positions

**Import Errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python path and virtual environment setup
- Verify all source files are present in src/ directory

**Performance Issues**
- Monitor exponential growth: 8^n paths possible per starting position
- Use filtering to eliminate invalid paths early
- Consider parallel processing for multiple starting points

### Debug Mode
Enable detailed logging by modifying filter functions to print intermediate results:

```python
def debug_filter(path):
    result = your_constraint_check(path)
    if not result:
        print(f"Path rejected: {path}")
    return result
```

## License

This project is available under the MIT License. See LICENSE file for details.

## Support and Contact

For questions, issues, or contributions:
- Create an issue in the project repository
- Review the code documentation and examples
- Check existing test cases for usage patterns

## Version History

- **v1.0.0**: Initial release with core knight move analysis
- **v1.1.0**: Added comprehensive type annotations
- **v1.2.0**: Enhanced documentation and performance optimizations
- **v1.3.0**: Extended vowel analysis and constraint systems