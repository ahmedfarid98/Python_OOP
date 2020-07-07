import car
import numpy as np

##### For First car Named Ahmed and it's color is blue

world_Ahmed=np.zeros((5,5))
init_position_Ahmed=[2,2]
init_velocity_Ahmed=[0,1]

Ahmed = car.Car(init_position_Ahmed,init_velocity_Ahmed,world_Ahmed,'b')

Ahmed.turn_right()
Ahmed.move()
Ahmed.move()
Ahmed.turn_left()
Ahmed.move()

Ahmed.display_world()

##### For second car Named Hafez and it's color is yellow

world_hafez=np.zeros((5,5))
init_position_hafez=[3,0]
init_velocity_hafez=[0,1]

hafez = car.Car(init_position_hafez,init_velocity_hafez,world_hafez,'y')
hafez.turn_left()
hafez.move()
hafez.move()
hafez.turn_right()
hafez.move()
hafez.move()
hafez.display_world()

