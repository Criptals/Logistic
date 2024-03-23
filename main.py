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
    '''
        Класс, описывающий работу экрана
    '''
    path_list = []

    def open(self, path, filename):
        '''
            Функция для овыбора файла и добаления его в список выбранных
        :param path: путь к файлу
        :param filename: имя файла
        '''
        if filename != []:
            if filename[0] not in self.path_list:
                self.path_list.append(filename[0])
                items = BaseListItem(text=filename[0], text_color=(100, 100, 100, 1), size_hint=(1, 0.005))
                self.ids["list"].add_widget(items)
                print(self.path_list)

    def selected(self, filename):
        pass

    def generate_files(self):
        '''
            Функция для начала генерации таблиц
        '''
        create_general_file(self.path_list, gen_name=self.ids.t1.text, avg_name=self.ids.t2.text)

    def delete_selected_files(self):
        '''
            Функция для очистки списка выбранных файлов
        '''
        while len(self.path_list) != 0:
            self.path_list.pop()
        self.ids["list"].clear_widgets()


class MyApp(MDApp):
    '''
        Класс для запуска программы
    '''
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    app = MyApp()
    app.run()