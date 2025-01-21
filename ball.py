import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball = pygame.Rect(400, 300, 20, 20)
ball_speed = [5, 5]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.left <= 0 or ball.right >= 800:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed[1] = -ball_speed[1]

    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 0, 0), ball)
    pygame.display.flip()
    clock.tick(60)
