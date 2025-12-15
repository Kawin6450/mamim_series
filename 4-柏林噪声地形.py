from manim import *
from perlin_noise import PerlinNoise
import numpy as np

class Rotating3DSystem(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        title = Text("柏林噪声地形动画演示", font_size=36).to_edge(UP)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add_fixed_in_frame_mobjects(title)
        '''
        控制细节层次，值越小地形越平滑，值越大细节越丰富
        随机种子，固定值确保每次运行结果相同，便于教学演示
        '''
        noise_gen = PerlinNoise(octaves=4,seed=114514)

        def terrian_surface(u,v):
            noise_val = noise_gen([u/3.0,v/3.0])
            height = (noise_val+0.5)*1.5+0.5
            return np.array([u,v,height])

        terrian = Surface(
            terrian_surface,
            u_range=[-2,2],
            v_range=[-2,2],
            resolution=(30,30),
            fill_opacity=0.8
        )

        terrian.set_color_by_gradient(BLUE,GREEN,YELLOW)

        self.play(Write(title),Create(axes))
        self.play(Create(terrian),run_time=3) # 曲面创建
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
        self.play(Rotate(terrian,angle=PI,axis=OUT),run_time=5)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()

config.preview = True
# 低分辨率，测试用（速度会快一点），获得原来的只要注释掉下面的代码就行
# config.quality = "low_quality"
scene = Rotating3DSystem()
scene.render()