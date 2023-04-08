class Unit:

    def __init__(self, state:bool, speed:int, x:int, y:int, field):
        self.state = state
        self.speed = speed
        self.x = x
        self.y = y
        self.field = field

    def move(self, direction):
        self.speed = self._get_speed()
        self._moveFlyOrCrawl(direction)
        self.field.set_unit(x=self.x, y=self.y, unit=self)

    def _moveFlyOrCrawl(self, direction):
        if direction == 'UP':
            self.y = self.y + self.speed
        elif direction == 'DOWN':
            self.y = self.y - self.speed
        elif direction == 'LEFT':
            self.x = self.x - self.speed
        elif direction == 'RIGHT':
            self.x = self.x + self.speed

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError("You can't fly and crawl")