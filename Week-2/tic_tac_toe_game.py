import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 4
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 8
CROSS_WIDTH = 10
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Game class
class Game:
    def __init__(self):
        self.board = [["" for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.player = "X"
        self.game_over = False

    def draw_lines(self):
        # Horizontal
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        # Vertical
        for i in range(1, BOARD_COLS):
            pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == "O":
                    pygame.draw.circle(screen, CIRCLE_COLOR,
                                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == "X":
                    start1 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                    end1 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    start2 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                    end2 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                    pygame.draw.line(screen, CROSS_COLOR, start1, end1, CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, start2, end2, CROSS_WIDTH)

    def mark_square(self, row, col):
        self.board[row][col] = self.player

    def is_available(self, row, col):
        return self.board[row][col] == ""

    def check_win(self, player):
        # Check rows, columns and diagonals
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(BOARD_COLS):
            if all(self.board[row][col] == player for row in range(BOARD_ROWS)):
                return True
        if all(self.board[i][i] == player for i in range(BOARD_ROWS)):
            return True
        if all(self.board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)):
            return True
        return False

    def switch_player(self):
        self.player = "O" if self.player == "X" else "X"

# Create game instance
game = Game()
game.draw_lines()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if game.is_available(mouseY, mouseX):
                game.mark_square(mouseY, mouseX)
                if game.check_win(game.player):
                    game.game_over = True
                    print(f"{game.player} wins!")
                game.switch_player()
                game.draw_figures()

    pygame.display.update()
