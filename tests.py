import pygame

pygame.init()

LARGEUR, HAUTEUR = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = LARGEUR // COLS

BROWN = (190, 130, 80)
WHITE = (250, 247, 225)

screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("MA-24 : Dames Game")

icon = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\International_draughts.png")
black_piece_image = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\MA-24_pion-noir.png")
white_piece_image = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\MA-24_pion-blanc.png")
pygame.display.set_icon(icon)

black_piece_image = pygame.transform.scale(black_piece_image, (SQUARE_SIZE, SQUARE_SIZE))
white_piece_image = pygame.transform.scale(white_piece_image, (SQUARE_SIZE, SQUARE_SIZE))


def dessiner_tableau():
    """Draw the checkerboard."""
    for row in range(ROWS):
        for col in range(COLS):
            color = BROWN if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def create_pieces():
    board = [[None for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 != 0:  # Only place on dark squares
                if row < 2:
                    board[row][col] = "B"  # Black piece (top two rows)
                elif row > 5:
                    board[row][col] = "W"  # White piece (bottom two rows)
    return board


def draw_pieces(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "B":
                screen.blit(black_piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            elif board[row][col] == "W":
                screen.blit(white_piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))


def valid_move(board, old_row, old_col, new_row, new_col):
    """Check if a move is valid."""
    if board[new_row][new_col] is not None:
        return False

    row_diff = new_row - old_row
    col_diff = abs(new_col - old_col)

    if col_diff != 1:
        return False

    if board[old_row][old_col] == "B" and row_diff != 1:
        return False

    if board[old_row][old_col] == "W" and row_diff != -1:
        return False

    return True


def valid_capture(board, old_row, old_col, new_row, new_col):
    row_diff = new_row - old_row
    col_diff = abs(new_col - old_col)

    if col_diff != 2:
        return False

    if row_diff not in [2, -2]:
        return False

    middle_row = (old_row + new_row) // 2
    middle_col = (old_col + new_col) // 2

    if board[middle_row][middle_col] is None:
        return False

    if board[old_row][old_col] == "B" and board[middle_row][middle_col] != "W":
        return False
    if board[old_row][old_col] == "W" and board[middle_row][middle_col] != "B":
        return False

    return True


def perform_capture(board, old_row, old_col, new_row, new_col):
    middle_row = (old_row + new_row) // 2
    middle_col = (old_col + new_col) // 2

    board[middle_row][middle_col] = None

    board[new_row][new_col] = board[old_row][old_col]
    board[old_row][old_col] = None


def changer_position(board, old_row, old_col, new_row, new_col):
    if valid_move(board, old_row, old_col, new_row, new_col):
        board[new_row][new_col] = board[old_row][old_col]
        board[old_row][old_col] = None
        return True
    elif valid_capture(board, old_row, old_col, new_row, new_col):
        perform_capture(board, old_row, old_col, new_row, new_col)
        return True
    return False


board = create_pieces()
selected_piece = None
running = True

while running:
    dessiner_tableau()
    draw_pieces(board)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE

            if selected_piece:
                old_row, old_col = selected_piece
                if changer_position(board, old_row, old_col, clicked_row, clicked_col):
                    selected_piece = None
            elif board[clicked_row][clicked_col] is not None:
                selected_piece = (clicked_row, clicked_col)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

pygame.quit()
