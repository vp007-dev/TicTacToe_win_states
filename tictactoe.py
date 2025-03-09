def is_valid_input(board):
    valid_chars = {'X', 'O', '-1'}
    x_count = board.count('X')
    o_count = board.count('O')

    if not all(cell in valid_chars for cell in board):
        return False
    
    if x_count not in {o_count, o_count + 1}:
        return False
    
    return True


def simulate_move(board, index, player):
    new_board = board.copy()
    new_board[index] = player
    return new_board


def check_win(board, player):
    winning_combinations = [
        [0, 1, 2],  
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6]   
    ]
    
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    
    return False


def count_winning_states(board):
    if not is_valid_input(board):
        return "INVALID INPUT"
    
    winning_states = set()

    for first_move in range(9):
        if board[first_move] == "-1":
            board_after_x = simulate_move(board, first_move, "X")

            if check_win(board_after_x, "X"):
                winning_states.add(tuple(board_after_x))
                continue  

            for second_move in range(9):
                if board_after_x[second_move] == "-1":
                    board_after_o = simulate_move(board_after_x, second_move, "O")

                    if check_win(board_after_o, "O"):
                        continue  

                    for third_move in range(9):
                        if board_after_o[third_move] == "-1":
                            board_after_x_again = simulate_move(board_after_o, third_move, "X")

                            if check_win(board_after_x_again, "X"):
                                winning_states.add(tuple(board_after_x_again))
    
    return len(winning_states)


def main():
    board = ['X', 'O', '-1', 'X', '-1', '-1', '-1', 'O', '-1']
    result = count_winning_states(board)
    print(result)


if __name__ == "__main__":
    main()
