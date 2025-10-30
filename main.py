from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        
        label = Label(
            text='ПРИЛОЖЕНИЕ УСПЕШНО СОБРАНО!',
            font_size=24
        )
        
        btn = Button(
            text='РАБОТАЕТ!',
            size_hint_y=0.3,
            background_color=(0, 1, 0, 1)
        )
        
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    MyApp().run()
