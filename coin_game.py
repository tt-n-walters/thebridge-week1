import arcade
import random
import time


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
        self.end_time = time.time() + 15
        print("Starting at", time.time())
        print("Finishing at ", self.end_time)


    def on_draw(self):
        arcade.start_render()
        # Draw the score on screen
        arcade.draw_text(
            str(self.coins_collected),
            self.width / 4,
            self.height / 2,
            (30, 30, 30),
            500,
            anchor_x="center",
            anchor_y="center"
        )
        # Draw the remaining time
        time_remaining = round(self.end_time - time.time(), 1)
        if time_remaining > 0:
            arcade.draw_text(
                str(time_remaining),
                self.width * 3 / 4,
                self.height / 2,
                (30, 30, 30),
                400,
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
        
        if time.time() >= self.end_time:
            self.player.kill()
            self.coins.clear()
    

    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
        self.player.center_y = y
    

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()



CoinGame()
arcade.run()