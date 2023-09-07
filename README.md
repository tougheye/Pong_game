# Pong_game
I used this project to solidify my understanding of OOP and 
used Python's builtin turtle package to create the ball, paddles and the scoreboard

The scoreboard class keeps track of each players' score by using l_point and r_point functions
and updates scoreboard by using update_scoreboard function

The Ball class has separate functions to recognize a move, bounce back, paddle hit, and 
the reset function to reset at the end of the game. 
The paddle_hit function has a move_speed variable that could change the ball speed after each contact with the paddle

The Paddle class creates and moves paddles by using respective functions. It takes 2 input for up and down button for each paddle.

In the main.py file, the right paddle was created using "Up" and "Down" buttons and 
the left paddle used "w" and "s" buttons to move each paddle.
