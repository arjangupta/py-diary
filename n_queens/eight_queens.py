def main():
    pass

class ChessSquare:
    def __init__(self, alpha, num):
        self.alpha = alpha
        self.num   = num

class QueenChessBoard:
    def place_queen(self, alpha, num):
        # Place a queen here

    def check_square(self, alpha, num):
        # Check if alpha, num is even valid
        if alpha not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False
        
        if num not in list(range(1:9)):
            return False

        # Check if this square is in an already placed queen's path


if __name__ == "__main__":
    main()