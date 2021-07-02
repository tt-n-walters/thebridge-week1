import arcade


def draw_tree(x, y):
    print("Drawing a tree.")
    arcade.draw_triangle_filled(
        x + 320 - 400, y + 200 - 200,
        x + 400 - 400, y + 500 - 200,
        x + 480 - 400, y + 200 - 200,
        arcade.color.FOREST_GREEN)
    arcade.draw_rectangle_filled(x + 400 - 400, y + 175 - 200, 25, 50, arcade.color.BROWN)


arcade.open_window(800, 600, "Tree")

arcade.start_render()

arcade.draw_rectangle_filled(400, 425, 800, 350, arcade.color.SKY_BLUE)
arcade.draw_rectangle_filled(400, 125, 800, 250, arcade.color.PALE_GREEN)
draw_tree(0, 0)
draw_tree(300, 200)
draw_tree(550, 250)
draw_tree(600, 100)


arcade.finish_render()
arcade.run()
