# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

def downward_block_diagonal(n):
    """
    Generate a downward block diagonal of size n.

    :param n: Size of the diagonal
    :return: A string representation of the diagonal
    """
    diagonal = ""
    for i in range(n):
        # Add the necessary spaces at the beginning of each block
        diagonal += "  " * i
        # Add the top of the block
        diagonal += "+-+\n"
        # Add the middle of the block
        diagonal += "  " * i + "| |\n"
        # Add the bottom of the block only if it's not the last one
        if i != n - 1:
            diagonal += "  " * i + "+-+-+\n"
    
    # Add the bottom of the last block
    diagonal += "+-+\n"

    return diagonal

# Mihir Katyal
# mkatyal@uci.edu
# 19099879
