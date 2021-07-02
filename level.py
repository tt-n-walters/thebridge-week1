import arcade

width = 1280
height = 640

# Load the image
background = arcade.load_texture("map_1.png")
penguin = arcade.Sprite("penguin.png")
penguin.bottom = 500
penguin.left = 0
penguin.change_x = 5

gravity = -0.2

arcade.open_window(width, height, "Animal jump")
arcade.set_background_color(arcade.color.SKY_BLUE)

def draw(asdf):
    arcade.start_render()
    arcade.draw_texture_rectangle(width / 2, height / 2, width, height, background)
    penguin.draw()
    # Draw and update the penguin
    penguin.update()

    # Apply gravity to the penguin
    penguin.change_y = penguin.change_y + gravity

    # Stop penguin falling through the floor
    if penguin.bottom < 128:
        # penguin.change_y = 0
        penguin.bottom = 128

    # Cactus position
    if penguin.right >= 650 and penguin.right <= 652:
        penguin.change_y = 9
    
    # Bush position
    if penguin.right >= 1010 and penguin.right <= 1012:
        penguin.change_y = 9




arcade.schedule(draw, 1 / 60)
arcade.run()
