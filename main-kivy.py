from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):  # Keyword arguments leta = 'a'
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.boxLayout.add_widget(Tarefa(text=tarefa))

class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class MainApp(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Buscar filho', 'Fazer trabalho','Fazer compras', 'Buscar filho', 'Fazer trabalho'])

MainApp.title='Aulas de Kivy'
MainApp().run()
