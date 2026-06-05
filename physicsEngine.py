import time
from typing import List

class Vector2D:
    """reusable mathematical vector for coordinates and motion"""
    def __init__(self, x:float = 0.0, y:float = 0.0):
        self.x = x
        self.y = y

    def add(self, other:'Vector2D')->Vector2D:
        return Vector2D(self + other.x, self.y + other.y)
    
    def multiply(self, scalar:float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)


class Particle: 
    def __init__(self, mass:float, position:Vector2D, velocity:Vector2D):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.forces = Vector2D(0.0,0.0)

    def apply_force(self, force:Vector2D):
        self.forces = self.forces.add(force)
    
    def step(self, dt:float):
        acceleration = self.forces.multiply(1.0/self.mass)

        self.velocity = self.velocity.add(acceleration.multiply(dt))

        self.position = self.position.add(self.velocity.multiply(dt))

        self.forces = Vector2D(0.0,0.0)