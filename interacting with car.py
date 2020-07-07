'''
Creating a Car Object
To create a Car, which was named Hafez in the example. I have to:

Import our car file and define a car's initial state variable, andCall car.Car(); 
a special function that initializes a Car object, and pass in the initial state variables.
The state is defined by a position: [y, x] and a velocity, which has vertical and horizontal components: [vy, vx]. And lastly, 
we had to pass in a world, which is just a 2D array.
'''
#######		Imports and Defining initial variables		#######
import numpy as np
import car

# Declare initial variables
# Create a 2D world of 0's
height = 4
width = 6
world = np.zeros((height, width))

# Define the initial car state
initial_position = [0, 0] # [y, x] (top-left corner)
velocity = [0, 1] # [vy, vx] (moving to the right)
#########

######	 Creating and Visualizing a Car!  ##########

# Create a car object with these initial params
																######	IMPORTANT	 #####
Hafez = car.Car(initial_position, velocity, world)  ## First car is name of object file and second car is the name of Object itself. 
print('Hafez\'s initial state is: ' + str(Hafez.state))

# Display the world
#Hafez.display_world()

############  Move and track state   #########
'''
# Move in the direction of the initial velocity

Hafez.move()
Hafez.move()


# Track the change in state
print('Hafez\'s state is: ' + str(Hafez.state))

# Display the world

Hafez.turn_right()
for k in range(3):  ### Hafez car turns right and moves a 3 cells
	Hafez.move()

print('Hafez\'s state is: ' + str(Hafez.state))
Hafez.display_world()
'''
### Imp.  Make Ahmed car traverse a 4x4 square path And Display the result.


carla = car.Car(initial_position, velocity, world) 
carla.turn_left()
carla.turn_left()
for i in range(4):
    carla.turn_left()
    for j in range(3):
        carla.move()
        
carla.display_world()
