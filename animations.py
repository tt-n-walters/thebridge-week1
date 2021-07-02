import arcade
import time

screen_width = 800
screen_height = 600
w = 60
h = 60
x = [400, 500, 200]
y = [500, 50, 250]
x_speed = [3, -10, 0]
y_speed = [0, 10, 60]
behaviour = "bounce"

gravity = -0.5
elasticity = 0.8



def draw(asdfghjkl):
    shape = 0

    arcade.start_render()
    while True:
        # print(round(time.time()), "Drawing at", x, y)
        arcade.draw_rectangle_filled(x[shape], y[shape], w, h, arcade.color.ORANGE)
        
        # Movement code
        x[shape] = x[shape] + x_speed[shape]
        y[shape] = y[shape] + y_speed[shape]
        y_speed[shape] = y_speed[shape] + gravity

        # Collision code
        if behaviour == "wrap":
            if x[shape] <= 0:
                x[shape] = screen_width
            elif x[shape] >= screen_width:
                x[shape] = 0
            if y[shape] <= 0:
                y[shape] = screen_height
            elif y[shape] >= screen_height:
                y[shape] = 0
        elif behaviour == "bounce":
            if x[shape] - w / 2 <= 0:                # left
                x_speed[shape] = -x_speed[shape] * elasticity
                x[shape] = w / 2
            elif x[shape] + w / 2 >= screen_width:   # right
                x_speed[shape] = -x_speed[shape] * elasticity
                x[shape] = screen_width - w / 2
            if y[shape] - h / 2 <= 0:                # bottom
                y_speed[shape] = -y_speed[shape] * elasticity
                y[shape] = h / 2
            if y[shape] + h / 2 >= screen_height:    # top
                y_speed[shape] = -y_speed[shape] * elasticity
                y[shape] = screen_height - h / 2
        # print("Moved to", x, y)

        # While loop control
        shape = shape + 1
        if shape == len(y_speed):
            break

    


arcade.open_window(screen_width, screen_height, "Animations")
arcade.set_background_color(arcade.color.WHITE)

arcade.schedule(draw, 1 / 60)
arcade.run()
