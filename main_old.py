import pygame
import random

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
grid = []
    
class Rechteck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (x*(SCREEN_WIDTH/30)+(SCREEN_WIDTH/6), y*(SCREEN_WIDTH/30)+(SCREEN_HEIGHT/15))
        self.color = "grey"

    def draw(self, screen):
        self.rect = pygame.Rect(self.position[0], self.position[1], 0.9*(SCREEN_WIDTH/30), 0.9*(SCREEN_WIDTH/30))
        pygame.draw.rect(screen, self.color, self.rect)
    
    def canCollide(self, ball_x, ball_y):
        if self.position[0] == ball_x:
            index = self.y * 20 + self.x
            print(f"index for this is: {index}")
            grid[index] = None
        if self.position[1] == ball_y:
            del self

class movingBar:
    def __init__(self):
        self.position = [(SCREEN_WIDTH/2-SCREEN_WIDTH/16), (9*(SCREEN_HEIGHT/10))]
        self.color = "darkblue"

    def draw(self, screen):
        self.rect = pygame.Rect(self.position[0], self.position[1], SCREEN_WIDTH/8, SCREEN_HEIGHT/100)
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, x):
        self.position[0] += x

class bounciBall:
    def __init__(self):
        self.position = [random.randint(int(SCREEN_WIDTH/50),int(49*SCREEN_WIDTH/50)),random.randint(int(SCREEN_HEIGHT*5/6),int(SCREEN_HEIGHT-SCREEN_WIDTH/50))]
        self.color = "purple"
        self.dx = random.randint(50,100)/50 # Random velocity on x-Achsis
        self.dy = random.randint(-100,-50)/50 # Rnadom velocitiy on y-Achsis in positiv Direction towards the grid
        self.game = True

    def draw(self, screen):
        self.rect = pygame.Rect(self.position[0], self.position[1], SCREEN_WIDTH/50, SCREEN_WIDTH/50)
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self):
        self.position[0] += self.dx
        self.position[1] += self.dy
        if self.position[0] <= 0 or self.position[0] >= SCREEN_WIDTH:
            self.dx = -self.dx
        if self.position[1] <= 0:
            self.dy = -self.dy
        if self.position[1] > SCREEN_HEIGHT:
            self.game = False

def gridInit():
    for i in range(20):
        for j in range(10):
            rect = Rechteck(int(i), int(j))
            grid.append(rect)

def gridRender():
    for i in grid:
        if i == None:
            continue
        i.draw(screen)

def barMoving(moving):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        moving.move(-5)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        moving.move(5)

def canCollide(bar, recti, ball):
    if bar.rect.colliderect(ball.rect):
        ball.dy = -ball.dy
    for val in recti:
        if val is None:
            continue
        if val.rect.colliderect(ball.rect):
            grid[grid.index(val)] = None
            ball_rect = ball.rect
            rect = val.rect
            overlap_left = ball_rect.right - rect.left
            overlap_right = rect.right - ball_rect.left
            overlap_top = ball_rect.bottom - rect.top
            overlap_bottom = rect.bottom - ball_rect.top
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            if min_overlap == overlap_left:
                ball.dx = -abs(ball.dx)
            elif min_overlap == overlap_right:
                ball.dx = abs(ball.dx)
            elif min_overlap == overlap_top:
                ball.dy = -abs(ball.dy)
            elif min_overlap == overlap_bottom:
                ball.dy = abs(ball.dy)

def endFont():
    font = pygame.font.Font('Tiny5-Regular.ttf', 120)
    text_surface = font.render('You failed and you suck!', True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    screen.blit(text_surface, (SCREEN_WIDTH/2-text_rect.width/2, SCREEN_HEIGHT/2-text_rect.height/2))

def winFont():
    font = pygame.font.Font('Tiny5-Regular.ttf', 120)
    text_surface = font.render('Your are great!', True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    screen.blit(text_surface, (SCREEN_WIDTH/2-text_rect.width/2, SCREEN_HEIGHT/2-text_rect.height/2))


def main():
    moving = movingBar()
    moving.draw(screen)
    movePoint = bounciBall()
    movePoint.draw(screen)
    running = True
    win = False
    gridInit()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False      
        screen.fill("beige")
        # RENDER YOUR GAME HERE 
        run_count = 0
        for i in grid:
            if i == None:
                run_count += 1
        if run_count == len(grid):
            win = True    
        if win == False:   
            if movePoint.game == True:
                gridRender()
                barMoving(moving)
                moving.draw(screen)
                movePoint.move()
                movePoint.draw(screen)
                canCollide(moving, grid, movePoint)
            else:
                endFont()
        else:
            winFont()
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(165)  # limits FPS to 165, my refresh rate

    pygame.quit()

if __name__ == '__main__':
    main()
