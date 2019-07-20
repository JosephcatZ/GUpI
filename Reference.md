<h1>How to use gui's</h1>

the gui's in GUpI are very simple to use in understand.<br>
there is just one thing to keep in mind:<br>
  __X and Y in everything *BUT* the GUI it's self are relative to the gui__
  
  <h2>initializing your gui</h2>
GUI's in GUpI are __OBJECTS__ assigned to variables, as are everything<br>
If you want to get any data from anything, you'll need to access data from it.<br>
<br>
this is the code you need for a GUI
```Python
GUI_NAME = GUpI.GUI(X,Y,X size,Y size,Title,Color,Radius(optional))
```
<br>
<br>
<h2>having your gui drawn</h2>
it is very simple to draw your gui, and it is one command,
```python
GUpI.run(GUI_NAME)
```
<br>
<br>
<br>
<h1>Code Refrence</h1>
```python
GUpI.Text(Text,Color,Size,Align,Gui,X,Y,X2(wraping boundary(op)), Y2(wraping boundary(op)))
```
the Text class allows you to put text in the gui<br>
it functions identicaly to a text command
<br>
<br>
```python
GUpI.Submenu(X, Y, Xsize, Ysize, Title, Color,gui,r=None)
```
A submenu functions identicaly to a GUI, but is inside the gui<br>
these can be used for many reasons, but the main way is to group simmilar Items.
