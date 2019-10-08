import pyautogui as pg
import random
import wx

class command():
    def r(self):
        a = 5 * random.random()
        return a
    def ch1(self):
        pg.click(50+self.r(),620+self.r(),2)
    def ch2(self):
        pg.click(130+self.r(),620+self.r(),2)
    def ch3(self):
        pg.click(210+self.r(),620+self.r(),2)
    def ch4(self):
        pg.click(290+self.r(),620+self.r(),2)
    def skill1(self):
        pg.click(155+self.r(),675+self.r(),2)
    def skill2(self):
        pg.click(242+self.r(),675+self.r(),2)
    def skill3(self):
        pg.click(325+self.r(),675+self.r(),2)
    def skill4(self):
        pg.click(409+self.r(),675+self.r(),2)
    def back(self):
        pg.click(50+self.r(),505+self.r(),2)
    def auto(self):
        pg.click(53+self.r(),533)
    def attack(self):
        pg.click(370+self.r(),500+self.r())

    def event1(self):
        self.ch1()
        self.skill2()
        self.skill3()
        self.attack()
        self.auto()

#メイン画面
class Frame(wx.MiniFrame):
    def __init__(self,parent,title):
        wx.MiniFrame.__init__(
            self,
            parent,
            id = -1,
            title = title,
            size = (482,75),
            pos = wx.Point(0,910),
            style = wx.STAY_ON_TOP
            )
        panel = Main(self)
#メイン画面
class Main(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent,id=0,pos=(0,0),size=(482,75))
        self.parent = parent
        #レイアウト導出関数
        x = 481
        y = 73
        margin = 3
        def CalPos(id,number):
            xp = x-margin
            xp = (xp/number)*(id-1)+margin
            yp = margin
            return xp,yp
        def CalSize(number):
            xsize = (x-(margin*(number+1)))/number
            ysize = y-(margin*2)
            return xsize,ysize
        #レイアウト
        self.SetBackgroundColour((255,255,255))        
        bottun1 = wx.Button(self,1,label="日課",size=CalSize(5),pos=CalPos(1,5))
        bottun2 = wx.Button(self,2,label="イベント1",size=CalSize(5),pos=CalPos(2,5))
        bottun3 = wx.Button(self,3,label="None",size=CalSize(5),pos=CalPos(3,5))
        bottun4 = wx.Button(self,4,label="None",size=CalSize(5),pos=CalPos(4,5))
        bottun5 = wx.Button(self,5,label="終了",size=CalSize(5),pos=CalPos(5,5))
        #ボタンイベント
        def MainButtonEvent(event):
            if event.GetId() == 1:
                self.DestroyChildren()
                panel = Daily(self)
            elif event.GetId() == 2:
                pass
            elif event.GetId() == 3:
                pass
            elif event.GetId() == 4:
                pass
            elif event.GetId() == 5:
                frame.Close()
        #設定
        bottun3.Disable()
        bottun4.Disable()
        self.Bind(wx.EVT_BUTTON,MainButtonEvent)

#日課画面
class Daily(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent,id=1,pos=(0,0),size=(482,75))
        self.parent = parent
        #レイアウト導出関数
        x = 481
        y = 73
        margin = 3
        def CalPos(id,number):
            xp = x-margin
            xp = (xp/number)*(id-1)+margin
            yp = margin
            return xp,yp
        def CalPos2(id,number):
            xy = CalPos(id,number)
            xp = xy[0]
            yp = (y-margin)/2+margin
            return xp,yp
        def CalSize(number):
            xsize = (x-(margin*(number+1)))/number
            ysize = y-(margin*2)
            return xsize,ysize
        def CalSize2(number):
            xy = CalSize(number)
            xsize = xy[0]
            ysize = (xy[1]-margin)/2
            return xsize,ysize
        #レイアウト
        self.SetBackgroundColour((255,255,255))        
        bottun1 = wx.Button(self,1,label="島Hard",size=CalSize(5),pos=CalPos(1,5))
        bottun2 = wx.Button(self,2,label="ティアマト",size=CalSize2(5),pos=CalPos(2,5))
        bottun3 = wx.Button(self,3,label="コロッサス",size=CalSize2(5),pos=CalPos(3,5))
        bottun4 = wx.Button(self,4,label="リヴァイアサン",size=CalSize2(5),pos=CalPos(4,5))
        bottun5 = wx.Button(self,5,label="ユグドラシル",size=CalSize2(5),pos=CalPos2(2,5))
        bottun6 = wx.Button(self,6,label="シュヴァリエ",size=CalSize2(5),pos=CalPos2(3,5))
        bottun7 = wx.Button(self,7,label="セレスト",size=CalSize2(5),pos=CalPos2(4,5))
        bottun8 = wx.Button(self,8,label="Back",size=CalSize(5),pos=CalPos(5,5))
        #ボタンイベント
        def DailyButtonEvent(event):
            if event.GetId() == 1:
                pass
            elif event.GetId() == 2:
                pass
            elif event.GetId() == 3:
                pass
            elif event.GetId() == 4:
                pass
            elif event.GetId() == 8:
                parent.DestroyChildren()
                panel = Main(parent)
        #設定
        self.Bind(wx.EVT_BUTTON,DailyButtonEvent)



app = wx.App(False)
frame = Frame(None,"macro")
frame.Show(True)
app.MainLoop()