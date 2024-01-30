from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class ScrollableBoxLayout(ScrollView):
    def __init__(self, **kwargs):
        super(ScrollableBoxLayout, self).__init__(**kwargs)

        # Create a box layout to hold the content
        box_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)

        # Add images with larger sizes
        for _ in range(10):
            image = Image(source='your_image_path.jpg', size_hint_y=None, height=300)
            box_layout.add_widget(image)

        # Set the height of the box layout to accommodate its children
        box_layout.bind(minimum_height=box_layout.setter('height'))

        # Add the box layout to the scroll view
        self.add_widget(box_layout)

class MyApp(App):
    def build(self):
        return ScrollableBoxLayout()

if __name__ == '__main__':
    MyApp().run()
