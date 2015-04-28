import cocos
from cocos.actions import *

class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        super( HelloWorld, self ).__init__(4,64,224,255)
        label = cocos.text.Label('Hello World',
                          font_name='Lora',
                          font_size=32,
                          anchor_x='center', anchor_y='center')
        label.position = (320, 240)
        self.add(label)
        sprite = cocos.sprite.Sprite('grossini.png')
        sprite.position = (320, 240)
        sprite.scale = 2
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=2)
        # action 
        label.do(Repeat(scale + Reverse(scale)))

cocos.director.director.init()
hello_layer = HelloWorld()
hello_layer.do(RotateBy(360, duration=10))
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)

    
