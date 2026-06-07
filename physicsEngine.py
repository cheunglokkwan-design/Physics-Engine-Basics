import time
from typing import List

class Vector2D:
    """reusable mathematical vector for coordinates and motion"""
    def __init__(self, x:float = 0.0, y:float = 0.0):
        self.x = x
        self.y = y

    def add(self, other:'Vector2D')->'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)
    
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

class SimulationEngine:
    def __init__(self, gravity_y: float = -9.81):
        self.gravity = Vector2D(0.0, gravity_y)
        self.objects: List[Particle] = []
        
    def spawn_object(self, obj: Particle):
        self.objects.append(obj)

    def run(self, duration: float, dt: float):
        current_time = 0.0

        print(f"{'Time (s)':<10} | {'Pos X (m)':<12} | {'Pos Y (m)':<12} | {'Vel Y (m/s)':<12}")
        print("-" * 55)

        while current_time <= duration:
            for obj in self.objects:
                gravitational_force = self.gravity.multiply(obj.mass)
                obj.apply_force(gravitational_force)

                obj.step(dt)
                
                if round(current_time / 0.2, 5).is_integer():
                    print(f"{current_time:<10.2f} | {obj.position.x:<12.3f} | {obj.position.y:<12.3f} | {obj.velocity.y:<12.3f}")
            current_time += dt

if __name__ == "__main__":
    sim = SimulationEngine(gravity_y = -9.81)

    initial_pos = Vector2D(x=0.0,y = 0.0)
    initial_vel = Vector2D(x = 5.0, y = 15.0)
    projectile = Particle(mass=0.5, position=initial_pos, velocity=initial_vel)

    sim.spawn_object(projectile)
    

    sim.run(duration=3.0, dt=0.01)