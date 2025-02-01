import time 
from turtle import Screen 
from player import Player 
from car_manager import CarManager 
from scoreboard import Scoreboard  

# Create and set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  

# Prompt user for a turtle color, received via text input dialog
color = screen.textinput('Choose a color', 'What color you want your turtle to be ? :')

# Create a Player instance with the chosen color
player = Player(color)
screen.listen()  
screen.onkey(fun=player.move, key="Up")  

cars = [] 
speed_increase = 1  
scoreboard = Scoreboard()  

game_is_on = True  #
while game_is_on:
    time.sleep(0.1) 

    # Randomly add a new car with some probability (approx. 1 in 3 chance)
    if random.randint(1, 3) == 1:
        new_car = CarManager()
        cars.append(new_car)

    # Loop over a copy of the car list to update car positions and check collisions
    for car in cars[:]:
        car.move(speed_increase)  #
        if car.xcor() < -330:  
            cars.remove(car)  

        # Check if a car collides with the player
        if car.distance(player) < 30:  
            game_is_on = False  
            scoreboard.game_over() 

    # Check if the player has reached the top of the screen
    if player.ycor() > 280:
        player.next_level() 
        for car in cars:
            car.hideturtle()  
        cars.clear()  
        speed_increase += 0.2  
        scoreboard.update_score()  

    screen.update() 

screen.exitonclick()  
