class Robot:
    def __init__(self, orientation, position_x=0, position_y=0):
        self.orientation = orientation
        self.position = {'x': position_x, 'y': position_y}
        self.turn_mapping = {'up': {'left': 'left', 'right': 'right'},
                             'down': {'left': 'right', 'right': 'left'},
                             'right': {'left': 'up', 'right': 'down'},
                             'left': {'left': 'down', 'right': 'up'}}

    def move(self, steps):
        if self.orientation == 'up':
            self.position['y'] += steps
        elif self.orientation == 'down':
            self.position['y'] -= steps
        elif self.orientation == 'right':
            self.position['x'] += steps
        elif self.orientation == 'left':
            self.position['x'] -= steps

    def turn(self, direction):
        self.orientation = self.turn_mapping[self.orientation][direction]

    def display_position(self):
        print(f"Connecting... \
        Online position is: ({self.position['x']}, {self.position['y']}), Orientation is: {self.orientation}")


robot = Robot(orientation='up')

robot.display_position()  
robot.turn('right')
robot.move(3)
robot.display_position()
robot.move(5)
robot.display_position()  
robot.turn('left')
robot.move(2)
robot.display_position()
