"""
Author: Tirath Singh Bindra

Description:
This code creates a two-player TicTacToe game using a Python GUI.
It uses the Tkinter library for the graphical user interface.
The backend uses a matrix multiplication algorithm to decide
winners based on scores.

License: GNU General Public License v3.0

Permissions:
- Commercial use, Modification, Distribution, Patent use, Private use

Conditions:
- License and copyright notices must be preserved.
- Changes must be documented and shared with source code.
- Source code of modifications should be available publicly.
- Modifications must carry the same license.

For detailed information, refer to the LICENSE file.
"""

from engine import TicTacToeEngine
from ui import TicTacToeGUI


def main():
    """Initialize and start the TicTacToe application."""
    # Initialize logic
    engine = TicTacToeEngine()

    # Initialize UI and pass engine to it
    app = TicTacToeGUI(engine)

    # Start game
    app.run()


if __name__ == "__main__":
    main()
