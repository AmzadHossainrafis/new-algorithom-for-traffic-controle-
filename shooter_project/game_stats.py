class GameState():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship_left = self.settings.ship_limit
        self.game_active = False
        self.score = 0

        self.reset_state()

    def reset_state(self):
        self.ships_left = self.settings.ship_limit
