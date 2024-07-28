import pygame
import numpy as np

def main():
    pygame.init()

    # Define screen dimensions and colors
    width, height = 600, 400
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)

    # Define the snake's initial properties
    snake_block = 10
    snake_speed = 15

    # Initialize screen and clock
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Define fonts
    font_style = pygame.font.SysFont(None, 50)
    score_font = pygame.font.SysFont(None, 35)

    # Define the snake object
    def snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

    # Define the score display
    def your_score(score):
        value = score_font.render(f"Your Score: {score}", True, white)
        screen.blit(value, [0, 0])

    # Define the message display
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width / 6, height / 3])

    # Define the game loop
    def gameLoop():
        game_over = False
        game_close = False

        x1 = width / 2
        y1 = height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        foodx = round(np.random.randint(0, width - snake_block) / 10.0) * 10.0
        foody = round(np.random.randint(0, height - snake_block) / 10.0) * 10.0

        while not game_over:
            while game_close:
                screen.fill(black)
                message("You Lost! Press Q-Quit or C-Play Again", red)
                your_score(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill(black)
            pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            snake(snake_block, snake_list)
            your_score(length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(np.random.randint(0, width - snake_block) / 10.0) * 10.0
                foody = round(np.random.randint(0, height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()

if __name__ == "__main__":
    main()
