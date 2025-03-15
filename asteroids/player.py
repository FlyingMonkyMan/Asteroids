import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    
    
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        self.color = (255, 255, 255)
        self.points = self.triangle()
        line_width = 2
        pygame.draw.polygon(screen, self.color, self.points, line_width)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot_velocity = pygame.Vector2(0,1)
            shot_velocity = shot_velocity.rotate(self.rotation)
            shot_velocity =  shot_velocity * PLAYER_SHOOT_SPEED
            shot.velocity = shot_velocity
            self.shot_timer = PLAYER_SHOOT_COOLDOWN        
            return shot
        return None