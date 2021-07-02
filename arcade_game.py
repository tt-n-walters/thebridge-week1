import arcade

arcade.open_window(800, 600, "Python Arcade")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()


arcade.draw_circle_filled(400, 300, 200, arcade.color.YELLOW)
arcade.draw_circle_filled(320, 375, 40, arcade.color.BLACK)
arcade.draw_circle_filled(480, 375, 40, arcade.color.BLACK)
arcade.draw_triangle_filled(
    300, 250,
    340, 210,
    400, 200,
    arcade.color.BLACK)
arcade.draw_triangle_filled(
    500, 250,
    360, 210,
    400, 200,
    arcade.color.BLACK)

arcade.draw_rectangle_filled(400, 480, 300, 30, arcade.color.BLACK)
arcade.draw_rectangle_filled(400, 600, 200, 240, arcade.color.BLACK)

arcade.finish_render()

arcade.run()
