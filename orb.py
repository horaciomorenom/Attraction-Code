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
        self.x_positions = np.append(self.x_positions, self.position[0])
        self.y_positions = np.append(self.y_positions, self.position[1])

    def calculate_distance_travelled(self):
        self.distance = np.sum(np.sqrt(np.sum(np.diff(self.positions, axis=0)**2, axis=1)))

def get_orb_distance(orb1, orb2):

    return np.linalg.norm(orb1.position - orb2.position)

def get_max_orb_distance(orbs): # I know that I am doing more work than supposed to but I don't want to think

    distances = np.array([])

    for orb1 in orbs:
        for orb2 in orbs:
            distances = np.append(distances, get_orb_distance(orb1, orb2))
    return np.max(distances)

def evolve_orbs(orbs,t , dt, stop_distance, max_dists, time_array):

    while max_dists[-1] >= 0.3:

        for orb in orbs:
            orb.update_velocity()
        
        for orb in orbs:
            orb.update_position(dt)

    t += dt
    time_array = np.append(time_array, t)

    max_dists = np.append(max_dists, get_max_orb_distance(orbs))

    return time_array, max_dists
