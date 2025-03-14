import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from AsteroidField import AsteroidField 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), PLAYER_RADIUS)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = game_clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        updatable_group.update(dt)
        
        for asteroid in asteroids_group:
            if player.collision_check(asteroid):
                print("Game Over!")
                sys.exit()

        for object in drawable_group:
            object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()