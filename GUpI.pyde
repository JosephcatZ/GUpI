import types
class GUI:
            def __init__(self, X, Y, Xsize, Ysize, Title, Color,r=None):
                self.X = X
                self.Y = Y
                self.Xsize = Xsize
                self.Title = Title
                self.Ysize = Ysize
                self.Color = Color
                self.Dropdowns = []
                self.Buttons = []
                self.TextFields =[]
                self.texts = []
                self.Submenus =[]
                self.r=r
class Text:
    def __init__(self,Text,Color,Size,Align,Gui,X,Y,X2 = None, Y2 = None):
        self.Text=Text
        self.Color=Color
        self.Size=Size
        self.Align=Align
        self.X = X
        self.Y = Y
        self.X2 = X2
        self.Y2 = Y2
        Gui.texts.append(self)
class Submenu:
            def __init__(self, X, Y, Xsize, Ysize, Title, Color,gui,r=None):
                self.X = X
                self.Y = Y
                self.Xsize = Xsize
                self.Title = Title
                self.Ysize = Ysize
                self.Color = Color
                self.Dropdowns = []
                self.Buttons = []
                self.TextFields =[]
                self.texts = []
                self.Submenus =[]
                self.r=r
                gui.Subenus.append(self)
class Button:
    def __init__(self, X, Y, Xsize, Ysize, Text, Color, Function, GUI,R=None):
        self.Function = types.MethodType(Function, self)
        self.X=X
        self.Y=Y
        self.Xsize=Xsize
        self.Ysize=Ysize
        self.Text=Text
        self.Color=Color
        self.r=R
        self.count=0
        GUI.Buttons.append(self)
        
def run(gui):
    X=gui.X
    Y=gui.Y
    r= gui.r
    fill(gui.Color)
    if r!=None:
        rect(gui.X, gui.Y, gui.Xsize, gui.Ysize,r)
    else:
        rect(gui.X, gui.Y, gui.Xsize, gui.Ysize)
    textSize(gui.Xsize/len(gui.Title))
    fill(0)
    textAlign(CENTER)
    text(gui.Title, gui.Xsize/2, gui.Y+gui.Xsize/len(gui.Title))
    for i in gui.Submenus:
        run(i)
    for i in gui.texts:
        fill(i.Color)
        textSize(i.Size)
        textAlign(i.Align)
        if i.Y2 != None:
            text(i.Text,X+i.X,Y+i.Y,X+i.X2,Y+i.Y2)
        else:
            text(i.Text,X+i.X,Y+i.Y)
    for i in gui.Buttons:
        if r!=None:
            rect(X+i.X,X+i.Y,X+i.Xsize,X+i.Ysize,i.r)
        else:
            rect(X+i.X,X+i.Y,X+i.Xsize,X+i.Ysize)
        if i.count == 0:
            if (X+i.X <= mouseX <= X+i.Xsize+i.X) and (Y+i.Y <= mouseY <= Y+i.Ysize+i.Y):
                if mousePressed:
                    i.Function()
                    i.count = 10
        else:
            i.count = i.count - 1
def H2x(x):
    return(hex(x)[-2:])
def rgb(r,g,b):
    return('#'+H2x(r)+H2x(g)+H2x(b))
