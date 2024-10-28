from tictactoe_rx2255.game import initialize_board, make_move, check_winner, reset_game

def test_initialize_board():
    """Test that the board is initialized as a 3x3 grid of empty spaces."""
    board = initialize_board()
    
    # check if the board is 3x3
    assert len(board) == 3, "The board should have 3 rows."
    assert all(len(row) == 3 for row in board), "Each row should have 3 columns."
    
    # check if the cell in the board is an empty space
    for row in board:
        for cell in row:
            assert cell == ' ', "Each cell should be initialized with an empty space."


def test_make_move_valid():
    """Test that make_move successfully places a player's symbol on an empty cell."""
    
    # pre-specified board configuration
    board = [['X', ' ', 'O'],
             [' ', 'X', ' '],
             ['O', ' ', ' ']]
    
    # test valid move for player 'X' on an empty cell
    move_successful = make_move(board, 1, 2, 'X')  # 'X' in row 1, col 2 (which is currently empty)
    assert move_successful == True, "The move should be successful."
    assert board[1][2] == 'X', "The board should have 'X' at position (1, 2)."
    
    # test valid move for player 'O' on an empty cell
    move_successful = make_move(board, 2, 1, 'O')  # 'O' in row 2, col 1 (which is currently empty)
    assert move_successful == True, "The move should be successful."
    assert board[2][1] == 'O', "The board should have 'O' at position (2, 1)."

def test_make_move_invalid():
    """Test that make_move does not overwrite an occupied cell and returns False."""
    
    # pre-specified board configuration with some occupied cells
    board = [['X', ' ', 'O'],
             [' ', 'X', ' '],
             ['O', ' ', ' ']]
    
    # try to place 'O' in a cell already occupied by 'X'
    move_successful = make_move(board, 0, 0, 'O')  # (0, 0) is occupied by 'X'
    assert move_successful == False, "Move should fail because the cell is already occupied."
    assert board[0][0] == 'X', "The board should not overwrite the existing 'X' at (0, 0)."
    
    # try to place 'X' in a cell already occupied by 'O'
    move_successful = make_move(board, 2, 0, 'X')  # (2, 0) is occupied by 'O'
    assert move_successful == False, "Move should fail because the cell is already occupied."
    assert board[2][0] == 'O', "The board should not overwrite the existing 'O' at (2, 0)."

def test_game_integration():
    """Integration test for initializing the board, making moves, checking the winner, and resetting the game."""
    
    board = initialize_board()
    
    # verify that the board is empty 
    assert all(cell == ' ' for row in board for cell in row), "The board should be empty after initialization."
    
    # multiple moves
    assert make_move(board, 0, 0, 'X') == True, "Move for 'X' at (0, 0) should be successful."
    assert make_move(board, 0, 1, 'O') == True, "Move for 'O' at (0, 1) should be successful."
    assert make_move(board, 1, 0, 'X') == True, "Move for 'X' at (1, 0) should be successful."
    assert make_move(board, 1, 1, 'O') == True, "Move for 'O' at (1, 1) should be successful."
    assert make_move(board, 2, 0, 'X') == True, "Move for 'X' at (2, 0) should be successful."
    
    # check for a winner after X's winning move
    assert check_winner(board) == 'X', "Player 'X' should be the winner after completing the first column."
    
    # reset the game
    board = reset_game()
    
    # verify the board is reset to the initial empty state
    assert all(cell == ' ' for row in board for cell in row), "The board should be empty after resetting the game."
