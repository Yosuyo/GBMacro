import pyautogui as pg
import random
import wx
import command

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
        bottun5 = wx.Button(self,5,label="QUIT",size=CalSize(5),pos=CalPos(5,5))
        #ボタンイベント
        def MainButtonEvent(event):
            if event.GetId() == 1:
                parent.DestroyChildren()
                panel = Daily(parent)
            elif event.GetId() == 2:
                parent.DestroyChildren()
                panel = Event1(parent)
            elif event.GetId() == 3:
                pass
            elif event.GetId() == 4:
                pass
            elif event.GetId() == 5:
                parent.Close()
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
                command.daily1()
            elif event.GetId() == 2:
                command.daily2()
            elif event.GetId() == 3:
                command.daily3()
            elif event.GetId() == 4:
                command.daily4()
            elif event.GetId() == 5:
                command.daily5()
            elif event.GetId() == 6:
                command.daily6()
            elif event.GetId() == 7:
                command.daily7()
            elif event.GetId() == 8:
                parent.DestroyChildren()
                panel = Main(parent)
        #設定
        self.Bind(wx.EVT_BUTTON,DailyButtonEvent)
    
#イベント1画面
class Event1(wx.Panel):
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
        def CalSize(number):
            xsize = (x-(margin*(number+1)))/number
            ysize = y-(margin*2)
            return xsize,ysize
        #レイアウト
        self.SetBackgroundColour((255,255,255))        
        bottun1 = wx.Button(self,1,label="A",size=CalSize(5),pos=CalPos(1,5))
        bottun2 = wx.Button(self,2,label="B",size=CalSize(5),pos=CalPos(2,5))
        bottun3 = wx.Button(self,3,label="C",size=CalSize(5),pos=CalPos(3,5))
        bottun4 = wx.Button(self,4,label="D",size=CalSize(5),pos=CalPos(4,5))
        bottun5 = wx.Button(self,5,label="Back",size=CalSize(5),pos=CalPos(5,5))
        #ボタンイベント
        def DailyButtonEvent(event):
            if event.GetId() == 1:
                command.event1()
            elif event.GetId() == 2:
                command.event2()
            elif event.GetId() == 3:
                command.event3()
            elif event.GetId() == 4:
                command.event4()
            elif event.GetId() == 5:
                parent.DestroyChildren()
                panel = Main(parent)
        #設定
        self.Bind(wx.EVT_BUTTON,DailyButtonEvent)



app = wx.App(False)
frame = Frame(None,"macro")
frame.Show(True)
app.MainLoop()