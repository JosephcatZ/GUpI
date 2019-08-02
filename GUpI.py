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
        def test():
            print('test')
        self.Function = lambda: Function()
        self.X=X
        self.Y=Y
        self.Xsize=Xsize
        self.Ysize=Ysize
        self.Text=Text
        self.Color=Color
        self.r=R
        self.count=0
        GUI.Buttons.append(self)
    def __call__():
        run(self.Function)
class Dropdown:
    def __init__(self, X, Y, Width, Height, Values, Gui):
        self.X = X
        self.Y = Y
        self.W = Width
        self.H = Height
        self.Selected = Values[0]
        self.V = Values
        self.Down=False
        self.index=0
        Gui.Dropdowns.append(self)
class Textfield:
    def __init__(self, X,Y, Width, Height,Len, GUI):
        self.X = X
        self.Y = Y
        self.W = Width
        self.H = Height
        self.Value='test'
        self.Focus=False
        self.Len=Len
        self.count=0
        GUI.TextFields.append(self)
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
    text(gui.Title, X+gui.Xsize/2, gui.Y+gui.Xsize/len(gui.Title))
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
        fill(i.Color)
        if r!=None:
            rect(X+i.X,X+i.Y,X+i.Xsize,X+i.Ysize,i.r)
        else:
            rect(X+i.X,X+i.Y,X+i.Xsize,X+i.Ysize)
        textAlign(CENTER)
        textSize(i.Ysize/2)
        fill(0)
        text(i.Text,X+i.X+(i.Xsize/2),Y+i.Y+7*(i.Ysize/8))
        if i.count == 0:
            if (X+i.X <= mouseX <= X+i.Xsize+i.X) and (Y+i.Y <= mouseY <= Y+i.Ysize+i.Y):
                if mousePressed:
                    i.Function()
                    i.count = 100
        else:
            i.count = i.count - 1
    for i in gui.TextFields:
        fill(255)
        strokeWeight(2)
        stroke(0)
        rect(X+i.X,Y+i.Y,i.W,i.H)
        if mousePressed:
            if (X+i.X <= mouseX <= X+i.W+i.X) and (Y+i.Y <= mouseY <= Y+i.H+i.Y):
                i.Focus=True
            else:
                i.Focus=False
        textAlign(LEFT)
        fill(0)
        textSize(i.H/2)
        if len(i.Value) <= i.Len:
            val = i.Value
        else:
            val = i.Value[len(i.Value)-i.Len:len(i.Value)-i.Len+5]
        text(val,X+i.X+5,Y+i.Y+3*(i.H/4))
        if i.count==0:
            if keyPressed:
                if i.Focus:
                    if key==DELETE or key==BACKSPACE:
                        i.Value = i.Value[0:len(i.Value)-1]
                    elif key != CODED:
                        i.Value = i.Value+str(key)
                    i.count = 100
        else:
            if keyPressed:
                i.count = i.count - 1
            else:
                i.count=0
                
    for i in gui.Dropdowns:
        fill(255)
        strokeWeight(2)
        stroke(0)
        rect(X+i.X,Y+i.Y,i.W,i.H)
        fill(127)
        rect(i.W+X+i.X-i.H,Y+i.Y,i.H,i.H)
        fill(0)
        textSize(12)
        text(i.Selected,X+i.X+12,Y+i.Y+12)
        k=0
        if mousePressed:
            
            if(X+i.X<=mouseX<=X+i.X+i.W and Y+i.Y+(k*i.H)<=mouseY<=Y+i.Y+i.H+(k*i.H)):
                i.Down=True
            else:
                if not(X+i.X<=mouseX<=X+i.X+i.W and Y+i.Y+(k*i.H)<=mouseY<=Y+i.Y+i.H+((len(i.V)+1)*i.H)):
                    i.Down=False
        if i.Down:
            for J in i.V:
                k=k+1
                fill(255)
                strokeWeight(2)
                stroke(0)
                rect(X+i.X,Y+i.Y+i.H*k,i.W,i.H)
                fill(0)
                textSize(12)
                text(J,X+i.X+12,i.Y+i.H*k+12)
                
                if(X+i.X<=mouseX<=X+i.X+i.W and Y+i.Y+(k*i.H)<=mouseY<=Y+i.Y+i.H+(k*i.H) and mousePressed):
                    i.Selected=J
            
        
def H2x(x):
    return(hex(x)[-2:])
def rgb(r,g,b):
    return('#'+H2x(r)+H2x(g)+H2x(b))
