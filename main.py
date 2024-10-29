import pygame as p
from math import ceil
from random import randint
from datetime import date, datetime

# import datalog as d

p.init()

now = datetime.now()
game_start = now.strftime('%H:%M:%S')
game_start_day = date.today()

window = p.display.set_mode((700, 600))
window_width = window.get_width()
window_height = window.get_height()

image_height = 50
image_width = 50
image = p.image.load('Char1.png').convert()
image = p.transform.scale(image, (image_height, image_width)).convert()
image2 = p.image.load('Block.png').convert()
image2 = p.transform.scale(image2, (image_height, image_width)).convert()
image3 = p.image.load('Char2.png').convert()
image3 = p.transform.scale(image3, (image_height, image_width)).convert()

score = 0
score_speed = 0.01
score_font = p.font.Font('freesansbold.ttf', 32)
score_text = score_font.render('Score : ' + str(score), True, (0, 0, 0), (255, 255, 255))
score_rect = score_text.get_rect()
score_rect.center = (window_width // 2, 65)

user_font = p.font.Font('freesansbold.ttf', 32)
user_text = user_font.render('Username : ', True, (0, 0, 0), (255, 255, 255))
user_rect = user_text.get_rect()
user_rect.center = (100, 50)

user_font2 = p.font.Font('freesansbold.ttf', 32)
user_text2 = user_font.render('Username : ', True, (0, 0, 0), (255, 255, 255))
user_rect2 = user_text.get_rect()
user_rect2.center = (window_width // 2 - 50, 30)

userhs_font = p.font.Font('freesansbold.ttf', 32)
userhs_text = userhs_font.render('Username (Highest Score): ', True, (0, 0, 0), (255, 255, 255))
userhs_rect = userhs_text.get_rect()
userhs_rect.center = (window_width // 2 - 50, window_height - 75)

# Highest Score
hscore = score
# hscore = d.hscore(mode)
hscore_font = p.font.Font('freesansbold.ttf', 32)
hscore_text = hscore_font.render('Score : ' + str(hscore), True, (0, 0, 0), (255, 255, 255))
hscore_rect = hscore_text.get_rect()
hscore_rect.center = (window_width // 2, window_height - 40)

time_font = p.font.Font('freesansbold.ttf', 32)
time_text = time_font.render('Time : ', True, (0, 0, 0), (255, 255, 255))
time_rect = time_text.get_rect()
time_rect.center = (window_width // 2, window_height - 200)

mode_font = p.font.Font('freesansbold.ttf', 32)
mode_text = mode_font.render('Mode : ', True, (0, 0, 0), (255, 255, 255))
mode_rect = mode_text.get_rect()
mode_rect.center = (60, 150)

mode_font2 = p.font.Font('freesansbold.ttf', 32)
mode_text2 = mode_font2.render('E for Easy; M for Moderate; H for Hard', True, (0, 0, 0), (255, 255, 255))
mode_rect2 = mode_text2.get_rect()
mode_rect2.center = (300, 100)

end_font = p.font.Font('freesansbold.ttf', 32)
end_text = end_font.render('Life is Unfair!', True, (0, 0, 0), (255, 255, 255))
end_rect = end_text.get_rect()
end_rect.center = (window_width // 2 + 22, window_height // 2 - 150)

image.set_colorkey((255, 255, 255))
p.display.set_icon(image)
p.display.set_caption('2AD')

# Coordinates of character
x, y = 100, 300
# y coordinate of obstacle
y2 = 300

# Setting the coordinates of the obstacle
x2 = -100 
x3 = -200
x4 = -300
y_speed = 0.6
obstacle_speed = 1

jump = False
fall = False

jump_height = 200

username = ''
username_given = False
# hsusername = d.hsusername(mode)
hsusername = username

time = 5
time_temp = p.time.get_ticks() // 1000
temp = 0

ch_change = True
mode = None
temp = 0
EASY = 500
MODERATE = 300
HARD = 0

def obstacle():
    global x2, x3, x4
    global obstacle_speed
    global window_width, image_width
    global temp, mode

    temp = window_width + randint(1, 3000)

    if (x3 + image_width) < 0:
        if not (temp < (x2 + mode) or temp < (x4  + mode)):
            x3 = temp
    elif (x2 + image_width) < 0:
        if not (temp < (x3 + mode) or temp < (x4  + mode)):
            x2 = temp
    elif (x4 + image_width) < 0:
        if not (temp < (x2 + mode) or temp < (x3  + mode)):
            x4 = temp

    x2 -= obstacle_speed
    x3 -= obstacle_speed
    x4 -= obstacle_speed

def gquit():
    global username, score, game_start, game_start_day
    now = datetime.now()
    game_quit = now.strftime('%H:%M:%S')
    game_end_day = date.today()
    # d.gamelog(username, ceil(score), mode, game_start, game_quit, game_start_day, game_end_day)
    p.quit()
    quit()

stop = 0
# Loop Condition
lcond = True

while lcond:
    for event in p.event.get():
        if event.type == p.QUIT:
            gquit()
        if event.type == p.KEYDOWN:
            if username_given == False:
                if username != '' and event.key == p.K_RETURN:
                    username_given = True
                elif username != '' and event.key == p.K_BACKSPACE:
                    username = username[:-1]
                    user_text = user_font.render('Username : ' + username, True, (0, 0, 0), (255, 255, 255))
                else:
                    if event.unicode.isalnum() or event.unicode in '$!?@_':
                        username += event.unicode
                        user_text = user_font.render('Username : ' + username, True, (0, 0, 0), (255, 255, 255))
            elif mode == None:
                    if event.unicode in ['e', 'm', 'h']:
                        if event.unicode == 'e':
                            mode = EASY
                        elif event.unicode == 'm':
                            mode = MODERATE
                        elif event.unicode == 'h':
                            mode = HARD
            else:
                if event.key == p.K_SPACE:
                    if fall == False:
                        jump = True
                        ch_change = False
                elif event.key == p.K_q:
                        gquit()

    if username_given == False:
        window.fill((255, 255, 255))
        window.blit(user_text, user_rect)

    elif username_given == True and mode == None:
        window.blit(mode_text, mode_rect)
        window.blit(mode_text2, mode_rect2)

    elif not stop and username_given == True and mode != None:
        window.fill((255, 255, 255))

        if time >= 0:
            hsusername = username # Delete this line later
            user_text2 = user_font.render('Username : ' + username, True, (0, 0, 0), (255, 255, 255))
            userhs_text = userhs_font.render('Username (Highest Score): ' + hsusername, True, (0, 0, 0), (255, 255, 255))
            time_text = time_font.render('Time : ' + str(time), True, (0, 0, 0), (255, 255, 255))
            window.blit(time_text, time_rect)
            p.time.delay(1000)
            time -= 1
        else:
            score += score_speed

            if jump == True and y > jump_height:
                y -= y_speed
            else:
                jump = False
                fall = True
            if fall == True and  y < 300:
                y += y_speed
            else:
                fall = False
                ch_change = True

            for i in range(ceil(x), ceil(x) + 31):
                if i == ceil(x2):
                    for j in range(ceil(y), ceil(y) + 31):
                        if j == ceil(y2):
                            stop = True
                            print('\a\a\a\a') # Error sound
                if i == ceil(x3):
                    for j in range(ceil(y), ceil(y) + 31):
                        if j == ceil(y2):
                            stop = True
                            print('\a\a\a\a') # Error sound
                if i == ceil(x4):
                    for j in range(ceil(y), ceil(y) + 31):
                        if j == ceil(y2):
                            stop = True
                            print('\a\a\a\a') # Error sound

            score_text = score_font.render('Score : ' + str(ceil(score)), True, (0, 0, 0), (255, 255, 255))
            obstacle()

        if ceil(score) % 2 == 0 and ch_change:
            window.blit(image3, (x, y))
        else:
            window.blit(image, (x, y))

        if hscore < score:
            hscore_text = hscore_font.render('Score : ' + str(ceil(score)), True, (0, 0, 0), (255, 255, 255))
        else:
            hscore_text = hscore_font.render('Score : ' + str(hscore), True, (0, 0, 0), (255, 255, 255))
            
        window.blit(image2, (x2, y2))
        window.blit(image2, (x3, y2))
        window.blit(image2, (x4, y2))
        window.blit(score_text, score_rect)
        window.blit(user_text2, user_rect2)
        window.blit(userhs_text, userhs_rect)
        window.blit(hscore_text, hscore_rect)
        p.draw.rect(window, (0, 0, 0), p.Rect(0, y2 + image_height, window_width, 5))

    else:
        p.time.wait(2000)
        if stop == 1:
            p.draw.rect(window, (0, 0, 0), p.Rect(0, y2 + image_height, window_width, 5))
            # Reusing user_text since it, no longer, has any other use
            user_text = user_font.render('Press Q to Quit', True, (0, 0, 0), (255, 255, 255))
            user_rect.center = (window_width // 2, window_height // 2 - 100)
            window.blit(end_text, end_rect)
            stop += 1
        elif stop == 2:
            p.time.wait(250)
            window.blit(user_text, user_rect)
            stop += 1

    p.display.update()

p.quit()
