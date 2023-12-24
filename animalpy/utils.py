import random

class Utils:
    def __init__(self):
        self.BASE_URL = "https://github.com/SeasonalKirito/animalpy"
        self.RAW_BASE_URL = "https://raw.githubusercontent.com/SeasonalKirito/animalpy/main"
        self.CURRENT_MAX = 5

    def _random_num(self):
        try:
            return random.randint(1, self.CURRENT_MAX)
        except Exception as e:
            pass
    
    def _get_img(self, TYPE=None):
        try:
            return f"{self.RAW_BASE_URL}/content/{TYPE}/img[{self._random_num()}].png"
        except Exception as e:
            return str(e)

    def _get_gif(self, TYPE=None):
        try:
            return f"{self.RAW_BASE_URL}/content/{TYPE}/gif[{self._random_num()}].png"
        except Exception as e:
            return str(e)