from manim import *
import pandas as pd 

# elements is the name of the csv with the element information
# I am using only the element symbol, atomic number and atomic mass, 
# but with the information inside the csv you can include a lot more
elements = pd.read_csv("Elements.csv")

# White Background looks good for me
config.background_color = WHITE

# Here we create the base for the elements. 
#element_number is the atomic number of the element we want to draw. 
#We'll se later, in the Element(Scene) object how to change it.


def element_frame(self, element_number=1, fill_colors = color_gradient((BLUE,BLUE,WHITE),10)):

     #These color the rectangle as a color_gradient.
    color = BLACK # Sets the color to all the text and the vertices of the frame


    Frame = Rectangle(width = 1.5, height = 2, stroke_width = 0.9, color = color, fill_color = fill_colors, fill_opacity = 0.1)
    Element = Text(str(elements.iloc[[element_number-1],[1]]).split()[2], color = color)
    Element_Symbol = Text(str(elements.iloc[[element_number-1],[2]]).split()[2], color = color)
    Atomic_number = Text(str(elements.iloc[[element_number-1],[0]]).split()[2], color = color)
    Atomic_Mass = Text(str(elements.iloc[[element_number-1],[3]]).split()[2], color = color)
    
    #TODO: Now you get a nice looking framed element, but if we want to reshape
    # the rectangle, it becomes a mess. In the future, I'll make the position and 
    # size of the information relative to the rectangle

    #Scales everything to make it fit inside the frame. Element_Symbol is not scaled as it's the reference for the other things. 
    Element.scale(0.5)
    Atomic_number.scale(0.5)
    Atomic_Mass.scale(0.3)

    #Keeps scaling element name  in case (eg. Carbon fits very well with a 0.5 scale, Praseodymium does not)
    while Element.get_width()*1.05 > Frame.get_width():
        Element.scale(0.95)

    # Moves everything to it's place inside the frame.
    Element_Symbol.move_to(Frame.get_center()+0.15*UP)
    Element.move_to(Frame.get_center()+0.4*DOWN)
    Atomic_number.move_to(Frame.get_top()+Frame.get_left())
    Atomic_Mass.move_to(Frame.get_center()+0.75*DOWN)


    #Keeps moving the atomic number in case it's too big
    while Atomic_number.get_left()[0]+0.05*LEFT[0] < Frame.get_left()[0]:
        Atomic_number.shift(0.01*RIGHT)
    while Atomic_number.get_top()[1]+0.05*UP[1] > Frame.get_top()[1]:
        Atomic_number.shift(0.01*DOWN)    


    #puts everything inside a VGroup to make it easier to call back.
    element_framed=VGroup(Frame, Element, Element_Symbol, Atomic_number, Atomic_Mass)
    return(element_framed)


    #Here we use Element(Scene) as a normal animation with the element_frame as any other MObject
    # Use Element to chose an element. H = 1, He = 2, etc.


class Element(Scene):
    def construct(self, Element = 34):
        your_element = element_frame(self, Element)
        self.play(GrowFromEdge(your_element, LEFT))
        self.wait()
        
    #It's only used if we call it outside the object. Very usefull to get a lot of diferent videos 
    # with the same animation but with different element. 
    # To use it, in the python control just type python Elements_manim.py and it will do 
    # what you said OUTSIDE the object (see above)
    def render_element(self, Element = 1):
        self.setup()
        self.construct(Element)
        self.tear_down()
        self.renderer.finish(self)
        logger.info(
                f"Rendered {str(self)}\nPlayed {self.renderer.num_plays} animations"
            )

"""

#Example of the use of render_element with Hydrogen and Oganesson:

#use this to change the name of the file.
config.output_file = "Hydrogen" 
H = Element().render_element(Element = 1)

#use again with a diferent nameor it will rewrite the last file
config.output_file = "Oganesson" 
Og = Element().render_element(Element = 118)

#Example of using render_element with a list of elements
# TODO: Include the use of the csv file to take a range of elements (Eg. from C to F).
# Not necessary to do it right now as it's only an example.


elements_list = ["H","He","Li"]

for element in range(len(elements_list)):
    config.output_file = elements_list[element]
    Element().render_element(element+1)    


# TODO: Include the option of rendering as png


"""

# It's easy to build a simple periodic table. 
#I'll use Hydrogen as the reference element

