import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
grey = (200, 200, 200)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 1200
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 14)


class Snake:
    def __init__(self, snumber):
        self.Length_of_snake = 1
        self.snake_List = []
        self.x1 = 20
        self.y1 = 100
        self.x1_change = 0
        self.y1_change = 0
        self.snake_Head = []
        self.isAlive = True
        if snumber == 1:
            self.color = red
        else:
            self.color = black
            self.x1 = 20
            self.y1 = 120
        self.score = 0

    def draw(self):
        for x in self.snake_List:
            pygame.draw.rect(dis, self.color, [x[0], x[1], snake_block, snake_block])

    def get_info(self, snumber):
        value = score_font.render("Player " + str(snumber) + " score: " + str(self.score), True, yellow)
        dis.blit(value, [0, (snumber - 1) * 20])
        if (self.isAlive == False):
            value = score_font.render(" DIED ", True, red)
            dis.blit(value, [110, (snumber - 1) * 20])

    def check_walls(self):
        if self.x1 >= dis_width or self.x1 < 0 or self.y1 >= dis_height or self.y1 < 0:
            return True
        return False

    def check_head(self):
        for x in self.snake_List[:-1]:
            if x == self.snake_Head:
                return True

    def change_vals(self):
        self.x1 += self.x1_change
        self.y1 += self.y1_change

    def add_head(self):
        self.snake_Head = []
        self.snake_Head.append(self.x1)
        self.snake_Head.append(self.y1)
        self.snake_List.append(self.snake_Head)
        if len(self.snake_List) > self.Length_of_snake:
            del self.snake_List[0]

    def is_beats_wall(self, level):
        for wall in level_walls[level]:
            if self.x1 >= wall["start_x"] and self.y1 >= wall["start_y"] and self.x1 <= wall["start_x"] + wall[
                "weight_x"] and self.y1 <= wall["start_y"] + wall["weight_y"]:
                self.x1 = random.randrange(0, wall["start_x"])
                self.y1 = random.randrange(0, wall["start_y"])
                return True
        return False


def cross_snakes(snake1, snake2):
    if snake1.isAlive == True:
        for x in snake2.snake_List:
            if snake1.x1 == x[0] and snake1.y1 == x[1]:
                return 1
    if snake2.isAlive == True:
        for x in snake1.snake_List:
            if snake2.x1 == x[0] and snake2.y1 == x[1]:
                return 2
    return 0


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def check_food_for_wall(level, foodx, foody):
    for wall in level_walls[level]:
        if foodx >= wall["start_x"] + snake_block and foody >= wall["start_y"] - snake_block and foodx <= wall[
            "start_x"] + wall["weight_x"] + snake_block and foody <= wall["start_y"] + wall["weight_y"] + snake_block:
            foodx = random.randrange(0, wall["start_x"] - snake_block)
            foody = random.randrange(0, wall["start_y"] - snake_block)
            return [foodx, foody]
    return [foodx, foody]


wall1 = {
    "start_x": 150,
    "start_y": 150,
    "weight_x": 300,
    "weight_y": 100
}

wall2 = {
    "start_x": 150,
    "start_y": 350,
    "weight_x": 300,
    "weight_y": 100
}
wall3 = {
    "start_x": 800,
    "start_y": 100,
    "weight_x": 200,
    "weight_y": 400
}
wall4 = {
    "start_x": 100,
    "start_y": 100,
    "weight_x": 50,
    "weight_y": 300
}
wall5 = {
    "start_x": 220,
    "start_y": 220,
    "weight_x": 300,
    "weight_y": 100
}
wall6 = {
    "start_x": 600,
    "start_y": 100,
    "weight_x": 50,
    "weight_y": 300
}
wall7 = {
    "start_x": 900,
    "start_y": 100,
    "weight_x": 50,
    "weight_y": 300
}
level_walls = {
    1: [wall1, wall2],
    2: [wall1, wall2, wall3],
    3: [wall4, wall5, wall6, wall7]}  # walls for levels

for wall in level_walls[1]:
    print("wall in level 1", wall)


def gameLoop(lvl):
    game_over = False
    game_close = False

    level = lvl
    if lvl != 0:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        coords = check_food_for_wall(level, foodx, foody)
        foodx = coords[0]
        foody = coords[1]
        print(coords)
    snake_speed = 10 + lvl * 2
    player1 = Snake(1)
    player2 = Snake(2)
    print(dis_width / 2 + 50, dis_width / 2 + 50, snake_block * 5, snake_block)
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            if player1.score > player2.score:
                message(
                    "Player 1 wins! " + str(player1.score) + ":" + str(player2.score) + " Press C-Play Again or Q-Quit",
                    yellow)
            elif player1.score < player2.score:
                message(
                    "Player 2 wins! " + str(player1.score) + ":" + str(player2.score) + " Press C-Play Again or Q-Quit",
                    yellow)
            else:
                message("Equal powers! Press C-Play Again or Q-Quit", yellow)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop(0)
                if event.key == pygame.K_LEFT:
                    player1.x1_change = -snake_block
                    player1.y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    player1.x1_change = snake_block
                    player1.y1_change = 0
                elif event.key == pygame.K_UP:
                    player1.y1_change = -snake_block
                    player1.x1_change = 0
                elif event.key == pygame.K_DOWN:
                    player1.y1_change = snake_block
                    player1.x1_change = 0
                elif event.key == pygame.K_a:
                    player2.x1_change = -snake_block
                    player2.y1_change = 0
                elif event.key == pygame.K_d:
                    player2.x1_change = snake_block
                    player2.y1_change = 0
                elif event.key == pygame.K_w:
                    player2.y1_change = -snake_block
                    player2.x1_change = 0
                elif event.key == pygame.K_s:
                    player2.y1_change = snake_block
                    player2.x1_change = 0
                elif level == 0 and event.key == pygame.K_1:
                    level = 1
                    gameLoop(1)
                elif level == 0 and event.key == pygame.K_2:
                    level = 2
                    gameLoop(2)
                elif level == 0 and event.key == pygame.K_3:
                    level = 3
                    gameLoop(3)

        if level == 0:
            dis.fill(blue)
            message("Please choose level. Easy press - 1, Medium press - 2, Hard press - 3", yellow)
            pygame.display.update()
            continue

        if player1.check_walls():
            player1.isAlive = False

        if player2.check_walls():
            player2.isAlive = False

        if player1.isAlive:
            player1.change_vals()
        if player2.isAlive:
            player2.change_vals()
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        if player1.isAlive:
            player1.add_head()
        if player2.isAlive:
            player2.add_head()

        for wall in level_walls[level]:
            pygame.draw.rect(dis, grey, [wall["start_x"], wall["start_y"], wall["weight_x"], wall["weight_y"]])

        player1.draw()
        player2.draw()

        player1.get_info(1)
        player2.get_info(2)

        if player1.check_head():
            player1.isAlive = False

        if player2.check_head():
            player2.isAlive = False

        cros = cross_snakes(player1, player2)
        if cros == 1:
            player1.isAlive = False
        elif cros == 2:
            player2.isAlive = False

        if player1.is_beats_wall(level) == True:
            player1.isAlive = False

        if player2.is_beats_wall(level) == True:
            player2.isAlive = False

        pygame.display.update()

        if player1.isAlive == False and player2.isAlive == False:
            game_close = True

        if player1.x1 == foodx and player1.y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            player1.Length_of_snake += 1
            player1.score += 1

        if player2.x1 == foodx and player2.y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            player2.Length_of_snake += 1
            player2.score += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop(0)