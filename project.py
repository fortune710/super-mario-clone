import pygame
from mario import Mario
from time import sleep

pygame.init()
screen_width = 600
screen_height = 650
pos = []
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario Clone")



#This is for playing background music
pygame.mixer.music.load("background-music.mp3")
pygame.mixer.music.set_volume(0.35)
pygame.mixer.music.play(-1)

#This is for Sound Effects
jump_sound_effect = pygame.mixer.Sound("jump-effect.mp3")
jump_sound_effect.set_volume(0.4)

#These are for the game backgound
background_color = pygame.Color(255, 255, 255)


#pos = (screen_width // 2, screen_height // 2)
mario = Mario(100, 150)
actor_group = pygame.sprite.Group()
actor_group.add(mario)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_sound_effect.play()
                mario.rect.centery += 100
                mario.update_jump()

                for i in range(0, 5):
                    sleep(0.15)
                    mario.rect.centery -= 20
                
                mario.set_idle_image()

            if event.key == pygame.K_RIGHT:
                pygame.key.set_repeat(80, 40)

                mario.rect.centerx += 4
                mario.update_walk()

    #actor_group.update()
    screen.fill(background_color)
    pygame.draw.rect(screen, (255, 0, 0), (0, 20, screen_width, 200))
    screen.blit(mario.image, mario.rect)
    #actor_group.draw(screen)

    pygame.display.update()
pygame.quit()
    

