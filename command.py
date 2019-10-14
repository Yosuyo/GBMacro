import pyautogui as pg
import random
import time

def r():
    a = 5 * random.random()
    return a
def right():
    pg.moveTo(350+r(),755+r())
    pg.dragRel(-150,0,0.1,button="left")
    time.sleep(0.1)
def left():
    pg.moveTo(250+r(),755+r())
    pg.dragRel(150,0,0.1,button="left")
    time.sleep(0.1)
def ch1():
    pg.click(50+r(),620+r(),2)
def ch2():
    pg.click(130+r(),620+r(),2)
def ch3():
    pg.click(210+r(),620+r(),2)
def ch4():
    pg.click(290+r(),620+r(),2)
def skill1():
    pg.click(155+r(),675+r(),2)
def skill2():
    pg.click(242+r(),675+r(),2)
def skill3():
    pg.click(325+r(),675+r(),2)
def skill4():
    pg.click(409+r(),675+r(),2)
def back():
    pg.click(50+r(),505+r(),2)
def auto():
    pg.click(53+r(),533)
def attack():
    pg.click(370+r(),500+r())
def summonKatsuo():
    pg.click(385+r(),600+r(),2)
    time.sleep(0.2)
    pg.click(50+r(),600+r())
    time.sleep(0.1)
    pg.click(350+r(),707+r())
def summon3():
    pg.click(385+r(),600+r(),2)
    time.sleep(0.3)
    pg.click(200+r(),600+r())
    time.sleep(0.1)
    pg.click(350+r(),643+r())

#日課
def daily1():
    pos = pg.position()
    ch1()
    skill4()
    skill2()
    skill1()
    skill3()
    attack()
    auto()
    pg.moveTo(pos)
def daily2():
    pos = pg.position()
    ch1()
    skill2()
    skill3()
    skill4()
    right()
    skill2()
    right()
    right()
    skill3()
    attack()
    auto()
    pg.moveTo(pos)
def daily3():
    pos = pg.position()
    ch1()
    skill3()
    skill4()
    back()
    time.sleep(0.5)
    summonKatsuo()
    attack()
    auto()
    pg.moveTo(pos)
def daily4():
    pos = pg.position()
    ch1()
    skill2()
    skill3()
    skill4()
    back()
    time.sleep(0.5)
    summon3()
    attack()
    auto()
    pg.moveTo(pos)
def daily5():
    pos = pg.position()
    ch1()
    skill2()
    skill3()
    skill4()
    left()
    skill2()
    attack()
    auto()
    pg.moveTo(pos)
def daily6():
    pos = pg.position()
    ch1()
    skill2()
    skill3()
    skill4()
    right()
    skill1()
    right()
    skill1()
    right()
    skill2()
    attack()
    auto()
    pg.moveTo(pos)
def daily7():
    pos = pg.position()
    ch1()
    skill2()
    skill3()
    skill4()
    right()
    skill1()
    right()
    right()
    skill1()
    skill2()
    skill3()
    attack()
    auto()
    pg.moveTo(pos)

def event1():
    pos = pg.position()
    ch1()
    skill2()
    skill3()
    skill4()
    right()
    skill1()
    right()
    right()
    skill1()
    skill2()
    skill3()
    attack()
    auto()
    pg.moveTo(pos)

def event2():
    pos = pg.position()
    ch1()
    skill1()
    skill2()
    skill3()
    skill4()
    right()
    skill1()
    right()
    right()
    skill4()
    attack()
    auto()
    pg.moveTo(pos)

def event3():
    pos = pg.position()
    summonKatsuo()
    attack()
    auto()
    pg.moveTo(pos)

def event4():
    pos = pg.position()
    ch1()
    skill3()
    attack()
    auto()
    pg.moveTo(pos)