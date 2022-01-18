import numpy as np

def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        return v
    return v/norm

class orb:
    def __init__(self, position):
        self.position = position
        self.velocity = np.array([0,0]) 
        self.velocity_history = np.array([]) 
        self.positions = np.array([self.position])
        self.x_positions = np.array([])
        self.y_positions = np.array([])   
    
    def set_target(self, target):
        self.target = target

    def update_velocity(self):
        self.velocity = normalize(self.target.position - self.position)
        np.append(self.velocity_history, self.velocity, axis=0)

    def update_position(self, timestep):
        self.position = self.position + self.velocity*timestep
        self.positions = np.append(self.positions, np.array([self.position]), axis=0)
    def calculate_distance_travelled(self):
        self.distance = np.sum(np.sqrt(np.sum(np.diff(self.positions, axis=0)**2, axis=1)))

