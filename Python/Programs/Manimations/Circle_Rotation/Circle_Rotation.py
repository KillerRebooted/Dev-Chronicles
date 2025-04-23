from manim import *

class CircleRotation(Scene):
    def construct(self):
        # Intro Text
        start_text = Text("The 1982 SAT Question\n   Everyone got Wrong")

        # Main Question
        q1 = Text("In the figure above, the radius of circle A is", font_size=20).move_to(LEFT*2.2)
        q2 = Text("r", font_size=20).next_to(q1, RIGHT, buff=0.12)
        q3 = Text("and the radius of circle B is", font_size=20).next_to(q2, RIGHT, buff=0.12).align_to(q2, DOWN)
        q4 = Text("3r", font_size=20).next_to(q3, RIGHT, buff=0.1).align_to(q3, DOWN)
        q5 = Text(".", font_size=20).next_to(q4, RIGHT, buff=0.1).align_to(q4, DOWN)
        q6 = Text("Starting from the position shown in the figure, circle A rolls around circle B.\nAt the end of how many revolutions of circle A will the center of circle first\nreach its starting point?", font_size=20).next_to(q1, DOWN, buff=0.03).align_to(q1, LEFT)

        question = Group(q1, q2, q3, q4, q5, q6)
        
        # Create Demo Circles
        color_1 = YELLOW
        color_2 = BLUE

        circle_r = Circle(radius=1, color=color_1).shift(DOWN*0.2)
        ref_circle_r_true = Circle(radius=1.5, color=color_1).shift(DOWN*0.2)
        
        circle_r_by_3 = circle_r.copy()
        ref_circle_r_by_3 = Circle(radius=1, color=color_2).next_to(circle_r, LEFT, buff=0)
        ref_circle_r_by_3_true = Circle(radius=0.5, color=color_2).move_to(ref_circle_r_by_3)

        # Adding Audio Track to the Animation
        self.add_sound("Edited Sample 1.mp3")

        self.play(Write(start_text, font_size=30), run_time=3)
        self.wait(4)
        self.play(Unwrite(start_text), run_time=1)

        self.play(Write(q1), run_time=2)
        self.play(Write(q2, run_time=0.5))
        self.play(Write(q3), run_time=1.5)
        self.play(Write(q4), run_time=0.5)
        self.play(Write(q5), run_time=0.5)
        self.play(Write(q6), run_time=7.5)

        self.play(question.animate.shift(UP*3), run_time=1)

        self.play(GrowFromCenter(circle_r), run_time=1)
        self.play(Transform(circle_r_by_3, ref_circle_r_by_3), run_time=1)

        q2_copy = q2.copy()
        q4_copy = q4.copy()
        
        self.play(FadeToColor(q2_copy, color=color_2), FadeToColor(q4_copy, color=color_1), Circumscribe(q2_copy), Circumscribe(q4_copy), run_time=1)
        self.play(q2_copy.animate.move_to(circle_r_by_3.get_center()), q4_copy.animate.move_to(circle_r.get_center()), run_time=1)

        self.play(Transform(circle_r, ref_circle_r_true), Transform(circle_r_by_3, ref_circle_r_by_3_true), FadeOut(q2_copy), FadeOut(q4_copy), run_time=1.5)
        self.wait(1)

        # Display Options
        A = Text("A)", font_size=24)
        A_num = MathTex(r"\frac{3}{2}", font_size=28).next_to(A, RIGHT, buff=0.2)
        option_A = Group(A, A_num)
        option_A.shift(DOWN*3 + LEFT*4 + LEFT*0.2)
        B = Text("B)", font_size=24)
        B_num = Text("3", font_size=24).next_to(B, RIGHT, buff=0.2)
        option_B = Group(B, B_num)
        option_B.shift(DOWN*3 + LEFT*2 + LEFT*0.2)
        C = Text("C)", font_size=24)
        C_num = Text("6", font_size=24).next_to(C, RIGHT, buff=0.2)
        option_C = Group(C, C_num)
        option_C.shift(DOWN*3 + LEFT*0 + LEFT*0.2)
        D = Text("D)", font_size=24)
        D_num = MathTex(r"\frac{9}{2}", font_size=28).next_to(D, RIGHT, buff=0.2)
        option_D = Group(D, D_num)
        option_D.shift(DOWN*3 + RIGHT*2 + LEFT*0.2)
        E = Text("E)", font_size=24)
        E_num = Text("9", font_size=24).next_to(E, RIGHT, buff=0.2)
        option_E = Group(E, E_num)
        option_E.shift(DOWN*3 + RIGHT*4 + LEFT*0.2)

        self.play(FadeIn(option_A), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(option_B), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(option_C), run_time=1.5)
        self.play(FadeIn(option_D), run_time=1.5)
        self.play(FadeIn(option_E), run_time=1.5)
        self.wait(18)

        # Highlight Intuitive but Wrong Option B)
        wrong_B = Text("B)", font_size=24, color=PURE_RED)
        wrong_B_num = Text("3", font_size=24, color=PURE_RED).next_to(wrong_B, RIGHT, buff=0.2)
        wrong_option_B = Group(wrong_B, wrong_B_num).move_to(option_B)

        self.play(Circumscribe(option_B), run_time=1)
        self.wait(1)
        self.play(Transform(option_B, wrong_option_B), run_time=1)

        # Display Perimeter to support Intuitive Answer
        self.wait(7)
        circum_1 = Text("3×2πr", font_size=30).next_to(circle_r, UP)
        circum_2 = Text("2πr", font_size=30).next_to(circle_r_by_3, UP*1.5)
        solved_circum_1 = Text("6πr", font_size=30).move_to(circum_1)

        self.play(Write(circum_2), run_time=1)
        self.wait(3)
        self.play(TransformFromCopy(circum_2, circum_1), run_time=1)
        self.wait(4)
        self.play(Transform(circum_1, solved_circum_1), run_time=1)
        self.wait(2)

        # Demonstrate that the Perimeter of Larger Circle is 3 Times the Smaller one
        arc_1 = Arc(angle=2*PI/3, radius=1.5, start_angle=-PI, color=color_2).shift(DOWN*0.2)
        arc_2 = Arc(angle=2*PI/3, radius=1.5, start_angle=-PI+2*PI/3, color=color_2).shift(DOWN*0.2)
        arc_3 = Arc(angle=2*PI/3, radius=1.5, start_angle=-PI+4*PI/3, color=color_2).shift(DOWN*0.2)

        self.play(TransformFromCopy(circle_r_by_3, arc_1), run_time=1)
        self.wait(1)
        self.play(TransformFromCopy(circle_r_by_3, arc_2), run_time=1)
        self.wait(1)
        self.play(TransformFromCopy(circle_r_by_3, arc_3), run_time=1)
        self.wait(8.5)

        # Reveal that all options were wrong
        wrong_A = Text("A)", font_size=24, color=PURE_RED)
        wrong_A_num = MathTex(r"\frac{3}{2}", font_size=28, color=PURE_RED).next_to(wrong_A, RIGHT, buff=0.2)
        wrong_option_A = Group(wrong_A, wrong_A_num).move_to(option_A)
        wrong_C = Text("C)", font_size=24, color=PURE_RED)
        wrong_C_num = Text("6", font_size=24, color=PURE_RED).next_to(wrong_C, RIGHT, buff=0.2)
        wrong_option_C = Group(wrong_C, wrong_C_num).move_to(option_C)
        wrong_D = Text("D)", font_size=24, color=PURE_RED)
        wrong_D_num = MathTex(r"\frac{9}{2}", font_size=28, color=PURE_RED).next_to(wrong_D, RIGHT, buff=0.2)
        wrong_option_D = Group(wrong_D, wrong_D_num).move_to(option_D)
        wrong_E = Text("E)", font_size=24, color=PURE_RED)
        wrong_E_num = Text("9", font_size=24, color=PURE_RED).next_to(wrong_E, RIGHT, buff=0.2)
        wrong_option_E = Group(wrong_E, wrong_E_num).move_to(option_E)

        self.play(Transform(option_A, wrong_option_A), run_time=0.5)
        self.play(Transform(option_C, wrong_option_C), run_time=0.5)
        self.play(Transform(option_D, wrong_option_D), run_time=0.5)
        self.play(Transform(option_E, wrong_option_E), run_time=0.5)
        self.wait(13.5)

        self.play(FadeOut(option_A), FadeOut(option_B), FadeOut(option_C), FadeOut(option_D), FadeOut(option_E), run_time=1)
        self.wait(3)

        # Create and Display Coin Demonstration
        coin_1_circle = Circle(radius=1.1, color="#DC143C")
        coin_2_circle = Circle(radius=1.1, color="#DC143C").next_to(coin_1_circle, UP, buff=0)
        coin_1 = ImageMobject("Coin.png").scale(0.5)
        coin_2 = ImageMobject("Coin.png").scale(0.5).move_to(coin_2_circle)
        
        self.play(FadeOut(question), FadeOut(arc_1), FadeOut(arc_2), FadeOut(arc_3), FadeOut(circum_1), FadeOut(circum_2), run_time=1)
        self.wait(1)
        self.play(Transform(circle_r, coin_1_circle), Transform(circle_r_by_3, coin_2_circle), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(circle_r), FadeOut(circle_r_by_3), FadeIn(coin_1), FadeIn(coin_2), run_time=1.5)
        self.wait(1.5)
        
        flash_1 = ShowPassingFlash(coin_1_circle.copy().set_color(RED).set_stroke(width=8))
        flash_2 = ShowPassingFlash(coin_2_circle.copy().set_color(RED).set_stroke(width=8))
        self.play(flash_1, flash_2, run_time=1)
        
        self.play(Rotate(coin_2, angle=2*PI), MoveAlongPath(coin_2, Arc(angle=PI, radius=2.2, start_angle=PI/2)), rate_func=linear, run_time=3)
        self.wait(1)
        self.play(Rotate(coin_2, angle=2*PI), MoveAlongPath(coin_2, Arc(angle=PI, radius=2.2, start_angle=-PI/2)), rate_func=linear, run_time=3)
        self.wait(5)
        self.play(Rotate(coin_2, angle=2*PI), MoveAlongPath(coin_2, Arc(angle=PI, radius=2.2, start_angle=PI/2)), rate_func=linear, run_time=3)
        self.wait(1)
        self.play(Rotate(coin_2, angle=2*PI), MoveAlongPath(coin_2, Arc(angle=PI, radius=2.2, start_angle=-PI/2)), rate_func=linear, run_time=3)