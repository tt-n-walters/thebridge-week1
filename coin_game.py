import arcade
import random

class CoinGame(arcade.Window):
    def __init__(self):           # Initialise
        super().__init__(800, 600, "Coin Game", True)
        self.set_mouse_visible(False)
        
        self.player = arcade.Sprite("player_front.png")
        self.player.center_x = self.width / 2
        self.player.center_y = self.height / 2

        # List to hold all coins
        self.coins = []
        for i in range(3):
            self.coin = arcade.Sprite("gold_1.png", 0.5)
            self.coin.center_x = random.randint(1, self.width)
            self.coin.center_y = random.randint(1, self.height)
            # Add the new coin to the list
            self.coins.append(self.coin)

        self.coins_collected = 0


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            str(self.coins_collected),
            self.width / 4,
            self.height / 2,
            arcade.color.DIM_GRAY,
            500,
            anchor_x="center",
            anchor_y="center"
        )
        self.player.draw()
        
        # Draw all the coins
        for coin in self.coins:
            coin.draw()
    

    def on_update(self, deltatime):
        # Collide with all coins
        for coin in self.coins:
            if self.player.collides_with_sprite(coin):
                print("Coin collected.")
                # Collect the coin and move to another random position
                self.coins_collected = self.coins_collected + 1
                coin.center_x = random.randint(1, self.width)
                coin.center_y = random.randint(1, self.height)
    

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
        self.player.center_y = y
    

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()



CoinGame()
arcade.run()