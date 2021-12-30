import pygame, random, time

pygame.init()


def open(i, j, rev=False):
    global screen, pole, qounter, pols_pole, cl
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
                    exit(42)
            game_over = pygame.font.SysFont("Calibri", 70)
            game_over_print = game_over.render("GAME OVER", False, (255, 100, 100))
            screen.blit(game_over_print, (150, 150))
            pygame.display.flip()
    if pole[j][i] and rev:
        r = True
    if pols_pole[j][i] == -1 and not r:
        qounter = 0
        if j <= 6 and pole[j + 1][i]:
            qounter += 1
        if j >= 1 and pole[j - 1][i]:
            qounter += 1
        if i <= 10 and pole[j][i + 1]:
            qounter += 1
        if i >= 1 and pole[j][i - 1]:
            qounter += 1
        if j <= 6 and i <= 10 and pole[j + 1][i + 1]:
            qounter += 1
        if j <= 6 and i >= 1 and pole[j + 1][i - 1]:
            qounter += 1
        if j >= 1 and i <= 10 and pole[j - 1][i + 1]:
            qounter += 1
        if j >= 1 and i >= 1 and pole[j - 1][i - 1]:
            qounter += 1
    if qounter == 0:
        if i <= 10:
            open(i + 1, j, True)
            if j >= 1:
                open(i + 1, j - 1, True)
            if j <= 6:
                open(i + 1, j + 1, True)
        if i >= 1:
            open(i - 1, j, True)
            if j >= 1:
                open(i - 1, j - 1, True)
            if j <= 6:
                open(i - 1, j + 1, True)
        if j >= 1:
            open(i, j - 1, True)
        if j <= 6:
            open(i, j + 1, True)
    if pols_pole[j][i] != -10:
        pols_pole[j][i] = qounter
    print("ok")


width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pole = [[False] * 12 for x in range(8)]
q = 60
pols_pole = [[-1] * 12 for fd in range(8)]
cl = [[[0, 0] for t in range(12)] for r in range(8)]
qounter = 0
image_fl = pygame.image.load("image/flag_orange.png")
j = []
end = False
col_vo_fl = 0
for t in range(11):
    x = random.randint(0, 11)
    y = random.randint(0, 7)
    while [x, y] in j:
        x = random.randint(0, 11)
        y = random.randint(0, 7)
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
                    exit(42)
            game = pygame.font.SysFont("Calibri", 70)
            game_print = game.render("YOU WINNER!!!", False, (255, 100, 100))
            screen.blit(game_print, (100, 100))
            pygame.display.flip()
    for t in range(0, 12):
        for u in range(0, 8):
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
    screen.blit(time_print, (520, 10))
    for y in pygame.event.get():
        if y.type == pygame.QUIT:
            exit(3)
        elif y.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:
                pos = pygame.mouse.get_pos()
                open(pos[0] // 50, pos[1] // 50)
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
