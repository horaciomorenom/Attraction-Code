import numpy as np

def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        return v
    return v/norm

class orb:
    """
    A class used to represent an orb in the 2-D attraction experiment

    ...

    Attributes
    ----------
    position : np.ndarray
        2-vector specifying the particle's position
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

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


