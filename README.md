# TicTacToe using Python GUI

A comprehensive, modular TicTacToe game built with Python 3 and the `tkinter` library. This project features a graphical user interface and an efficient win-detection algorithm based on matrix multiplications.

## Features

- **Graphical User Interface**: A clean and interactive game board built using `tkinter`.
- **Modular Architecture**: Separated game logic (`engine.py`), interface (`ui.py`), and constants (`constants.py`) for better maintainability.
- **Smart Win Detection**: Uses `numpy` for efficient board state analysis and win/draw condition checking.
- **Randomized Starts**: The starting player is chosen randomly for each game.
- **Game Reset**: Easily restart the game after a win or draw by clicking the status bar.

## Project Structure

- `main.py`: The entry point of the application.
- `engine.py`: Handles core game mechanics, board state, and win logic.
- `ui.py`: Manages the graphical interface, drawing, and user events.
- `constants.py`: Stores shared constants like player symbols, colors, and dimensions.
- `requirements.txt`: Lists the external dependencies (e.g., `numpy`).

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Er-TirathSinghBindra/TicTacToe-using-Python-GUI.git
   cd TicTacToe-using-Python-GUI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: `tkinter` is usually included with Python standard library. If you are on Linux and it's missing, you may need to install `python3-tk`.*

## Usage

To start the game, run the following command:

```bash
python main.py
```

## How to Play

1. The game will randomly decide which player (`X` or `O`) starts first.
2. Players take turns clicking on the grid to place their markers.
3. The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins.
4. If all squares are filled and no player has won, the game ends in a draw.
5. Once the game ends, click on the status label (e.g., "X has WON!!!") at the bottom to reset and play again.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author

- **Tirath Singh Bindra** - [Profile](https://github.com/Er-TirathSinghBindra)
