from abstract_factory import UIAbstractFactory, Button, TextBox

class DarkButton(Button):
  def paint(self):
    print("Dark button")

class DarkTextBox(TextBox):
  def paint(self):
    print("Dark text box")

class LightButton(Button):
  def paint(self):
    print("Light button")

class LightTextBox(TextBox):
  def paint(self):
    print("Light text box")

class DarkUIFactory(UIABstractFactory):
  def create_button(self):
    return DarkButton()

  def create_textbox(self):
    return DarkTextBox()

class LightUIFactory(UIABstractFactory):
  def create_button(self):
    return LightButton()

  def create_textbox(self):
    return LightTextBox()
