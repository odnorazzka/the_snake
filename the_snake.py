from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """
    Базовый класс, от которого наследуются все объекты.
    Содержит общие атрибуты: позиция и цвет.
    """

    def __init__(self, position=None, body_color=None):
        """
        Конструктор базового игрового объекта.
        Аргументы: position (координаты), body_color (цвет).
        """
        if position is None:
            self.position = (320, 240)
        else:
            self.position = position
    
    def draw(self, surface):
        """
        Абстрактный метод для отрисовки объекта на экране.
        Аргумент: surface (поверность, на которой рисуем)
        """ 
        pass

class Apple(GameObject):
    """
    Класс Apple. Наследуюется от GameObject.
    Появляется в случайном месте поля.
    """
    apple_color = (255, 0, 0)

    super().__init__(position=None, body_color=apple_color)

    self.radomize_position()

    def randomize_position(self):
        """
        Устанавливает случайные координаты для яблока.
        """
        max_x = 640 - 20
        max_y = 480 - 20

        x.random.randrage(0, max_x + 1, 20)
        y.random.randrage(0, max_y + 1, 20)

        self.position = (x, y)

    def draw(self, surface):
        """
        Отрисовывет яблоко на игровом поле.
        """

        rect = pygame.Rect(
            self.position[0],
            self.position[1],
            20,
            20
        )

        pygame.draw.rect(surface, self.body_color, rect)

class Snake(GameObject):
    """Класс змейки. Управляет движением, ростом и столкновениями."""

    def __init__(self):
        """Инициализирует змейку в начальном состоянии."""
        super().__init__(body_color=SNAKE_COLOR)
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        """
        Возвращает позицию головы змейки.

        Возвращает:
            tuple: Координаты (x, y) головы змейки.
        """
        return self.positions[0]

    def update_direction(self):
        """Обновляет направление движения змейки после нажатия клавиши."""
        if self.next_direction:
            next_dx, next_dy = self.next_direction
            dx, dy = self.direction
            if next_dx != -dx or next_dy != -dy:
                self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """
        Перемещает змейку на одну клетку вперёд.
        Реализует прохождение сквозь стены и проверку на самопересечение.
        """
        head = self.get_head_position()
        dx, dy = self.direction
        new_x = (head[0] + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (head[1] + dy * GRID_SIZE) % SCREEN_HEIGHT
        new_head = (new_x, new_y)

        if new_head in self.positions:
            self.reset()
            return

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def grow(self):
        """Увеличивает длину змейки при съедании яблока."""
        self.length += 1
        if self.last:
            self.positions.append(self.last)
            self.last = None

    def reset(self):
        """Сбрасывает змейку в начальное состояние после столкновения."""
        self.length = 1
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def draw(self, surface):
        """
        Отрисовывает змейку на игровой поверхности.
        Затирает последний сегмент, чтобы не было "следа".

        Аргументы:
            surface: Поверхность pygame для рисования.
        """
        if self.last:
            last_rect = pygame.Rect(
                self.last[0], self.last[1], GRID_SIZE, GRID_SIZE
            )
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

        for position in self.positions:
            rect = pygame.Rect(
                position[0], position[1], GRID_SIZE, GRID_SIZE
            )
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    ...

    # while True:
    #     clock.tick(SPEED)


if __name__ == '__main__':
    main()
