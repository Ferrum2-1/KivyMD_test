# сначала импортируем стандарстные библиотеки


# импортируем сторонние
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class ASPC(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = "50"
        return Builder.load_string(
        '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'ASPC mobile'
        md_bg_color: .7, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
    MDBottomNavigation:
        panel_color: .7, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Новости'
            icon: 'newspaper-variant-outline'

            MDLabel:
                text: 'Новости'
                halign: 'center' '''

        # Тут должен быть API Facebook для вывода ленты instagram    
        '''
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Рассписание'
            icon: 'view-list-outline' '''

            # Тут я хз как выводить картинки в jpg на весь экран
            '''
            MDLabel:
                text: 'Тут должно быть рассписание'
                halign: 'center'
            '''
            
        )
            
ASPC().run()


