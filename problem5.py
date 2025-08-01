problem = "problem5"
student_name = "Beemnet_Amdissa_Teshome"
student_number = "T0338757"

import numpy as np
import random
import matplotlib.pyplot as plt

def basic_knights_tour():
    # your code here, generates a knights tour and
    # displays it visually to the user.

    board = np.zeros((8, 8), dtype=int)

    horizontal = [2, 1, -1, -2, -2, -1, 1, 2]
    vertical = [1, 2, 2, 1, -1, -2, -2, -1]

    row, col = 4, 3
    board[row, col] = 1

    move_count = 2

    while True:
        possible_moves =  []

        for i in range(8):
            new_row, new_col = row + vertical[i], col + horizontal[i]

            # check if position is unvisited and not out of bound...
            if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row, new_col] == 0:
                possible_moves.append((new_row, new_col))
        
        if not possible_moves:      # if no more valid moves
            break
        
        row, col = random.choice(possible_moves)
        board[row, col] = move_count
        move_count += 1

    print_knight_tour(board)
    #visualise_knight_tour(board)

def print_knight_tour(board):

    for row in board:
        print(" ".join(f"{num:3}" for num in row))
        
basic_knights_tour()
#print('basic_knights_tour not implemented')


# simulating kinght tour 1,000,000 times
def knight_tour_simulation(num_tours=1_000_000):
    
    results = []  # Store number of moves per tour
    board_size = 8

    # Legal knight moves
    horizontal = [2, 1, -1, -2, -2, -1, 1, 2]
    vertical = [1, 2, 2, 1, -1, -2, -2, -1]

    for _ in range(num_tours):
        board = np.zeros((board_size, board_size), dtype=int)
        row, col = 4, 3  # Start position
        board[row, col] = 1
        move_count = 2

        while True:
            possible_moves =  []

            for i in range(8):
                new_row, new_col = row + vertical[i], col + horizontal[i]

                # check if position is unvisited and not out of bound...
                if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row, new_col] == 0:
                    possible_moves.append((new_row, new_col))
            
            if not possible_moves:      # if no more valid moves
                break
            
            row, col = random.choice(possible_moves)
            board[row, col] = move_count
            move_count += 1

        results.append(move_count - 1)  # Store the total moves made

    return results

def print_knight_tour(board):

    for row in board:
        print(" ".join(f"{num:3}" for num in row))

def visualize_results(results):
    
    plt.figure(figsize=(10, 5))
    
    # Histogram of move counts
    plt.hist(results, bins=range(1, 65), edgecolor="black", alpha=0.7)
    plt.xlabel("Number of Moves Before Stuck")
    plt.ylabel("Frequency")
    plt.title("Knight's Tour: Distribution of Move Counts Over 1,000,000 Runs")
    plt.show()

# Run simulation and visualize
results = knight_tour_simulation(1000000)
visualize_results(results)


# knight tour simulation using the heuristic approach

# Possible knight moves
horizontal = [2, 1, -1, -2, -2, -1, 1, 2]
vertical = [1, 2, 2, 1, -1, -2, -2, -1]

def initialize_reachability():
    """Creates the reachability table"""
    reachability = np.array([
        [2, 3, 4, 4, 4, 4, 3, 2],
        [3, 4, 6, 6, 6, 6, 4, 3],
        [4, 6, 8, 8, 8, 8, 6, 4],
        [4, 6, 8, 8, 8, 8, 6, 4],
        [4, 6, 8, 8, 8, 8, 6, 4],
        [4, 6, 8, 8, 8, 8, 6, 4],
        [3, 4, 6, 6, 6, 6, 4, 3],
        [2, 3, 4, 4, 4, 4, 3, 2]
    ])
    return reachability

def get_valid_moves(board, row, col):
    """Returns a list of valid next moves."""
    moves = []
    for i in range(8):
        new_row, new_col = row + vertical[i], col + horizontal[i]
        if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row, new_col] == 0:
            moves.append((new_row, new_col))
    return moves

def update_reachability(reachability, row, col):
    """Decreases the reachability count for squares affected by the knight's move."""
    for i in range(8):
        new_row, new_col = row + vertical[i], col + horizontal[i]
        if 0 <= new_row < 8 and 0 <= new_col < 8 and reachability[new_row, new_col] > 0:
            reachability[new_row, new_col] -= 1

def heuristic_knight_tour():
    """Runs the knight's tour using the heuristic approach"""
    board = np.zeros((8, 8), dtype=int)
    reachability = initialize_reachability()
    
    row, col = 4, 3  # Starting position
    board[row, col] = 1
    update_reachability(reachability, row, col)
    
    for move_count in range(2, 65):  # Maximum 64 moves
        valid_moves = get_valid_moves(board, row, col)
        
        if not valid_moves:
            break  # No more legal moves

        # Choose move with lowest reachability value
        min_reach = min(reachability[r, c] for r, c in valid_moves)
        best_moves = [(r, c) for r, c in valid_moves if reachability[r, c] == min_reach]
        row, col = random.choice(best_moves)

        board[row, col] = move_count
        update_reachability(reachability, row, col)

    return move_count - 1

def run_heuristic_simulation(num_tours=1000000):

    results = []

    for _ in range(num_tours):
        moves = heuristic_knight_tour()
        results.append(moves)

    return results

def visualize_results(results):
    """Visualizes the results"""
    plt.figure(figsize=(10, 5))
    
    # Histogram of move counts
    plt.hist(results, bins=range(1, 65), edgecolor="black", alpha=0.7)
    plt.xlabel("Number of Moves Before Stuck")
    plt.ylabel("Frequency")
    plt.title("Heuristic Knight's Tour: Distribution of Move Counts Over 1,000,000 Runs")
    plt.show()


def print_knight_tour(board):

    for row in board:
        print(" ".join(f"{num:3}" for num in row))

# Run and visualize
results = run_heuristic_simulation(1000000)
visualize_results(results)
board = heuristic_knight_tour()
print_knight_tour(board)

