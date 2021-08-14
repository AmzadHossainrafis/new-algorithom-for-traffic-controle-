import pygame as pygame



def display_update(rect_1, rect_2,BORDER,rect_1_bullet, rect_2_bullet, rect_1_health , rect_2_health):
    WIN.blit(back_g,(0,0))
    
    WIN.blit(ship_red,(rect_1.x, rect_1.y))
    WIN.blit(ship_yolo,(rect_2.x,rect_2.y))
    
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(rect_1_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(rect_2_health), 1, WHITE)
    pygame.draw.rect(WIN, COLOR_BLACK, BORDER )
    WIN.blit(red_health_text, (500 - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    for bullet in rect_1_bullet:
        pygame.draw.rect(WIN, COLOR_BLACK, bullet)

    for bullet in rect_2_bullet:
        pygame.draw.rect(WIN, COLOR_RED, bullet)
    pygame.display.update()


def move_rect_1(key_press,rect_1):
    if key_press[pygame.K_a] and rect_1.x - mov > 0:
        rect_1.x -= mov
    if key_press[pygame.K_d] and rect_1.x +mov < 210:
        rect_1.x += mov
    if key_press[pygame.K_w] and rect_1.y > 0:
        rect_1.y-= mov
    if key_press[pygame.K_s] and rect_1.y < 450:
        rect_1.y+= mov

def move_rect_2(key_press,rect_2):
    if key_press[pygame.K_LEFT] and rect_2.x - mov > BORDER.x +BORDER.width:
        rect_2.x -= mov
    if key_press[pygame.K_RIGHT] and rect_2.x + mov + rect_2.width < 490:
        rect_2.x += mov
    if key_press[pygame.K_UP] and rect_2.y > 0:
        rect_2.y-= mov
    if key_press[pygame.K_DOWN] and rect_2.y < 450:
        rect_2.y+= mov


def bullet_move(rect_1_bullet,rect_2_bullet, rect_1, rect_2):
    for bullet in rect_1_bullet:
        bullet.x+= bullet_mov
        if rect_2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(rect_2_hit))
            rect_1_bullet.remove(bullet)
        elif bullet.x > 500:
            rect_1_bullet.remove(bullet)

    for bullet in rect_2_bullet:
        bullet.x-= bullet_mov
        if rect_1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(rect_1_hit))
            rect_2_bullet.remove(bullet)
        elif bullet.x < 0:
            rect_2_bullet.remove(bullet)
