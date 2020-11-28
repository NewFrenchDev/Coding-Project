import pygame


class Button(pygame.Rect):

    def __init__(self, color=[133, 133, 133], x=0, y=0, width=0, height=0, text='', action=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        self.button_pressed = False

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont("comicsans", 20)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

    def click_on_button(self, screen):
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.is_over(pos):
            if click[0] == 1:
                self.button_pressed = True

    def display(self):
        print(f"Button {self.text} pressed")

    def display_proposition(self, screen, text="Test"):
        self.text = text
        self.draw(screen, outline=(0, 0, 0))