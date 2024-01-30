from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.config import Config

from kivy.core.window import Window




class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        button1 = Button(text='Page 1: 6 Images', on_press=self.go_to_page1)
        button2 = Button(text='Page 2: Buttons', on_press=self.go_to_page2)
        button3 = Button(text='Page 3: 2 Images', on_press=self.go_to_page3)

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        self.add_widget(layout)

    def go_to_page1(self, instance):
        Window.size = (680, 700)  # Set window size for Page 1
        self.manager.current = 'page1'

    def go_to_page2(self, instance):
        self.manager.current = 'page2'

    def go_to_page3(self, instance):
        self.manager.current = 'page3'

from kivy.uix.gridlayout import GridLayout

class Page1(Screen):
    def __init__(self, **kwargs):
        super(Page1, self).__init__(**kwargs)
        grid_layout = GridLayout(cols=2, spacing=10, padding=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Add images with fixed size
        for image_path in ["C:\\Users\\amish\\Python\\InkAndInsights\\Images\\1-MaleVsFemaleLine.png",
                           "C:\\Users\\amish\\Python\\InkAndInsights\\Images\\1-Heat.png",
                           "C:\\Users\\amish\\Python\\InkAndInsights\\Images\\1-GenderFemale.png",
                           "C:\\Users\\amish\\Python\\InkAndInsights\\Images\\1-MiddayBar.png"]:
            image = Image(source=image_path, size_hint=(None, None), size=(480, 480))
            grid_layout.add_widget(image)

        # Back button at the top-left corner with formatted appearance
        back_button = Button(text='Back to Main', on_press=self.go_to_main, size_hint=(0.2, 0.2), pos_hint={'x': 0, 'top': 1})
        back_button.background_color = (0.2, 0.6, 1, 1)  # Light blue background color for the button
        back_button.color = (1, 1, 1, 1)  # White text color

        # Add GridLayout and the back button to the screen
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(back_button)
        layout.add_widget(grid_layout)
        

        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'



class Page2(Screen):
    def __init__(self, **kwargs):
        super(Page2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        button1 = Button(text='Page 2.1: 8 Images', on_press=self.go_to_page2_1)
        button2 = Button(text='Page 2.2: 4 Graphs', on_press=self.go_to_page2_2)
        button3 = Button(text='Page 2.3: 4 Graphs', on_press=self.go_to_page2_3)

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        back_button = Button(text='Back to Main', on_press=self.go_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_page2_1(self, instance):
        self.manager.current = 'page2_1'

    def go_to_page2_2(self, instance):
        self.manager.current = 'page2_2'

    def go_to_page2_3(self, instance):
        self.manager.current = 'page2_3'

    def go_to_main(self, instance):
        self.manager.current = 'main'


class Page2_1(Screen):
    def __init__(self, **kwargs):
        super(Page2_1, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        for _ in range(8):
            image = Image(source='your_image_path.jpg')  # Replace with actual image path
            layout.add_widget(image)

        back_button = Button(text='Back to Page 2', on_press=self.go_to_page2)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_page2(self, instance):
        self.manager.current = 'page2'


class Page2_2(Screen):
    def __init__(self, **kwargs):
        
        super(Page2_2, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        '''

        # Add graphs and text labels here
        # ...
    '''
        back_button = Button(text='Back to Page 2', on_press=self.go_to_page2)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_page2(self, instance):
        self.manager.current = 'page2'


class Page2_3(Screen):
    def __init__(self, **kwargs):
        super(Page2_3, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Add graphs and text labels here
        # ...
        D1_button = Button(text='Display 3D graph- Literacy Rates- Male/Female/Overall', on_press=self.D1)
        layout.add_widget(D1_button)
        D2_button = Button(text='Display 3D graph- Female Literacy Vs. Girl Toilet Schools', on_press=self.D2)
        layout.add_widget(D2_button)
        back_button = Button(text='Back to Page 2', on_press=self.go_to_page2)
        layout.add_widget(back_button)

        self.add_widget(layout)
    def D1(self, instance):
        import pandas as pd
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        file_path = "C:\\Users\\amish\Python\\InkAndInsights\\2015_16_Statewise_Elementary.csv"
        data = pd.read_csv(file_path)


        label = 'STATNAME'  
        x = 'MALE_LIT'  
        y = 'FEMALE_LIT'  
        z = 'OVERALL_LI'
        l=data[label]
        x_data = data[x]
        y1_data = data[y]
        y2_data = data[z]

        # Create a 3D bar plot
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, projection='3d')

        # Plot the 3D bars
        x_values = range(len(l))
        y_values = x_data
        z_values = [1] * len(l)
        ax.bar(x_values, y_values, z_values, color='blue', alpha=0.7, label='Male_Lit')

        y_values = y1_data
        z_values = [2] * len(l)
        ax.bar(x_values, y_values, z_values, color='pink', alpha=0.7, label='Female_Lit')

        y_values = y2_data
        z_values = [3] * len(l)
        ax.bar(x_values, y_values, z_values, color='green', alpha=0.7, label='Overall_Lit')

        # Set labels and title
        ax.set_xticks(x_values)
        ax.set_xticklabels(l, rotation=90)
        ax.set_xlabel('States')
        ax.set_ylabel('Literacy rate')
        ax.set_zlabel('Category')
        ax.set_title('3D Bar Plot of Literacy Rates')

        # Add legend
        ax.legend()

        plt.show()
    def D2(self, instance):
        import pandas as pd
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D

        file_path = "C:\\Users\\amish\\Python\\InkAndInsights\\csv2.csv"  
        data = pd.read_csv(file_path)

        y1_column = 'female_literacy_rate'  
        y2_column = '%girls_toilet'  

        y = data[y1_column]
        z = data[y2_column]

        # Create a 3D scatter plot
        fig = plt.figure(figsize=(15, 15))
        ax = fig.add_subplot(111, projection='3d')

        # Scatter plot using the index as x-axis
        scatter = ax.scatter(data.index, y, z, c='blue', marker='o')

        # Set labels and title
        ax.set_ylabel('% Female Literacy')
        ax.set_zlabel('% Girls in Schools')
        ax.set_title('3D Scatter Plot: Index vs % Female Literacy vs % Girls in Schools')

        # Set state names as labels on the x-axis
        ax.set_xticks(data.index)
        ax.set_xticklabels(data['statname'], rotation=90)

        # Show plot
        plt.show()        
    def go_to_page2(self, instance):
        self.manager.current = 'page2'


class Page3(Screen):
    def __init__(self, **kwargs):
        super(Page3, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        for _ in range(2):
            image = Image(source='your_image_path.jpg')  # Replace with actual image path
            layout.add_widget(image)

        back_button = Button(text='Back to Main', on_press=self.go_to_main)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Page1(name='page1'))
        sm.add_widget(Page2(name='page2'))
        sm.add_widget(Page2_1(name='page2_1'))
        sm.add_widget(Page2_2(name='page2_2'))
        sm.add_widget(Page2_3(name='page2_3'))
        sm.add_widget(Page3(name='page3'))

        return sm

if __name__ == '__main__':
    MyApp().run()
