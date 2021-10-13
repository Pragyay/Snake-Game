import random
import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 720, 480

WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60

food_pos = [random.randint(1, WIDTH), random.randint(1, HEIGHT)]

# SNAKE_WIDTH = 20
# SNAKE_HEIGHT = 20

snake_pos = [100, 50]               # head of our snake
snake_body = [[100, 50], [90, 50], [80, 50]]

clock = pygame.time.Clock()

direction = 'RIGHT'
change_to = direction

bounds = WIN.get_rect()

score = 0


def show_score(choice):
    score_font = pygame.font.SysFont('comicsans', 40)
    score_text = score_font.render("Your score: " + str(score), 1, WHITE)

    if choice == 1:
        WIN.blit(score_text, (20, 10))
    else:
        WIN.blit(score_text, ((WIDTH - score_text.get_width())//2, HEIGHT//2 + 50))


def game_over():
    font = pygame.font.SysFont('comicsans', 80)
    draw_text = font.render("Game Over", 1, WHITE)
    width = (WIDTH - draw_text.get_width()) / 2
    height = (HEIGHT - draw_text.get_height()) / 2

    WIN.fill(BLACK)

    WIN.blit(draw_text, (width, height))
    show_score(0)

    pygame.display.flip()  # update whole screen
    pygame.time.delay(3000)
    pygame.quit()


def draw_window():

    WIN.fill(BLACK)

    for rect in snake_body:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(rect[0], rect[1], 10, 10))

    pygame.draw.rect(WIN, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    show_score(1)

    pygame.display.update()


run = True
while run:
    snake_head = pygame.Rect(snake_pos[0], snake_pos[1], 10, 10)
    food = pygame.Rect(food_pos[0], food_pos[1], 10, 10)

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to = 'UP'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                change_to = 'DOWN'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                change_to = 'LEFT'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 5
    if direction == 'DOWN':
        snake_pos[1] += 5
    if direction == 'LEFT':
        snake_pos[0] -= 5
    if direction == 'RIGHT':
        snake_pos[0] += 5

    # update coordinates of snake head
    snake_body.insert(0, list(snake_pos))

    # snake eats food
    if snake_head.colliderect(food):
        score += 1
        food_pos = [random.randint(21, WIDTH-20), random.randint(21, HEIGHT-20)]
    else:
        snake_body.pop()

    # if snake out of bounds
    if snake_pos[0] < bounds.left or snake_pos[0] + 10 > bounds.right:
        game_over()
    if snake_pos[1] < bounds.top or snake_pos[1] + 10 > bounds.bottom:
        game_over()

    # if snake touches its body
    for rect in snake_body[1:]:
        if snake_pos[0] == rect[0] and snake_pos[1] == rect[1]:
            game_over()

    draw_window()

pygame.quit()
