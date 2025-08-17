import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

FPS = 60

class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 6

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        elif not up and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(WIN, WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
        self.x_vel = 5
        self.y_vel = 5

    def move(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.y_vel *= -1

    def draw(self):
        pygame.draw.ellipse(WIN, WHITE, self.rect)

    def reset(self):
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.x_vel *= -1


def draw(paddles, ball, left_score, right_score):
    WIN.fill(BLACK)

    font = pygame.font.SysFont("comicsans", 50)
    score_text = font.render(f"{left_score}   {right_score}", True, WHITE)
    WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw()
    ball.draw()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    left_paddle = Paddle(10)
    right_paddle = Paddle(WIDTH - 20)
    ball = Ball()

    left_score, right_score = 0, 0

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left_paddle.move(up=True)
        if keys[pygame.K_s]:
            left_paddle.move(up=False)
        if keys[pygame.K_UP]:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN]:
            right_paddle.move(up=False)

        ball.move()

        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.x_vel *= -1

        if ball.rect.left <= 0:
            right_score += 1
            ball.reset()
        if ball.rect.right >= WIDTH:
            left_score += 1
            ball.reset()

        draw([left_paddle, right_paddle], ball, left_score, right_score)


if __name__ == "__main__":
    main()
