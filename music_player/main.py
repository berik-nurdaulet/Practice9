import pygame
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

player = MusicPlayer("music")

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.prev_track()

            elif event.key == pygame.K_q:
                running = False

  
    track_text = font.render(
        f"Track: {player.get_current_track_name()}",
        True,
        (255, 255, 255)
    )
    screen.blit(track_text, (20, 50))

    
    time_text = font.render(
        f"Time: {player.get_position()} sec",
        True,
        (200, 200, 200)
    )
    screen.blit(time_text, (20, 100))

    controls = [
        "P = Play",
        "S = Stop",
        "N = Next",
        "B = Previous",
        "Q = Quit"
    ]

    for i, text in enumerate(controls):
        ctrl = font.render(text, True, (180, 180, 180))
        screen.blit(ctrl, (20, 150 + i * 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()