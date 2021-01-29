import sys
from java.awt import Window
from javax.swing import JFrame, WindowConstants
from javax.swing import JButton,JLabel
from java.awt import BorderLayout
def buttonPressed(e):
    l.setText("Button Pressed")

border = BorderLayout()
f = JFrame()
l = JLabel("This is a label")
b = JButton("Press Me!")
f.title = "Hello AWT"
f.setLayout(border)
f.contentPane.add(b,BorderLayout.SOUTH)
f.contentPane.add(l,BorderLayout.NORTH)
f.setSize(400,400)
b.actionPerformed = buttonPressed
f.visible = True
f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)


    
