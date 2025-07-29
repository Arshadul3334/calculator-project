from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from simple_calc import add , subtraction , multiply , division , onlynumbers
from kivy.core.window import Window










class CalculatorLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 20
        self.spacing = 20
        self.cols = 1
        self.resultlabel = Label(text="Result will appear here!",color = (0.25, 0.88, 0.82, 1),font_size = 20 , halign = 'center')     
        self.number1 = TextInput(hint_text="First number : ", multiline = False , background_color = "black",foreground_color=(1, 1, 1, 1),font_size = 20)
        self.number2 = TextInput(hint_text='Second number : ',multiline = False , background_color = "black",foreground_color=(1, 1, 1, 1),font_size = 20)
        self.button1 = Button(text="Add",)
        self.button2 = Button(text="Substract",)
        self.button3 = Button(text="Multiply",)                
        self.button4 = Button(text="Divide",)
        self.theme = Button(text="Theme",)
        button_layout = BoxLayout(spacing=10 , padding = 10)     
        self.button1.bind(on_press=self.addition ,) 
        self.button2.bind(on_press=self.substract)         
        self.button3.bind(on_press=self.multiplication)         
        self.button4.bind(on_press=self.divide)
        self.number2.bind(on_text_validate=self.addition)
        self.number1.bind(on_text_validate=self.addition)  
        self.theme.bind(on_press = self.toggletheme)  
        self.add_widget(self.resultlabel)        
        self.add_widget(self.number1)
        self.add_widget(self.number2,)
        self.add_widget(button_layout)
        self.add_widget(self.theme)
        button_layout.add_widget(self.button1)
        button_layout.add_widget(self.button2)
        button_layout.add_widget(self.button3)
        button_layout.add_widget(self.button4)
        self.dark = True     
    def clear_input(self):
        self.number1.text = ""
        self.number2.text = ""
    def addition(self , instance):
        x = self.number1.text
        y = self.number2.text
        if onlynumbers(x) and onlynumbers(y):
            x = float(x)
            y = float(y)
            result = add(x,y)
            self.resultlabel.text = f"Result : {result}"
            self.clear_input()
        else:
            self.resultlabel.text = f"Pls enter numbers only"
    def substract(self , instance):
        x = self.number1.text
        y = self.number2.text
        if onlynumbers(x) and onlynumbers(y):
            x = float(x)
            y = float(y)
            result = subtraction(x,y)
            self.resultlabel.text = f"Result : {result}"
            self.clear_input()
        else:
            self.resultlabel.text = f"Pls enter numbers only"
    def multiplication(self , instance):
        x = self.number1.text
        y = self.number2.text
        if onlynumbers(x) and onlynumbers(y):
            x = float(x)
            y = float(y)
            result = multiply(x,y)
            self.resultlabel.text = f"Result : {result}"
            self.clear_input()
        else:
            self.resultlabel.text = f"Pls enter numbers only"   
    def divide(self , instance):
        x = self.number1.text
        y = self.number2.text
        if onlynumbers(x) and onlynumbers(y):
            x = float(x)
            y = float(y)
            result = division(x,y)
            self.resultlabel.text = f"Result : {result}"
            self.clear_input()
        else:
            self.resultlabel.text = f"Pls enter numbers only"
    def DarkMode(self):
        self.resultlabel.color = (0.25, 0.88, 0.82, 1)
        self.number1.background_color = (0, 0, 0, 1)
        self.number1.foreground_color = (1, 1, 1, 1)
        self.number2.background_color = (0, 0, 0, 1)
        self.number2.foreground_color = (1, 1, 1, 1)
    def LightMode(self):
        self.resultlabel.color = (1, 1, 1, 1)
        self.number1.background_color =  (1, 1, 1, 1)
        self.number1.foreground_color = (0, 0, 0, 1)
        self.number2.background_color =  (1, 1, 1, 1)
        self.number2.foreground_color = (0, 0, 0, 1)
    def toggletheme(self ,instance):
        if self.dark:
            self.LightMode()
            self.dark = False
        else:
            self.DarkMode()
            self.dark=True




class Calculator(App):
    icon = 'calculator.ico' 
    def build(self):
        Window.icon = self.icon  
        self.title = "Calculator"
        return CalculatorLayout()
    









if __name__== "__main__":
    Calculator().run()
