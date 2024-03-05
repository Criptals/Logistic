from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    Window.clearcolor = (10, 10, 10, 10)
    main_layout = BoxLayout(orientation="vertical")

    def build(self):

        h_layout = BoxLayout(padding=0, orientation='horizontal')

        button1 = Button(text='Добавить путь к файлу',
                        size_hint=(.05, .08),
                        pos_hint={'center_x': 0.9, 'center_y': 0.95},)
        button1.bind(on_press=self.on_press_button1)

        h_layout.add_widget(button1)
        button2 = Button(text='Сгенерировать таблицы',
                        size_hint=(.05, .08),
                        pos_hint={'center_x': 0.6, 'center_y': 0.95})
        button2.bind(on_press=self.on_press_button2)
        h_layout.add_widget(button2)
        button3 = Button(text='Очистить экран',
                        size_hint=(.05, .08),
                        pos_hint={'center_x': 0.93, 'center_y': 0.95})
        button3.bind(on_press=self.on_press_button3)
        h_layout.add_widget(button3)
        main_layout.add_widget(h_layout)

        main_layout.add_widget(TextInput(
            multiline=False, readonly=False, halign="center", font_size=25, size_hint=(1, .1),
        ))

        return main_layout


    def on_press_button1(self, instance):
        main_layout = BoxLayout(orientation="vertical")

        self.col = TextInput(
            multiline=False, readonly=False, halign="center", font_size=25, size_hint=(1, .1),
        )
        main_layout.add_widget(self.col)


    def on_press_button2(self, instance):
        print('Вы нажали на кнопку 2!')


    def on_press_button3(self, instance):
        print('Вы нажали на кнопку 3!')



if __name__ == '__main__':
    app = MainApp()
    app.run()