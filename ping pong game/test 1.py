import pygame
from ball import Ball
from paddle import Paddle

def paddle_move(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.update(True, HEIGHT)
    if keys[pygame.K_s]:
        left_paddle.update(False, HEIGHT)

    if keys[pygame.K_UP]:
        right_paddle.update(True, HEIGHT)
    if keys[pygame.K_DOWN]:
        right_paddle.update(False, HEIGHT)

def draw_score(window, left_score, right_score):
    left_score_text = score_font.render(f"{left_score}", True, WHITE)
    right_score_text = score_font.render(f"{right_score}", True, WHITE)
    window.blit(left_score_text, (100, 20))
    window.blit(right_score_text, (WIDTH-100-right_score_text.get_width(), 20))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 700
HEIGHT = 500
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping pong")
score_font = pygame.font.Font("C:/Users/steven.luo/Documents/Python project/Interesting-Python-Projects-That-I-Made/ping pong game/微軟正黑體.ttf", 50)

ball = Ball(WIDTH/2, HEIGHT/2, 7, WHITE)
# ball1 = Ball(100, 100, 10, (255, 0, 0))
# ball2 = Ball(200, 200, 10, (0, 0, 255))
paddle_width = 15
paddle_height = 100
left_paddle = Paddle(10, HEIGHT/2-paddle_height/2, paddle_width, paddle_height, WHITE)
right_paddle = Paddle(WIDTH-10-paddle_width, HEIGHT/2-paddle_height/2, paddle_width, paddle_height, WHITE)

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    # get the intake
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    paddle_move(keys, left_paddle, right_paddle)

    # update the game
    ball.update(WIDTH, HEIGHT, left_paddle, right_paddle)
    ball.check_collide(left_paddle, right_paddle)
    # ball1.update(WIDTH, HEIGHT)
    # ball2.update(WIDTH, HEIGHT)

    # display
    window.fill(BLACK)
    ball.draw(window)
    # ball1.draw(window)
    # ball2.draw(window)
    left_paddle.draw(window)
    right_paddle.draw(window)
    draw_score(window, left_paddle.score, right_paddle.score)
    pygame.display.update()

pygame.quit()
