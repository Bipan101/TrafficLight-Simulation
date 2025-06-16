import pygame
import time

# Initialization of pygame
pygame.init()

# Screen setup 
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car and Traffic System Simulation.")

# Colors used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CAR_COLOR = (0, 102, 204)


car_x = 0
road_y = HEIGHT // 2
car_width = 100
car_height = 45
car_y = road_y - 110 // 2  
car_speed = 2


traffic_light_x = 500
checkpoint_x = traffic_light_x - 80  
light_interval = 4  
last_switch_time = time.time()
traffic_light_color = RED

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    pygame.draw.line(screen, BLACK, (0, road_y), (WIDTH, road_y), 5)


    pygame.draw.line(screen, BLACK, (checkpoint_x, road_y - 40), (checkpoint_x, road_y + 40), 3)

    # === Draw traffic light ===
    light_y = road_y - 150
    light_x = traffic_light_x - 15
    pygame.draw.rect(screen, BLACK, (light_x, light_y, 30, 60))  # Light box
    pygame.draw.circle(screen, RED if traffic_light_color == RED else (80, 0, 0),
                       (light_x + 15, light_y + 15), 10)
    pygame.draw.circle(screen, GREEN if traffic_light_color == GREEN else (0, 80, 0),
                       (light_x + 15, light_y + 45), 10)

  
    current_time = time.time()
    if current_time - last_switch_time > light_interval:
        traffic_light_color = GREEN if traffic_light_color == RED else RED
        last_switch_time = current_time

   
    if car_x > WIDTH:
        car_x = -car_width  # reset from left side again

    
    if car_x + car_width < checkpoint_x or traffic_light_color == GREEN:
        car_x += car_speed

   
    pygame.draw.rect(screen, CAR_COLOR, (car_x, car_y, car_width, car_height))  # Car body
    pygame.draw.circle(screen, BLACK, (car_x + 15, car_y + car_height), 7)  # Rear wheel
    pygame.draw.circle(screen, BLACK, (car_x + car_width - 15, car_y + car_height), 7)  # Front wheel

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
