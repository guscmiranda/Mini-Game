import pygame

class BackgroundManager:
    def __init__(self, img_path, img_path_cont, screen_height=720, speed=15):

        # Primeira imagem
        img1_orig = pygame.image.load(img_path).convert()
        w1_orig, h1_orig = img1_orig.get_size()
        prop1 = screen_height / h1_orig
        new_w1 = int(w1_orig * prop1)
        img1_scaled = pygame.transform.smoothscale(img1_orig, (new_w1, screen_height))

        # Segunda imagem
        img2_orig = pygame.image.load(img_path_cont).convert()
        w2_orig, h2_orig = img2_orig.get_size()
        prop2 = screen_height / h2_orig
        new_w2 = int(w2_orig * prop2)
        img2_scaled = pygame.transform.smoothscale(img2_orig, (new_w2, screen_height))

        self.width = new_w1 + new_w2
        self.image = pygame.Surface((self.width, screen_height))

        # Cola a imagem 1 no começo (x=0)
        self.image.blit(img1_scaled, (0, 0))
        # Cola a imagem 2 logo em seguida (x=new_w1)
        self.image.blit(img2_scaled, (new_w1, 0))

        self.x = 0
        self.speed = speed

    def update(self, dt):
        self.x -= self.speed * dt

        if self.x < -self.width:
            self.x += self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + self.width, 0))