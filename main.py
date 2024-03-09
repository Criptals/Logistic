from kivy.config import Config
from kivymd.uix.list import BaseListItem
from kivymd.uix.screen import MDScreen

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivymd.app import MDApp
from kivy.core.text import Label
from kivy.lang import Builder
from general_file import create_general_file


Builder.load_file('mywidget.kv')
# ScrollView:
#         do_scroll: True
#         pos_hint: {'center_x': 0.5, 'center_y': 0.1}
#         MDList:
#             id: list
#             pos_hint: {'center_x': 0.5, 'center_y': 0.1}


class MyWidget(MDScreen):
    path_list = []

    def open(self, path, filename):
        if filename != []:
            if filename[0] not in self.path_list:
                self.path_list.append(filename[0])
                lbl = Label(text=filename[0], color=[.1, .1, .1, 1])
                items = BaseListItem(text=filename[0], text_color=(100, 100, 100, 1), size_hint=(1, 0.005))
                self.ids["list"].add_widget(items)
                print(self.path_list)

    def selected(self, filename):
        pass

    def generate_files(self):
        create_general_file(self.path_list)

    def delete_selected_files(self):
        while len(self.path_list) != 0:
            self.path_list.pop()
        self.ids["list"].clear_widgets()


class MyApp(MDApp):
    def build(self):
        return MyWidget()


# class MainApp(App):
#     path_list = []
#     Window.clearcolor = (10, 10, 10, 10)
#     main_layout = BoxLayout(orientation="vertical")
#
#     def build(self):
#         return self.layout1()
#
#     def on_press_button1(self, instance):
#         text_input = TextInput(
#             multiline=False, readonly=False, halign="center", font_size=15, size_hint=(1, .03),
#         )
#         self.path_list.append(text_input)
#         self.main_layout.add_widget(text_input)
#
#     def on_press_button2(self, instance):
#         lst = []
#         for i in range(len(self.path_list)):
#             lst.append(self.path_list[i].text[1:-1:1])
#             self.path_list[i].background_color = (10, 0, 0, 0)
#         print(check_files(lst))
#
#     def on_press_button3(self, instance):
#         self.main_layout.clear_widgets()
#         self.layout1()
#
#     def layout1(self):
#         h_layout = BoxLayout(padding=0, orientation='horizontal', size_hint=(1, .2), )
#
#         button1 = Button(text='Добавить путь к файлу',
#                          size_hint=(.05, .08),
#                          pos_hint={'center_x': 0.9, 'center_y': 0.95}, )
#         button1.bind(on_press=self.on_press_button1)
#
#         h_layout.add_widget(button1)
#         button2 = Button(text='Сгенерировать таблицы',
#                          size_hint=(.05, .08),
#                          pos_hint={'center_x': 0.6, 'center_y': 0.95})
#         button2.bind(on_press=self.on_press_button2)
#         h_layout.add_widget(button2)
#         button3 = Button(text='Очистить экран',
#                          size_hint=(.05, .08),
#                          pos_hint={'center_x': 0.93, 'center_y': 0.95})
#         button3.bind(on_press=self.on_press_button3)
#         h_layout.add_widget(button3)
#         self.main_layout.add_widget(h_layout)
#         text_input = TextInput(
#             multiline=False, readonly=False, halign="center", font_size=15, size_hint=(1, .03),
#         )
#         self.path_list.append(text_input)
#         self.main_layout.add_widget(text_input)
#         self.main_layout.add_widget(MyWidget)
#         return self.main_layout


if __name__ == '__main__':
    app = MyApp()
    app.run()