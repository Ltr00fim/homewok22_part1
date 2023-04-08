class Unit:

    def move(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, crawl: bool, speed: int = 1):

        if is_fly and crawl:
            raise ValueError("You can't fly and crawl")

        movement = []

        if is_fly:
            speed *= 1.2
            movement = self._moveFlyOrCrawl(direction, y_coord, x_coord, speed)
        if crawl:
            speed *= 0.5
            movement = self._moveFlyOrCrawl(direction, y_coord, x_coord, speed)

        field.set_unit(x=movement[0], y=movement[1], unit=self)

    @staticmethod
    def _moveFlyOrCrawl(direction, y_coord, x_coord, speed):
        new_x, new_y = 0, 0
        if direction == 'UP':
            new_y = y_coord + speed
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - speed
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord - speed
        elif direction == 'RIGHT':
            new_y = y_coord
            new_x = x_coord + speed
        return [new_x, new_y]

