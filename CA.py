from manim import * #manim -pql CA.py -a

class centripetalacceleration(Scene):
    def construct(self):
        circle = Circle(radius = 2, color = WHITE)
        dot = Dot(point = [0,-2,1], radius = 0.08, color = YELLOW)
        circlevelocity = Circle(radius = 0.8, color = YELLOW).move_to(dot.get_center())
        vect1 = Line(start = dot.get_center(), end = [0,0,1]).add_tip().set_color(YELLOW)
        dot2 = Dot(point = [0.8,-2,1], radius = 0.08, fill_opacity = 0)
        dot3 = Dot(radius = 0.08, color = YELLOW).move_to(dot.get_center()).shift(RIGHT*0.8)
        vectL = Line(start = dot.get_center() , end = dot2.get_center(), color = YELLOW).add_tip()
        radius = Text("r", font_size = 40).rotate(PI/2).move_to([-0.25,-1,1])
        velocity = Text("v", font_size = 40).move_to([0.25,-2.3,1])
        dotdraw = Dot(point = [0.8,-2,1], radius = 0.08, fill_opacity = 0)
        dotcenter = Dot(point = [0,0,1],radius = 0.15)
        workingout = [
            MathTex(r"\textit{acceleration}=\frac{\textit{change in velocity}}{\textit{elapsed time}}").move_to([0,2.5,1]),
            MathTex(r"\textit{change in velocity} = 2\pi\textit{v} ").move_to([0,2.5,1]),
            MathTex(r"\textit{elapsed time} = \frac{\textit{distance}}{\textit{velocity}}").move_to([0,2.5,1]),
            MathTex(r"\textit{elapsed time} = \frac{2\pi \textit{r}}{\textit{v}}").move_to([0,2.5,1]),
            MathTex(r"acceleration = \frac{2\pi \textit{v}}{\frac{2\pi \textit{r}}{\textit{v}}}").move_to([0,2.5,1]),
            MathTex(r"acceleration = \frac{2\pi v^{2}}{2\pi r}").move_to([0,2.5,1]),
            MathTex(r"acceleration = \frac{v^{2}}{r}").move_to([0,2.5,1]),
            MathTex(r"acceleration = \frac{v^{2}}{r}=\omega ^{2}r").move_to([0,2.5,1])
                ]
        
        path = VMobject()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        movement = Line(dot2.get_center(), dot2.get_center()).set_color(ORANGE)


        
        def update_VectL(vectL):
            vectk = Line(start = dot.get_center(), end = dot2.get_center(),color = YELLOW).add_tip()
            vectL.become(vectk)
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        def update_tip(vect1):
            vect2 = Line(start = dot.get_center(), end = [0,0,1]).add_tip().set_color(YELLOW)
            vect1.become(vect2)
        def update_center(circlevelocity):
            circle1 = Circle(radius = 0.8, color = YELLOW).move_to(dot.get_center())
            circlevelocity.become(circle1)
        def update_point(dot3):
            dot4 = Dot(radius = 0.08, color = YELLOW).move_to(dot.get_center()).shift(RIGHT*0.8)
            dot3.become(dot4)
        def update_line(movement):
            movement.append_points(Line(dotdraw,dot2).get_points()).set_color(ORANGE)
            dotdraw.become(dot2)

 

        path.add_updater(update_path) #runs every frame
        self.add(dot, path, dotcenter)
        self.play(Rotating(dot, radians = 2*PI, about_point = ORIGIN, run_time = 4))
        self.add(circle, movement, dotdraw)
        self.wait()
        path.clear_updaters()
        self.add(circle, movement)
        self.play(FadeIn(vect1,circlevelocity,dot2,vectL,dot3))
        self.wait()
        vect1.add_updater(update_tip)
        vectL.add_updater(update_VectL)  
        circlevelocity.add_updater(update_center)
        dot3.add_updater(update_point)
        #movement.add_updater(update_line)
        self.play(
            MoveAlongPath(dot2, circlevelocity, run_time = 4.00, rate_func = linear, buff = -0.05), #buffing fixes displacement caused by calculations
            Rotating(dot, radians = 2*PI, about_point = ORIGIN, run_time= 4)
            )
        self.play(
            MoveAlongPath(dot2, circlevelocity, run_time = 4.00, rate_func = linear, buff = -0.05), #buffing fixes displacement caused by calculations
            Rotating(dot, radians = 2*PI, about_point = ORIGIN, run_time= 4)
            )
        self.wait()
        self.play(Write(radius))
        self.play(Write(velocity))
        vect1.remove_updater(update_tip)
        vectL.remove_updater(update_VectL)
        circlevelocity.remove_updater(update_center)
        dot3.remove_updater(update_point)
        
        
        group = VGroup(circle, circlevelocity, dot, dot2,dotcenter, vect1, vectL,velocity,radius,path, dot3, movement, dotdraw)
        self.play(group.animate.shift(DOWN),run_time=2)
        self.play(Write(workingout[0]),run_time=3)
        self.wait()
        self.play(ReplacementTransform(workingout[0],workingout[1]),run_time = 4)
        self.wait()
        self.play(Indicate(circlevelocity, scale_factor = 1.7, color = BLUE), run_time = 2)
        self.wait()
        self.play(ReplacementTransform(workingout[1],workingout[2]),run_time = 4)
        self.wait()
        self.play(ReplacementTransform(workingout[2],workingout[3]),run_time = 4)
        self.wait()
        self.play(Indicate(circle, scale_factor = 1.3, color = BLUE), run_time = 2)
        for i in range(3,7):
            self.play(ReplacementTransform(workingout[i],workingout[i+1]), run_time = 4)
            self.wait()
        self.wait()
            
        
        
