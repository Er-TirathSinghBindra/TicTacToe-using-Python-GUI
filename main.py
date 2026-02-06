'''
Author : Tirath Singh Bindra

Description:

This code is to create a two player TicTacToe game using Python GUI. It uses Tkinter library for creating the graphical user interface of game.
For backend an algorithm based on matrix multiplications is used which decide on the basis of scores whether a person has won or not.

License: This code is licensed under GNU General Public License v3.0

It gives following permissions to the user for this code:
Permissions to use:
 Commercial use
 Modification
 Distribution
 Patent use
 Private use

Any commercial use, modification, distribution, patent use and private use of this code can be done only if following coditions are met:
 License and copyright notice : Copyright and license notices must be preserved. Each modification of this code must always carry this same doc report.
 State changes : All the changes made to code must be documented and shared along with source code.
 Disclose source : The source code of modifications should be made publicaly avaialable.
 Same license : Any modifications of code must carry the same license.

For detailed information kindly refer to LICENSE file.
'''
from engine import TicTacToeEngine
from ui import TicTacToeGUI

def main():
    # Initialize logic
    engine = TicTacToeEngine()
    
    # Initialize UI and pass engine to it
    app = TicTacToeGUI(engine)
    
    # Start game
    app.run()

if __name__ == "__main__":
    main()
