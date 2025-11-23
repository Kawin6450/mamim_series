from manim import *

class Rotating3DSystem(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cube = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.7)
        title = Text("3D坐标系演示", font_size=36).to_edge(UP)
        """
        设置3D摄像机视角
        phi：仰视角（从正Z轴向下看的角度）
           - 0度：从正上方垂直向下看
           - 90度：从水平面平视
           - 180度：从正下方向上看
        theta：方位角（围绕Z轴旋转的角度）
           - 0度：从正X轴方向看
           - 90度：从正Y轴方向看
           - 180度：从负X轴方向看
           - 270度：从负Y轴方向看
        当前设置：phi=75度（稍微仰视），theta=-45度（从右前方从45度角观察）
        """
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add_fixed_in_frame_mobjects(title)

        self.play(Write(title), Create(axes), Create(cube))
        self.wait(1)
        """
        旋转动画：让立方体围绕Y轴旋转180度
        Rotate()参数说明：
           cube：要旋转的对象（立方体）
           angie=PI:旋转角度（PI = 180度）
           axis=UP：旋转轴（UP = Y轴方向）
        run_time=2：动画持续2秒
        """
        self.play(Rotate(cube,angle=PI,axis=UP),run_time=5)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()

config.preview = True
scene = Rotating3DSystem()
scene.render()