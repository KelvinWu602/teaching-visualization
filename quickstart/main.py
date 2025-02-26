from manim import *

class DisplacementGraphDemo(Scene):
    def construct(self):
        graph = Axes(x_range=[0, 11], y_range=[-6, 6], x_length=6, y_length=6, axis_config={"color": BLUE, "include_numbers": True }).shift(LEFT * 2)
        labels = graph.get_axis_labels(x_label=Tex(r"\text{Time}/\text{s}").scale(0.5), y_label=Tex(r"\text{Displacement}/\text{m}").scale(0.5)).set_color(WHITE)

        circle = Circle(color=RED, fill_opacity=0.5).next_to(graph, RIGHT, buff=2)
        circle.set_height(0.5)
        circle.set_width(0.5)

        self.add(graph)
        self.add(labels)
        self.add(circle)
        # for the first 2s
        # circle move up to y = 4 in 2s
        # plot the line y = 2x with x range [0, 2] in 2s 
        line1 = graph.plot(lambda x: 2 * x, x_range=[0, 2], use_smoothing=False)
        self.play(circle.animate.shift(UP * 2), Create(line1))


        # for the next 2s
        # circle stay stationary 
        # plot the line y = 4 with x range [2, 4] in 2s
        line2 = graph.plot(lambda x: 4, x_range=[2, 4], use_smoothing=False)
        self.play(Create(line2))


        # for the next 2s
        # circle move down to y = -4 in 2s
        # plot the line y = -2x + 8 with x range [2, 4] in 2s
        line3 = graph.plot(lambda x: 20 - x * 4, x_range=[4, 6], use_smoothing=False)
        self.play(circle.animate.shift(DOWN * 4), Create(line3))

        # for the next 1s
        # circle move up to y = -3 in 1s
        # plot the line y = -3 with x range [6, 7] in 1s
        line4 = graph.plot(lambda x: -10+x, x_range=[6, 7], use_smoothing=False)
        self.play(circle.animate.shift(UP * 0.5), Create(line4))

        # for the next 1s
        # circle move down to y = -4 in 1s
        # plot the line y = -4 with x range [7, 8] in 1s
        line5 = graph.plot(lambda x: 4 - x, x_range=[7, 8], use_smoothing=False)
        self.play(circle.animate.shift(DOWN * 0.5), Create(line5))

        # for the next 2s
        # circle move up to y = 0 in 2s
        # plot the line y = 4x - 20 with x range [8, 10] in 2s
        line6 = graph.plot(lambda x: 2 * x - 20, x_range=[8, 10], use_smoothing=False)
        self.play(circle.animate.shift(UP * 2), Create(line6))
        
        




