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
        
class STSlopeIsVelocityDemo(Scene):
    def construct(self):
        graph = Axes(x_range=[0, 10], y_range=[-6, 6], x_length=6, y_length=6, axis_config={"color": BLUE, "include_numbers": True })
        labels = graph.get_axis_labels(x_label=Tex(r"\text{Time}/\text{s}").scale(0.5), y_label=Tex(r"\text{Displacement}/\text{m}").scale(0.5)).set_color(WHITE)

        
        self.add(graph)
        self.add(labels)
        line1 = graph.plot(lambda x: 2 * x, x_range=[0, 2], use_smoothing=False)
        line2 = graph.plot(lambda x: 4, x_range=[2, 4], use_smoothing=False)
        line3 = graph.plot(lambda x: 20 - x * 4, x_range=[4, 6], use_smoothing=False)
        line4 = graph.plot(lambda x: -10+x, x_range=[6, 7], use_smoothing=False)
        line5 = graph.plot(lambda x: 4 - x, x_range=[7, 8], use_smoothing=False)
        line6 = graph.plot(lambda x: 2 * x - 20, x_range=[8, 10], use_smoothing=False)
        self.add(line1, line2, line3, line4, line5, line6)


        
        ## Separate the lines segments evenly across the screen
        # Calculate positions for line segments
        displacements = [4, 0, -8, 1, -1, 2]
        times = [2, 2, 2, 1, 1, 2]
        lines = [line1, line2, line3, line4, line5, line6]
        texts = []
        self.play(FadeOut(graph), FadeOut(labels))
        screen_width = config.frame_width - 2  # Leave some margin
        segment_width = screen_width / len(lines)
        # Position each segment horizontally with equal spacing
        for i, line in enumerate(lines):
            # Calculate target x position 
            target_x = -screen_width/2 + segment_width/2 + i*segment_width
            # Move segment to position
            # show the slope of the segment
            # slope_text = Tex(f"\\text{{Slope}}={displacements[i]/times[i]}=\\frac{{{displacements[i]}\\text{{ m}}}}{{{times[i]}\\text{{ s}}}}=\\text{{Velocity}}={displacements[i]/times[i]}\\text{{ m/s}}").scale(0.5)
            slope_text = Tex(f"\\text{{Slope}} = {int(displacements[i]/times[i])} \\\\[0.5em] \\text{{Velocity}} = $\\frac{{{displacements[i]}m}}{{{times[i]}s}}$ \\\\[0.5em] = {int(displacements[i]/times[i])}  $ms^{{-1}}$").scale(0.5)
            slope_text.move_to([target_x, -3, 0])
            self.play(line.animate.move_to([target_x, 0, 0]), Create(slope_text))
            texts.append(slope_text)

        ## Fade out everything
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4), FadeOut(line5), FadeOut(line6), FadeOut(*texts))

        ## Display text in the middle of the screen
        text = Text("Velocity = slope of the displacement-time graph").scale(0.5)
        equation = Tex("v = $\\frac{\Delta s}{\Delta t}$").scale(2)
        text.move_to([0, 0.75, 0])
        equation.move_to([0, -0.5, 0])
        self.play(Create(text), Create(equation))
        self.wait(1)
