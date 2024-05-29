from concrete_component import PlainText
from concrete_decorator import HTMLDecorator

plain_text = PlainText('Hola mundo!')
print(" Texto sin decorar: ", plaint_text.render())

html_text = HTMLDecorator(plain_text.render())
print("Text decorado: ", html_text.render())
