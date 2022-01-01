import pygame, random, time

pygame.init()


def playing(width, height):
    end = False
    screen = pygame.display.set_mode((width, height))
    pole = [[False] * (width//50) for x in range(height//50)]
    q = 60
    pols_pole = [[-1] * (width // 50) for fd in range(height//50)]
    cl = [[[0, 0] for t in range(width//50)] for r in range(height//50)]
    qounter = 0
    image_fl = pygame.image.load("D://Программирование/Python/miner/dist/image/flag_orange.png")
    j = []
    col_vo_fl = 0

    def open(i, j, rev=False):
        qounter = 0
        r = False
        for y in cl:
            if (i * 50, j * 50) in y:
                return
        print(j, i)
        cl[j][i] = (i * 50, j * 50)
        if pole[j][i] and not rev:
            while True:
                for h in pygame.event.get():
                    if h.type == pygame.QUIT:
                        return -50
                game_over = pygame.font.SysFont("Calibri", 50)
                game_over_print = game_over.render("GAME OVER", False, (255, 100, 100))
                screen.blit(game_over_print, (width // 2-100, height // 2-50))
                pygame.display.flip()
        if pole[j][i] and rev:
            r = True
        if pols_pole[j][i] == -1 and not r:
            qounter = 0
            if j <= height//50-2 and pole[j + 1][i]:
                qounter += 1
            if j >= 1 and pole[j - 1][i]:
                qounter += 1
            if i <= width//50-2 and pole[j][i + 1]:
                qounter += 1
            if i >= 1 and pole[j][i - 1]:
                qounter += 1
            if j <= height//50-2 and i <= width//50-2 and pole[j + 1][i + 1]:
                qounter += 1
            if j <= height//50-2 and i >= 1 and pole[j + 1][i - 1]:
                qounter += 1
            if j >= 1 and i <= width//50-2 and pole[j - 1][i + 1]:
                qounter += 1
            if j >= 1 and i >= 1 and pole[j - 1][i - 1]:
                qounter += 1
        if qounter == 0:
            if i <= width//50-2:
                open(i + 1, j, True)
                if j >= 1:
                    open(i + 1, j - 1, True)
                if j <= height//50-2:
                    open(i + 1, j + 1, True)
            if i >= 1:
                open(i - 1, j, True)
                if j >= 1:
                    open(i - 1, j - 1, True)
                if j <= height//50-2:
                    open(i - 1, j + 1, True)
            if j >= 1:
                open(i, j - 1, True)
            if j <= height//50-2:
                open(i, j + 1, True)
        if pols_pole[j][i] != -10:
            pols_pole[j][i] = qounter
        print("ok")

    for t in range((width//50*height//50)//10):
        x = random.randint(0, width//50-1)
        y = random.randint(0, height//50-1)
        while [x, y] in j:
            x = random.randint(0, width//50-1)
            y = random.randint(0, height//50-1)
        j.append([x, y])
    for k in j:
        pole[k[1]][k[0]] = True
    time_begin = time.time() // 60
    time_begin_2 = time.time() % 60
    while True:
        screen.fill((240, 240, 240))
        time_now = time.time() // 60
        time_now_2 = time.time() % 60
        real_time = int(time_now - time_begin)
        if time_now_2 >= time_begin_2:
            real_time_2 = int(time_now_2 - time_begin_2)
        else:
            real_time -= 1
            real_time_2 = int(60 - (time_begin_2 - time_now_2))
        end = True
        for n in pols_pole:
            if -1 in n:
                end = False
                break
        if end:
            while True:
                for h in pygame.event.get():
                    if h.type == pygame.QUIT:
                        return
                game = pygame.font.SysFont("Calibri", 50)
                game_print = game.render("YOU WINNER!!!", False, (255, 100, 100))
                screen.blit(game_print, (width // 2 - 120, height // 2 - 50))
                pygame.display.flip()
        for t in range(0, width//50):
            for u in range(0, height//50):
                if pols_pole[u][t] == -1:
                    pygame.draw.rect(screen, (0, 55, 10), (t * 50, u * 50, 49, 49))
                elif pols_pole[u][t] > -1:
                    font_num = pygame.font.SysFont("Calibri", 50)
                    s = font_num.render("" if pols_pole[u][t] == 0 else str(pols_pole[u][t]), False, (0, 0, 255))
                    screen.blit(s, (cl[u][t][0], cl[u][t][1]))
                elif pols_pole[u][t] == -10:
                    screen.blit(image_fl, (cl[u][t][0], cl[u][t][1]))
        timing = pygame.font.SysFont("Calibri", 50)
        time_print = timing.render(str(real_time) + "." + str(real_time_2), False, (0, 0, 0))
        screen.blit(time_print, (width-100, 20))
        for y in pygame.event.get():
            if y.type == pygame.QUIT:
                return
            elif y.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == 1:
                    pos = pygame.mouse.get_pos()
                    if open(pos[0] // 50, pos[1] // 50) == -50:
                        return
                else:
                    pos_2 = pygame.mouse.get_pos()
                    if pols_pole[pos_2[1] // 50][pos_2[0] // 50] == -1 and col_vo_fl < 11:
                        cl[pos_2[1] // 50][pos_2[0] // 50] = [pos_2[0] // 50 * 50, pos_2[1] // 50 * 50]
                        pols_pole[pos_2[1] // 50][pos_2[0] // 50] = -10
                        col_vo_fl += 1
                    elif pols_pole[pos_2[1] // 50][pos_2[0] // 50] == -10:
                        if col_vo_fl > 0:
                            col_vo_fl -= 1
                        pols_pole[pos_2[1] // 50][pos_2[0] // 50] = -1
        pygame.display.flip()


while True:
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    screen.fill((100, 100, 100))
    play_8_8 = pygame.Rect((50, 50, 100, 100))
    font_8_8 = pygame.font.SysFont("Calibri", 50)
    font_8_8_print = font_8_8.render("8 * 8", False, (255, 255, 0))
    play_10_10 = pygame.Rect((347, 50, 100, 100))
    font_10_10 = pygame.font.SysFont("Calibri", 36)
    font_10_10_print = font_10_10.render("10 * 10", False, (255, 255, 0))
    play_13_13 = pygame.Rect((50, 300, 100, 100))
    font_13_13 = pygame.font.SysFont("Calibri", 36)
    font_13_13_print = font_13_13.render("13 * 13", False, (255, 255, 0))
    play_16_16 = pygame.Rect((350, 300, 100, 100))
    font_16_16 = pygame.font.SysFont("Calibri", 36)
    font_16_16_print = font_16_16.render("16 * 16", False, (255, 255, 0))
    for t in pygame.event.get():
        if t.type == pygame.QUIT:
            exit(50)
        elif t.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_2 = pygame.Rect((pos[0], pos[1], 1, 1))
            if play_8_8.colliderect(pos_2):
                playing(8 * 50, 8 * 50)
            elif play_10_10.colliderect(pos_2):
                playing(10*50, 10*50)
            elif play_13_13.colliderect(pos_2):
                playing(13*50, 13*50)
            elif play_16_16.colliderect(pos_2):
                playing(16*50, 16*50)
    pygame.draw.rect(screen, (255, 200, 0), (50, 50, 100, 100))
    pygame.draw.rect(screen, (255, 200, 0), (350, 50, 100, 100))
    pygame.draw.rect(screen, (255, 200, 0), (50, 300, 100, 100))
    pygame.draw.rect(screen, (255, 200, 0), (350, 300, 100, 100))
    screen.blit(font_8_8_print, (50, 80))
    screen.blit(font_10_10_print, (347, 80))
    screen.blit(font_13_13_print, (48, 340))
    screen.blit(font_16_16_print, (348, 340))
    pygame.display.flip()
