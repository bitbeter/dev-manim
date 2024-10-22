from manim import *
from manim_slides.slide import Slide
from manim_dsa import *


class CreateCircle(Slide):
    def construct(self):
        epsilon = .1
        n_points = 10

        points = [
            [0 + n * epsilon, 0 + n * epsilon, 0 + n * epsilon]
            for n in range(n_points)
        ]
        colors = color_gradient([BLUE_E, YELLOW], len(points))

        circles = [
            Circle(arc_center=p, color=c) for p, c in zip(points, colors)
        ]

        squares = [
            Square(color=c) for p, c in zip(points, colors)
        ]

        self.play(Create(c) for c in circles)

        self.next_slide()

        self.play(Transform(c, s) for c, s in zip(circles, squares))

        self.next_slide(loop=True)

        self.play(Wiggle(c, scale_value=1.9) for c in circles)


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

        self.next_slide()

        graph = {
            'A': [('C', 11), ('D', 7)],
            'B': [('A', 5),  ('C', 3)],
            'C': [('A', 11), ('B', 3)],
            'D': [('A', 7),  ('C', 4)],
        }
        nodes_and_positions = {
            'A': LEFT * 1.5,
            'B': UP * 2,
            'C': RIGHT * 1.5,
            'D': DOWN * 2,
        }

        mArray = (
            MArray([1, 2, 3], style=ArrayStyle.BLUE)
            .add_indexes()
            .scale(0.9)
            .add_label(Text("Array", font="Cascadia Code"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=StackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("Stack", font="Cascadia Code"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, GraphStyle.PURPLE)
            .add_label(Text("Graph", font="Cascadia Code"))
            .to_edge(RIGHT, 1)
        )

        self.play(Create(mArray))
        self.play(Create(mStack))
        self.play(Create(mGraph))
        self.wait()
