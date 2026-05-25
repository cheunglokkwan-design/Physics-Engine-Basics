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
