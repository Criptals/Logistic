from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    path_list = []
    Window.clearcolor = (10, 10, 10, 10)
    main_layout = BoxLayout(orientation="vertical")

    def build(self):
        return self.layout1()


    def on_press_button1(self, instance):
        text_input = TextInput(
            multiline=False, readonly=False, halign="center", font_size=15, size_hint=(1, .03),
        )
        self.path_list.append(text_input)
        self.main_layout.add_widget(text_input)


    def on_press_button2(self, instance):

        for i in range(len(self.path_list)):
            print(self.path_list[i].text)


    def on_press_button3(self, instance):
        self.main_layout.clear_widgets()
        self.layout1()


    def layout1(self):
        h_layout = BoxLayout(padding=0, orientation='horizontal', size_hint=(1, .2), )

        button1 = Button(text='Добавить путь к файлу',
                         size_hint=(.05, .08),
                         pos_hint={'center_x': 0.9, 'center_y': 0.95}, )
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
        self.main_layout.add_widget(h_layout)
        text_input = TextInput(
            multiline=False, readonly=False, halign="center", font_size=15, size_hint=(1, .03),
        )
        self.path_list.append(text_input)
        self.main_layout.add_widget(text_input)
        return self.main_layout


if __name__ == '__main__':
    app = MainApp()
    app.run()