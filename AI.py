import pygame

global TEST_AI

TEST_AI = True
(DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT) = range(4)

def drawAstarSearch(screen, enemies):
    #print(enemies[0].direction)
    index = 0
    for enemie in enemies:
        color3 = 50 + 50 * (index % 4)
        color2 = 100 + 50 * (index % 3)
        color1 = 23 * (index % 4)
        if enemie.path == None:
            return
        for position in enemie.path:
            p = [position[0] + 480, position[1]]
            screen.fill([color3, color2, color1], pygame.Rect(p , [26, 26]))
        index += 1
    return

'''
    Generate a display window on the right side of
    original game window.
'''
def generate_map_forai(screen, topleft):

    screen.fill([0, 255, 255], pygame.Rect(topleft, [16, 16]))
    return


def update_astarMap(astar_map, player_position = None, recover = True):
    x = int(round(player_position[1] / 16))
    y = int(round(player_position[0] / 16))

    if recover == True:
        score_player = 1
    else:
        score_player = 9999

    astar_map[x][y] = score_player
    if x < 25:
        astar_map[x + 1][y] = score_player
    if y < 25:
        astar_map[x][y + 1] = score_player
    if x < 25 and y < 25:
        astar_map[x + 1][y + 1] = score_player


