from manim import *
import random

class Rotating3DSystem(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        title = Text("3D坐标系演示", font_size=36).to_edge(UP)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add_fixed_in_frame_mobjects(title)

        blocks = VGroup()
        for i in range(5):
            for j in range(5):
                height = random.random()*1.5 + 0.5
                block = Prism(dimensions=[0.6,0.6,height])
                if height < 1.0:
                    color = BLUE
                elif height < 1.5:
                    color = GREEN
                block.set_color(color)
                block.move_to([i-2,j-2,0])
                blocks.add(block)
    
    # -----

        self.play(Write(title), Create(axes), Create(blocks))
        self.wait(1)
        """
                Z (OUT/IN)
                ↑
                |
                |
                +----→ X (RIGHT/LEFT)
               /
              /
             /
            Y (UP/DOWN) - 这个在3D中指向屏幕内/外
        """
        self.play(Rotate(blocks,angle=PI,axis=OUT),run_time=5)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()

config.preview = True
# 低分辨率，测试用（速度会快一点），获得原来的只要注释掉下面的代码就行
# config.quality = "low_quality"
scene = Rotating3DSystem()
scene.render()