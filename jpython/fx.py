
import sys
from javafx.application import Application
from javafx.scene import Scene
from javafx.scene.layout import FlowPane, GridPane
from javafx.stage import Stage
import javafx.scene.control

from javafx.geometry import Pos

class HelloApplication(Application):
    
    
    def start(self, stage):
        root = GridPane()
        l = javafx.scene.control.Label("Talha")
        b = javafx.scene.control.Button("Press Me!")
        root.setAlignment(Pos.CENTER)
        root.addRow(0,l)
        root.addRow(1,b)
        scene = Scene( root, 640, 480 )
        stage.setScene( scene )
        stage.setTitle( "Hello, World" )
        stage.show()
        b.setOnAction (self.buttonPressed)
    def buttonPressed(self,ae):
       print('Button was pressed.')
if __name__ == "__main__":
    Application.launch(HelloApplication().class, sys.argv[1:])
   
