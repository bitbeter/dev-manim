from manim import *
from manim_slides.slide import Slide


class CreateCircle(Slide):
    def construct(self):
        epsilon = .1
        n_points = 10

        states = [
            [0 + n * epsilon, 0 + n * epsilon, 0 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([BLUE_E, YELLOW], len(states))

        animations = [
            Circle(color=n, arc_center=state) for state, n in zip(states, colors)
        ]

        self.play(*[Create(c) for c in animations])


        self.next_slide(loop=True)

        self.play(*[Create(c, scale_value=1.9) for c in animations])


        # self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        # self.next_slide()  # This will start a new non-looping slide

        # circle_red = Circle(color=RED)
        # circle_green = Circle(color=GREEN)
        # circle_blue = Circle(color=BLUE)
        # circle_red.shift(LEFT)
        # circle_blue.shift(RIGHT)
        # gr = VGroup(circle_red, circle_green)
        # gr2 = VGroup(circle_blue) # Constructor uses add directly
        # self.add(gr,gr2)
        # self.wait()
        # gr += gr2 # Add group to another
        # self.play(
        #     gr.animate.shift(DOWN),
        # )
        # gr -= gr2 # Remove group
        # self.play( # Animate groups separately
        #     gr.animate.shift(LEFT),
        #     gr2.animate.shift(UP),
        # )
        # self.play( #Animate groups without modification
        #     (gr+gr2).animate.shift(RIGHT)
        # )
        # self.play( # Animate group without component
        #     (gr-circle_red).animate.shift(RIGHT)
        # )
