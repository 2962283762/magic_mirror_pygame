from pickle import TRUE
from tkinter.font import NORMAL
import pygame
import sys
import post_request
import time
import schedule
from playsound import playsound
import weather
import datetime
from post_request import history_day,img,terminal
#全局变量
x,y=0,0
i = 0
bg_bool = 0
kbn_i = 1

BLACK = (0,0,0)
WHITE = (255,255,255)
date_location = (0,0)
lunar_location = (0,40)
temporal_location = (150,40)
text_lcoation = (0,90)
img_location = (549,0)
wheather_location = (350,52)
history_day_location = (0,700)
bg_img_location = (0,0)
kbn_location = (500,650)


#周期初始化函数
def main_init():
    global x,y,i
    x,y = 300,400
    i = 0
    kbn_x, kbn_y = 0, 0

def tk_main():
    tkinter.geometry("200x300")




#单次运行

state_text_source = post_request.state()
wheather_source = post_request.wehather()
wheather_text = str(wheather_source[3][0])
wheather_code = str(wheather_source[2][0])
wheather_temp = str(wheather_source[1][0])
img_path = f"/home/pi/Desktop/dd/{wheather_code}@1x.png"
wheather_str = f"天气：{wheather_text}\n气温：{wheather_temp} 摄氏度"
pp = post_request.now_day()
histor_list = post_request.history_day(i)
history_text = "那年今天:" +  "\n" + histor_list
img()
bg_img_path = "/home/pi/Desktop/dd/bg.png"
kbn_img_path = f"/home/pi/Desktop/dd/kbn/{kbn_i}.png"
#字体及pygame初始化
pygame.init()

fontObj = pygame.font.Font("/home/pi/Desktop/dd/sanji.ttf", 30)
stateObj = pygame.font.Font("/home/pi/Desktop/dd/sanji.ttf", 20)
sanjiObj = pygame.font.Font("/home/pi/Desktop/dd/sanji.ttf",20)
course = pygame.font.Font('/home/pi/Desktop/dd/sanji.ttf',20)

#一言文本函数
def text_fun():
    global state_text_source
    state_text_source = post_request.state()

#播放函数
def auto_loud():
    last_text = weather.state0()
    post_request.autop(last_text)
    playsound('/home/pi/Desktop/dd/audio.mp3')






#时间请求
def time_func():
    global pp
    pp = post_request.now_day()

#历史的今天
def history():
    global history_text,i
    histor_list = post_request.history_day(i)
    history_text = "那年今天:" +  "\n" + histor_list
#天气函数
def wheather_func():
    global wheather_source,wheather_text,wheather_code,wheather_temp,wheather_str,img_path
    state_text_source = post_request.state()
    wheather_source = post_request.wehather()
    wheather_text = str(wheather_source[3][0])
    wheather_code = str(wheather_source[2][0])
    wheather_temp = str(wheather_source[1][0])
    img_path = f"/home/pi/Desktop/dd/{wheather_code}@1x.png"
    wheather_str = f"天气：{wheather_text}\n气温：{wheather_temp} 摄氏度"


def mouse_action_get():
    global x,y,i,bg_bool
    x_get, y_get = pygame.mouse.get_pos()

    if(x - x_get >=70):
        bg_bool = 1

        x_get,y_get = 0,0
    if(x - x_get <= -70):
        bg_bool = 0
    if(y - y_get >= 70):
        text_fun()
        x_get,y_get = 0,0
    if(y_get - y >= 70):
        i += 1
        history()


def kbn():
    global kbn_x,kbn_y
    if(kbn_x>=500 or kbn_y>=650):
        print("aa")
        img()


#pygame的上载函数
def upgrde_time():
    global kbn_i
    screen = pygame.display.set_mode((600,1050),pygame.NOFRAME)
    screen.fill(BLACK)
    bg_img_load = pygame.image.load(bg_img_path)
    if(bg_bool == 1):
        screen.blit(bg_img_load,bg_img_location)
    if(kbn_i>4):
        kbn_i = 1
    kbn_load = pygame.image.load(kbn_img_path)
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    textSurfaceObj = fontObj.render(str(now_time), True,WHITE)
    lunar_text = fontObj.render(str(pp[1][0]),True,WHITE)
    temporal_text = fontObj.render(str(pp[2][0]),True,WHITE)
    wheather_img = pygame.image.load(img_path)
    line0 = pygame.draw.line(screen,WHITE,(0,80),(600,80),5)
    state_text = stateObj.render(state_text_source,True,WHITE)
    wheather_text_last = sanjiObj.render(wheather_str,True,WHITE)
    history_last = sanjiObj.render(history_text,True,WHITE)
    screen.blit(wheather_text_last,wheather_location)
    screen.blit(state_text,text_lcoation)
    screen.blit(temporal_text,temporal_location)
    screen.blit(lunar_text,lunar_location)
    screen.blit(textSurfaceObj, date_location)
    screen.blit(wheather_img,img_location)
    screen.blit(history_last,history_day_location)
    line01 = pygame.draw.line(screen,WHITE,(0,150),(500,150),3)
    line02 = pygame.draw.line(screen,WHITE,(0,650),(500,650),3)
    line03 = pygame.draw.line(screen,WHITE,(500,150),(500,650),3)
    line04 = pygame.draw.line(screen,WHITE,(0,250),(500,250),3)
    line05 = pygame.draw.line(screen,WHITE,(0,350),(500,350),3)
    line06 = pygame.draw.line(screen,WHITE,(0,450),(500,450),3)
    line07 = pygame.draw.line(screen,WHITE,(0,550),(500,550),3)
    line08 = pygame.draw.line(screen,WHITE,(400,150),(400,650),3)
    line09 = pygame.draw.line(screen,WHITE,(300,150),(300,650),3)
    line10 = pygame.draw.line(screen,WHITE,(200,150),(200,650),3)
    line11 = pygame.draw.line(screen,WHITE,(100,150),(100,650),3)
    course_01 = course.render("math",True,WHITE)
    course_02 = course.render("line",True,WHITE)
    course_03 = course.render("base",True,WHITE)
    course_04 = course.render("physcial",True,WHITE)
    course_05 = course.render("English",True,WHITE)
    course_06 = course.render("lab",True,WHITE)
    course_07 = course.render("physics",True,WHITE)
    screen.blit(course_01,(0,165))
    screen.blit(course_02,(0,265))
    screen.blit(course_03,(0,365))
    screen.blit(course_04,(0,465))
    screen.blit(course_05,(110,165))
    screen.blit(course_06,(110,265))
    screen.blit(course_07,(110,365))
    screen.blit(kbn_load,kbn_location)
    kbn_i = kbn_i + 1
#定时函数


schedule.every().day.at("08:00:00").do(wheather_func)
schedule.every().day.at("08:00:30").do(text_fun)
schedule.every().day.at("08:00:40").do(history)
schedule.every(1).hour.do(time_func)
schedule.every().day.at("07:59:00").do(main_init)
schedule.every(1).hour.do(wheather_func)






while True:
    upgrde_time()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            kbn_x,kbn_y = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_action_get()
            kbn()




    schedule.run_pending()
    pygame.display.update()