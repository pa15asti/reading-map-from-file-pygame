import pygame

pygame.init()
boxlist = []
pygame.display.set_caption('Mario')
screen = pygame.display.set_mode((500, 500))

def listappend():
    f = open('data2/map.txt')
    for line in f:
        for symb in line:
            listsymb.append(symb)

def render(screen, list, marcoord, boxlist):
    index = 0
    box = pygame.image.load('data2/box.png')
    grass = pygame.image.load('data2/grass.png')
    for a in list:
        if '\n' in list:
            list.remove('\n')
    for x in range(0, 500, 50):
        for y in range(0, 500, 50):
            if list[index] == '#':
                screen.blit(box, (y, x))
                if (y, x) not in boxlist:
                    boxlist.append((y, x))
            if list[index] == '=':
                screen.blit(grass, (y, x))
            index += 1
    mar = pygame.image.load('data2/mar.png')
    screen.blit(mar, marcoord)


running = True
fon = True
listsymb = []
listappend()
marcoord = (200, 200)
while running:
    while fon:
        fonn = pygame.image.load('data2/fon.jpg')
        fonn = pygame.transform.scale(fonn, (500, 500))
        screen.blit(fonn, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                fon = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fon = False
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (marcoord[0] - 50, marcoord[1]) not in boxlist:
                    marcoord = (marcoord[0] - 50, marcoord[1])
            elif event.key == pygame.K_RIGHT:
                if (marcoord[0] + 50, marcoord[1]) not in boxlist:
                    marcoord = (marcoord[0] + 50, marcoord[1])
            elif event.key == pygame.K_UP:
                if (marcoord[0], marcoord[1] - 50) not in boxlist:
                    marcoord = (marcoord[0], marcoord[1] - 50)
            elif event.key == pygame.K_DOWN:
                if (marcoord[0], marcoord[1] + 50) not in boxlist:
                    marcoord = (marcoord[0], marcoord[1] + 50)
    pygame.display.flip()
    render(screen, listsymb, marcoord, boxlist)
pygame.quit()