import sys, random, pygame
from pygame.locals import *


def print_text(font, x, y, text, color=(255, 0, 0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

# 初始化pygame
pygame.init()
# 窗口大小
window_width, window_height = 800, 600
# 设置窗口和游戏名称
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('我的游戏自己取名')
level = 0
# 导入背景图片
background_image = pygame.image.load("resources/images/background.png")
screen.blit(background_image, (0, 0))
# 导入玩仔图片
wanzai = pygame.image.load("resources/images/wanzai.png")
wanzai_width, wanzai_height = wanzai.get_size()
# 设置字体
font1 = pygame.font.SysFont('simhei', 24)
gameove_font = pygame.font.SysFont('simhei', 54)
# 计算中心坐标
wanzai_left, wanzai_top = window_width // 2, window_height // 2
# 计算玩仔中心对齐的左上角坐标
wanzai_left, wanzai_top = wanzai_left - wanzai_width // 2, wanzai_top - wanzai_height // 2
screen.blit(wanzai, (wanzai_left, wanzai_top))
dianchi_speed = 8
lives, number = 1, 0
#电池精灵组
battery_group=pygame.sprite.Group()
#电池类
class Battery(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources\images\dianchi.png")
        self.wanzai_width, self.wanzai_height = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
    def move(self):
        self.rect=self.rect.move([0,dianchi_speed])
#新电池函数
def next_battery():
    battery_top = 0
    battery_left = random.randint(0, 800)
    pos=(battery_left,battery_top)
    # 添加进电池组
    battery_group.add(Battery(pos))

    
while True:
    # 对于事件列表里的每一个事件
    for event in pygame.event.get():
        # 如果事件为退出
        if event.type==pygame.QUIT:
            sys.exit()
        # 如果事件为移动鼠标
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
    screen.blit(background_image, (0, 0))
    wanzai_left, wanzai_top = mouse_x - wanzai_width // 2, mouse_y - \
                              wanzai_height // 2
    #生成新电池
    next_battery()   
    for battery in battery_group:
        battery.move()
        screen.blit(battery.image,battery.rect)
        if wanzai_left <= battery.rect.left and battery.rect.left + battery.wanzai_width <= \
     wanzai_left + wanzai_width and wanzai_top < battery.rect.top:
            number += 1
            battery_group.remove(battery)
        if battery.rect.top > window_height:  # miss a dianchi
            # lives -= 1
            battery_group.remove(battery)
    screen.blit(wanzai, (wanzai_left, wanzai_top))    
    print_text(font1, 0, 0, "生命值: " + str(lives))
    print_text(font1, 200, 0, "已接电池数: " + str(number))
    pygame.display.update()
