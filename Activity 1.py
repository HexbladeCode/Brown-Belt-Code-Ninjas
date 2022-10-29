import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

class Ball(object):
    def __init__(self, screen, radius, x, y):
        self.__screen = screen
        self.__radius = radius
        self.xLoc = x
        self._yLoc = y
        self.__xVel = 5
        self.__yVel = -3
        w, h = pygame.display.get_surface().get_size()
        self.__width = w
        self.__height = h

    def draw(self):

        pygame.draw.circle(screen, (255, 0, 0), (self._xLoc, self._yLoc), self._radius)

        def update(self, paddle, brickwall):

            self._xLoc += self.__xVel
            self._yLoc += self.__yVel
            if self._xLoc == self.radius:
                self.__xVel *= -1
            elif self._xLoc >= self.__width - self.radius:
                self.__xVel *= -1
            if self.yLoc == self._radius:
                self.__yVel *= -1
            elif self._yLoc >= self.__height - self._radius:
                return True

        if brickwall.collide(self):
            self.__yVel *=-1

        paddleX = paddle._xLoc
        paddleY = paddle._yLoc
        paddleW = paddle._width
        paddleH = paddle._height
        ballX = self._xLoc
        ballY = self._yLoc

        if ((ballX + self._radius) > paddleX and ballX <= (paddleX + paddleW)) \
            and ((ballY + self._radius) >= paddleY and ballY <= (paddleY + paddleH)):
            self.__yVel *= -1

        return False

class Paddle(object):
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h

    def draw(self):

        pygame.draw.rect(screen, (0, 0, 0), (self._xLoc, self._yLoc, self._width, self._width, self._height), 0)

    def update(self):

        x, y = pygame.mouse.get_pos()
        if x >= 0 and x <= (self.__W - self._width):
            self._xLoc = x

class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, x, y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = y
        self._yLoc = y
        w, y = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h
        self.__isInGroup = False

    def draw(self):

        pygame.draw.rect(screen, (56, 177, 237), (self._xLoc, self._yLoc, self._width, self._height), 0)

    def add(self, group):

        group.add(self)
        self.__isInGroup = True

    def remove(self, group):

        group.remove(self)
        self.__isInGroup = False

    def alive(self):
        return self.__isInGroup

    def collide(self, ball):

        brickX = self._xLoc
        brickY = self._yLoc
        brickW = self._width
        brickH = self._height
        ballX = ball._xLoc
        ballY = ball._yLoc
        radius = ball.radius

        if ((ballX + radius) >= brickX and ballX <= (brickX + brickW)) \
            and ((ballY + radius) >= brickY and ballY <= (brickY + brickH)):
            return True

        return False


class BrickWall(pygame.sprite.Group):
    def __init__(self, screen, x, y, width, height):
        self.__screen = screen
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._bricks = []

        X = x
        Y = y
        for i in range(3):
            for j in range(4):
                self._bricks.append(Brick(screen, width, height, X, Y))
                X += width + (width / 7.0)
            Y += height + (height / 7.0)
            X = x

    def add (self, brick):
        self._bricks.append(brick)

    def remove (self, brick):
        self._bricks.remove(brick)

    def draw (self):
        for brick in self._bricks:
            if brick != None:
                brick.draw()