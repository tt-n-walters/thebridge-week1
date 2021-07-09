import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 640, "Game")

        tilemap = arcade.tilemap.read_tmx("C://Users/Alumno.NOT06-02-I5S17G.000/Downloads/map_basic_ni.tmx")
        self.sprites = arcade.tilemap.process_layer(tilemap, "Tile Layer 1", 0.5)
        self.background = arcade.tilemap.process_layer(tilemap, "Background", 0.5)

        self.player = arcade.Sprite("player_idle.png")
        self.player.left = 0
        self.player.top = self.height

        # Start up the physics engine
        self.physics = arcade.PhysicsEnginePlatformer(self.player, self.sprites, gravity_constant=0.8)

        arcade.set_background_color(arcade.color.SKY_BLUE)


    def on_draw(self):
        arcade.start_render()
        self.sprites.draw()
        self.background.draw()
        self.player.draw()

    def on_update(self, delta_time):
        self.physics.update()

        # Camera shenanigans
        l, r, b, t = self.get_viewport()
        distance_from_right = r - self.player.right
        print(distance_from_right)
        if distance_from_right < 250:
            screen_left = self.player.right + 250 - self.width
            screen_right = screen_left + self.width
            screen_top = self.height
            screen_bottom = 0
            arcade.set_viewport(screen_left, screen_right, screen_bottom, screen_top)
        
        # Stop the player moving off the left
        if self.player.left < l:
            self.player.left = l
        
        # Reach the end of the map
        if self.player.right > 2900:
            arcade.close_window()
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.physics.can_jump():
            self.physics.jump(16)
        if key == arcade.key.D:
            self.player.change_x = 4
        if key == arcade.key.A:
            self.player.change_x = -4
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.D or key == arcade.key.A:
            self.player.change_x = 0

Game()
arcade.run()