class Periodic_Table(Scene):
    def construct(self):

        #Group 1
        H = element_frame(self, 1)
        Li = element_frame(self,3,color_gradient((RED,RED,WHITE),100)).next_to(H,DOWN, buff = 0)
        Na = element_frame(self,11,color_gradient((RED,RED,WHITE),10)).next_to(Li,DOWN, buff = 0)
        K = element_frame(self,19,color_gradient((RED,RED,WHITE),10)).next_to(Na,DOWN, buff = 0)
        Rb = element_frame(self,37,color_gradient((RED,RED,WHITE),10)).next_to(K,DOWN, buff = 0)
        Cs = element_frame(self,55,color_gradient((RED,RED,WHITE),10)).next_to(Rb,DOWN, buff = 0)
        Fr = element_frame(self,87,color_gradient((RED,RED,WHITE),10)).next_to(Cs,DOWN, buff = 0)

        grupo_1 = VGroup(H,Li,Na,K,Rb,Cs,Fr)

    
        #Group 2
        Be = element_frame(self,4,color_gradient((ORANGE,ORANGE,WHITE),10)).next_to(Li,RIGHT, buff = 0)
        Mg = element_frame(self,12,color_gradient((ORANGE,ORANGE,WHITE),10)).next_to(Be,DOWN, buff = 0)
        Ca = element_frame(self,20,color_gradient((ORANGE,ORANGE,WHITE),10)).next_to(Mg,DOWN, buff = 0)
        Sr = element_frame(self,38,color_gradient((ORANGE,ORANGE,WHITE),10)).next_to(Ca,DOWN, buff = 0)
        Ba = element_frame(self,56,color_gradient((ORANGE,ORANGE,WHITE),10)).next_to(Sr,DOWN, buff = 0)
        Ra = element_frame(self,88,color_gradient((ORANGE,ORANGE,WHITE),10)).next_to(Ba,DOWN, buff = 0)

        grupo_2 = VGroup(Be,Mg,Ca,Sr,Ba,Ra)


        #Group 3
        Sc = element_frame(self,21,color_gradient((GREY,GREY,WHITE),10)).next_to(Ca,RIGHT, buff = 0)
        Y = element_frame(self,39,color_gradient((GREY,GREY,WHITE),10)).next_to(Sc,DOWN, buff = 0)
        La = element_frame(self,57,color_gradient((PINK,PINK,WHITE),10)).next_to(Y,DOWN, buff = 0)
        Ac = element_frame(self,89,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(La,DOWN, buff = 0)
        grupo_3 = VGroup(Sc, Y, La, Ac)
        


        #Grupo 4
        Ti = element_frame(self,22,color_gradient((GREY,GREY,WHITE),10)).next_to(Sc,RIGHT, buff = 0)
        Zr = element_frame(self,40,color_gradient((GREY,GREY,WHITE),10)).next_to(Ti,DOWN, buff = 0)
        Hf = element_frame(self,72,color_gradient((GREY,GREY,WHITE),10)).next_to(Zr,DOWN, buff = 0)
        Rf = element_frame(self,104,color_gradient((GREY,GREY,WHITE),10)).next_to(Hf,DOWN, buff = 0)
        grupo_4 = VGroup(Ti,Zr,Hf,Rf)
        


        #Group 5
        V = element_frame(self,23,color_gradient((GREY,GREY,WHITE),10)).next_to(Ti,RIGHT, buff = 0)
        Nb = element_frame(self,41,color_gradient((GREY,GREY,WHITE),10)).next_to(V,DOWN, buff = 0)
        Ta = element_frame(self,73,color_gradient((GREY,GREY,WHITE),10)).next_to(Nb,DOWN, buff = 0)
        Db = element_frame(self,105,color_gradient((GREY,GREY,WHITE),10)).next_to(Ta,DOWN, buff = 0)
        grupo_5 = VGroup(V, Nb, Ta, Db)
        


        #Group 6
        Cr = element_frame(self,25,color_gradient((GREY,GREY,WHITE),10)).next_to(V,RIGHT, buff = 0)
        Mo = element_frame(self,42,color_gradient((GREY,GREY,WHITE),10)).next_to(Cr,DOWN, buff = 0)
        W = element_frame(self,74,color_gradient((GREY,GREY,WHITE),10)).next_to(Mo,DOWN, buff = 0)
        Sg = element_frame(self,106,color_gradient((GREY,GREY,WHITE),10)).next_to(W,DOWN, buff = 0)
        grupo_6 = VGroup(Cr,Mo,W,Sg)
        


        #Group 7
        Mn = element_frame(self,25,color_gradient((GREY,GREY,WHITE),10)).next_to(Cr,RIGHT, buff = 0)
        Tc = element_frame(self,43,color_gradient((GREY,GREY,WHITE),10)).next_to(Mn,DOWN, buff = 0)
        Re = element_frame(self,75,color_gradient((GREY,GREY,WHITE),10)).next_to(Tc,DOWN, buff = 0)
        Bh = element_frame(self,107,color_gradient((GREY,GREY,WHITE),10)).next_to(Re,DOWN, buff = 0)
        grupo_7 = VGroup(Mn, Tc, Re, Bh)

        #Group 8
        Fe = element_frame(self,26,color_gradient((GREY,GREY,WHITE),10)).next_to(Mn,RIGHT, buff = 0)
        Ru = element_frame(self,44,color_gradient((GREY,GREY,WHITE),10)).next_to(Fe,DOWN, buff = 0)
        Os = element_frame(self,76,color_gradient((GREY,GREY,WHITE),10)).next_to(Ru,DOWN, buff = 0)
        Hs = element_frame(self,108,color_gradient((GREY,GREY,WHITE),10)).next_to(Os,DOWN, buff = 0)
        grupo_8 = VGroup(Fe,Ru,Os,Hs)


        #Group 9
        Co = element_frame(self,27,color_gradient((GREY,GREY,WHITE),10)).next_to(Fe,RIGHT, buff = 0)
        Rh = element_frame(self,45,color_gradient((GREY,GREY,WHITE),10)).next_to(Co,DOWN, buff = 0)
        Ir = element_frame(self,7,color_gradient((GREY,GREY,WHITE),10)).next_to(Rh,DOWN, buff = 0)
        Mt = element_frame(self,109,color_gradient((GREY,GREY,WHITE),10)).next_to(Ir,DOWN, buff = 0)
        grupo_9 = VGroup(Co,Rh,Ir,Mt)
        
  

        #Group 10
        Ni = element_frame(self,28,color_gradient((GREY,GREY,WHITE),10)).next_to(Co,RIGHT, buff = 0)
        Pd = element_frame(self,46,color_gradient((GREY,GREY,WHITE),10)).next_to(Ni,DOWN, buff = 0)
        Pt = element_frame(self,78,color_gradient((GREY,GREY,WHITE),10)).next_to(Pd,DOWN, buff = 0)
        Ds = element_frame(self,110,color_gradient((GREY,GREY,WHITE),10)).next_to(Pt,DOWN, buff = 0)
        grupo_10 = VGroup(Ni, Pd, Pt, Ds)
        


        #Group 11
        Cu = element_frame(self,29,color_gradient((GREY,GREY,WHITE),10)).next_to(Ni,RIGHT, buff = 0)
        Ag = element_frame(self,47,color_gradient((GREY,GREY,WHITE),10)).next_to(Cu,DOWN, buff = 0)
        Au = element_frame(self,79,color_gradient((GREY,GREY,WHITE),10)).next_to(Ag,DOWN, buff = 0)
        Rg = element_frame(self,111,color_gradient((GREY,GREY,WHITE),10)).next_to(Au,DOWN, buff = 0)
        grupo_11= VGroup(Cu, Ag, Au, Rg)
        

        #Group 12
        Zn = element_frame(self,30,color_gradient((GREY,GREY,WHITE),10)).next_to(Cu,RIGHT, buff = 0)
        Cd = element_frame(self,48,color_gradient((GREY,GREY,WHITE),10)).next_to(Zn,DOWN, buff = 0)
        Hg = element_frame(self,80,color_gradient((GREY,GREY,WHITE),10)).next_to(Cd,DOWN, buff = 0)
        Cn = element_frame(self,112,color_gradient((GREY,GREY,WHITE),10)).next_to(Hg,DOWN, buff = 0)
        grupo_12= VGroup(Zn, Cd, Hg, Cn)
        



        #Group 13
        
        Ga = element_frame(self,31,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Zn,RIGHT, buff = 0) # Inverted in order to put next to Zn
        Al = element_frame(self,13,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Ga,UP, buff = 0)
        B = element_frame(self,5,color_gradient((DARK_BROWN,DARK_BROWN,WHITE),10)).next_to(Al,UP, buff = 0)
        In = element_frame(self,49,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Ga,DOWN, buff = 0)
        Tl = element_frame(self,81,color_gradient((TEAL,TEAL,WHITE),10)).next_to(In,DOWN, buff = 0)
        Nh = element_frame(self,113,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Tl,DOWN, buff = 0)

        grupo_13 = VGroup(B,Al,Ga,In,Tl,Nh) # Reordered, as it should be

        #Group 14
        C = element_frame(self,6,color_gradient((MAROON,MAROON,WHITE),10)).next_to(B,RIGHT, buff = 0)
        Si = element_frame(self,14,color_gradient((DARK_BROWN,DARK_BROWN,WHITE),10)).next_to(C,DOWN, buff = 0)
        Ge = element_frame(self,32,color_gradient((DARK_BROWN,DARK_BROWN,WHITE),10)).next_to(Si,DOWN, buff = 0)
        Sn = element_frame(self,50,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Ge,DOWN, buff = 0)
        Pb = element_frame(self,82,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Sn,DOWN, buff = 0)
        Fl = element_frame(self,114,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Pb,DOWN, buff = 0)

        grupo_14 = VGroup(C,Si,Ge,Sn,Pb,Fl)

        #Group 15
        N = element_frame(self,7,color_gradient((MAROON,MAROON,WHITE),10)).next_to(C,RIGHT, buff = 0)
        P = element_frame(self,15,color_gradient((MAROON,MAROON,WHITE),10)).next_to(N,DOWN, buff = 0)
        As = element_frame(self,33,color_gradient((DARK_BROWN,DARK_BROWN,WHITE),10)).next_to(P,DOWN, buff = 0)
        Sb = element_frame(self,51,color_gradient((DARK_BROWN,DARK_BROWN,WHITE),10)).next_to(As,DOWN, buff = 0)
        Bi = element_frame(self,83,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Sb,DOWN, buff = 0)
        Mc = element_frame(self,115,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Bi,DOWN, buff = 0)

        grupo_15 = VGroup(N,P,As,Sb,Bi,Mc)

        #Group 16      
        O = element_frame(self,8,color_gradient((MAROON,MAROON,WHITE),10)).next_to(N,RIGHT, buff = 0)
        S = element_frame(self,16,color_gradient((MAROON,MAROON,WHITE),10)).next_to(O,DOWN, buff = 0)
        Se = element_frame(self,34,color_gradient((MAROON,MAROON,WHITE),10)).next_to(S,DOWN, buff = 0)
        Te = element_frame(self,52,color_gradient((DARK_BROWN,DARK_BROWN,WHITE),10)).next_to(Se,DOWN, buff = 0)
        Po = element_frame(self,84,color_gradient((DARK_BROWN,DARK_BROWN,WHITE),10)).next_to(Te,DOWN, buff = 0)
        Lv = element_frame(self,116,color_gradient((TEAL,TEAL,WHITE),10)).next_to(Po,DOWN, buff = 0)

        grupo_16 = VGroup(O,S,Se,Te,Po,Lv)

        #Group 17
        F = element_frame(self,9,color_gradient((GREEN,GREEN,WHITE),10)).next_to(O,RIGHT, buff = 0)
        Cl = element_frame(self,1,color_gradient((GREEN,GREEN,WHITE),10)).next_to(F,DOWN, buff = 0)
        Br = element_frame(self,35,color_gradient((GREEN,GREEN,WHITE),10)).next_to(Cl,DOWN, buff = 0)
        I = element_frame(self,53,color_gradient((GREEN,GREEN,WHITE),10)).next_to(Br,DOWN, buff = 0)
        At = element_frame(self,85,color_gradient((GREEN,GREEN,WHITE),10)).next_to(I,DOWN, buff = 0)
        Ts = element_frame(self,117,color_gradient((GREEN,GREEN,WHITE),10)).next_to(At,DOWN, buff = 0)

        grupo_17 = VGroup(F,Cl,Br,I,At,Ts)

        #Group 18

        Ne = element_frame(self,10,color_gradient((YELLOW,YELLOW,WHITE),10)).next_to(F,RIGHT, buff = 0) # Inverted again
        He = element_frame(self,2,color_gradient((YELLOW,YELLOW,WHITE),10)).next_to(Ne,UP, buff = 0)
        Ar = element_frame(self,18,color_gradient((YELLOW,YELLOW,WHITE),10)).next_to(Ne,DOWN, buff = 0)
        Kr = element_frame(self,36,color_gradient((YELLOW,YELLOW,WHITE),10)).next_to(Ar,DOWN, buff = 0)
        Xe = element_frame(self,54,color_gradient((YELLOW,YELLOW,WHITE),10)).next_to(Kr,DOWN, buff = 0)
        Rn = element_frame(self,86,color_gradient((YELLOW,YELLOW,WHITE),10)).next_to(Xe,DOWN, buff = 0)
        Og = element_frame(self,118,color_gradient((YELLOW,YELLOW,WHITE),10)).next_to(Rn,DOWN, buff = 0)

        grupo_18 = VGroup(He,Ne,Ar,Kr,Xe,Rn,Og)

        #Lanthanides
        Lan = element_frame(self,57,color_gradient((PINK,PINK,WHITE),10)).next_to(Ac,DOWN, buff = 1.5)
        Ce = element_frame(self,58,color_gradient((PINK,PINK,WHITE),10)).next_to(Lan,RIGHT, buff = 0)
        Pr = element_frame(self,59,color_gradient((PINK,PINK,WHITE),10)).next_to(Ce,RIGHT, buff = 0)
        Nd = element_frame(self,60,color_gradient((PINK,PINK,WHITE),10)).next_to(Pr,RIGHT, buff = 0)
        Pm = element_frame(self,61,color_gradient((PINK,PINK,WHITE),10)).next_to(Nd,RIGHT, buff = 0)
        Sm = element_frame(self,62,color_gradient((PINK,PINK,WHITE),10)).next_to(Pm,RIGHT, buff = 0)
        Eu = element_frame(self,63,color_gradient((PINK,PINK,WHITE),10)).next_to(Sm,RIGHT, buff = 0)
        Gd = element_frame(self,64,color_gradient((PINK,PINK,WHITE),10)).next_to(Eu,RIGHT, buff = 0)
        Tb = element_frame(self,65,color_gradient((PINK,PINK,WHITE),10)).next_to(Gd,RIGHT, buff = 0)
        Dy = element_frame(self,66,color_gradient((PINK,PINK,WHITE),10)).next_to(Tb,RIGHT, buff = 0)
        Ho = element_frame(self,67,color_gradient((PINK,PINK,WHITE),10)).next_to(Dy,RIGHT, buff = 0)
        Er = element_frame(self,68,color_gradient((PINK,PINK,WHITE),10)).next_to(Ho,RIGHT, buff = 0)
        Tm = element_frame(self,69,color_gradient((PINK,PINK,WHITE),10)).next_to(Er,RIGHT, buff = 0)
        Yb = element_frame(self,70,color_gradient((PINK,PINK,WHITE),10)).next_to(Tm,RIGHT, buff = 0)
        Lu = element_frame(self,71,color_gradient((PINK,PINK,WHITE),10)).next_to(Yb,RIGHT, buff = 0)

        lanthanides = VGroup(Lan,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu)
        
        #Actinides

        Act = element_frame(self,89,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Lan,DOWN, buff = 0)
        Th = element_frame(self,90,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Act,RIGHT, buff = 0)
        Pa = element_frame(self,91,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Th,RIGHT, buff = 0)
        U = element_frame(self,92,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Pa,RIGHT, buff = 0)
        Np = element_frame(self,93,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(U,RIGHT, buff = 0)
        Pu = element_frame(self,94,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Np,RIGHT, buff = 0)
        Am = element_frame(self,95,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Pu,RIGHT, buff = 0)
        Cm = element_frame(self,96,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Am,RIGHT, buff = 0)
        Bk = element_frame(self,97,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Cm,RIGHT, buff = 0)
        Cf = element_frame(self,98,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Bk,RIGHT, buff = 0)
        Es = element_frame(self,99,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Cf,RIGHT, buff = 0)
        Fm = element_frame(self,100,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Es,RIGHT, buff = 0)
        Md = element_frame(self,101,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Fm,RIGHT, buff = 0)
        No = element_frame(self,102,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(Md,RIGHT, buff = 0)
        Lr = element_frame(self,103,color_gradient((PURPLE,PURPLE,WHITE),10)).next_to(No,RIGHT, buff = 0)

        actinides = VGroup(Act,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr)

        #blocks

        s_block = VGroup(grupo_1, grupo_2)
        p_block = VGroup(grupo_13,grupo_14,grupo_15,grupo_16,grupo_17,grupo_18)
        d_block = VGroup(grupo_3,grupo_4,grupo_5,grupo_6,grupo_7,grupo_8,grupo_9,grupo_10,grupo_11,grupo_12 )
        f_block = VGroup(lantanidos,actinidos)


        periodic_table = VGroup(bloque_s, bloque_d, bloque_p, bloque_f)
        periodic_table.scale(0.38)
        periodic_table.shift(9*UP+13*LEFT)
        self.wait()
        self.play(Write(tabla_periodica), run_time = 5)
        self.wait()


