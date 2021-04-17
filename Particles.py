from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
import random



kv="""
<Particle>:
    canvas.after:
        Color:
            rgb: (root.visibility, root.visibility, root.visibility)
        Ellipse:
            pos: root.pos
            size: root.size

"""

Builder.load_string(kv)

class Particle(Widget):
    visibility=NumericProperty(1)
    
    def init(self):
        self.size_hint = None, None
        a = random.randint(15, 25)
        self.size=(a, a)
        self.v = [random.random()*100-50, random.random()*100-50]
        self.g = -30
        
    def fade(self, dt):
        self.visibility -= dt/10
        self.height -= 4*dt/3
        self.width -= 4*dt/3
        
        self.x += self.v[0]*dt
        self.y += self.v[1]*dt
        self.v[1] += self.g*dt
        
        if self.y < 0-self.height:
            self.parent.remove_widget(self)
        

class Label2(Label):
    visibility=1
    def fade(self, dt):
        pass 

    
class Particles(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_pos = [Window.width/2, Window.height/2]
        self.label = Label2(text="0")
        self.add_widget(self.label)
        
        Clock.schedule_interval(self.create, .001)
        
        
    def create(self, dt):
       # for i in range(3):
            p = Particle()
            self.add_widget(p)
            p.pos = self.create_pos
            p.init()
            for i in self.children:
                i.fade(dt)
                if i .visibility<0:
                    self.remove_widget(i)
            self.label.text=str(len(self.children))
    
    def on_touch_down(self, touch):
        self.create_pos=touch.pos
        
    def on_touch_move(self, touch):
        self.create_pos=touch.pos


class ParticlesApp(App):
    
    def build(self):
        return Particles()


ParticlesApp().run()