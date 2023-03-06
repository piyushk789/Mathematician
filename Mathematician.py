# Math Solution ```python````
# Author: Kartikey Baghel
# Country: India
# github: https://github.com/piyushk789


class Simple:

    __all__ = [
        'adding', 'subtraction', 'division', 'multiplication',
        'average', 'questioner', 'power', 'table_of',
        'is_prime', 'sqrt', 'cub_rt'
    ]

    def __init__(self) -> None:
        """
        # Simple Math function
        which take numbers in function and return the result some examples of function:
        >>> from Mathematician import Simple
        >>> mod = Simple()
        >>> print(mod.adding(4,6))
        10.0
        >>> print(mod.adding(1,6,13,65))
        85.0
        >>> print(mod.division(100,10))
        10.0
        >>> print(mod.division(100, 5, 2))
        10.0
        >>> print(mod.multiplication(4,6))
        24.0
        >>> print(mod.multiplication(1,6,13,65))
        1365.0
        >>> print(mod.subtraction(4,6))
        -2.0

        and so on ... """

    def adding(self,a, b, *arg) -> float:
        k = a+b if type(a) == int or type(a) == float and type(b) == int or type(b) == float else "Input Argument must be Integer or Float"
        if arg:
            for n in arg: k = k+n
        return float(k)

    def subtraction(self, a, b, *arg) -> float:
        k = a-b
        if arg:
            for n in arg: k = k-n
        return float(k)
    
    def division(self, a, b, *arg) -> float:
        k = a/b
        if arg:
            for n in arg: k = k/n
        return float(k)

    def average(self, a, b, *arg) -> float:
        k = a+b
        if arg:
            for n in arg: k = k+n
            avg = len(arg)+2
            return k/avg
        else: return k/2

    def multiplication(self, a, b, *arg) -> float:
        k = a * b
        if arg:
            for n in arg: k = k*n
        return float(k)

    def questioner(self, *b:list[int]) -> list:
        k = []
        if b:
            for n in b:
                k.append(float(n[0]//n[1])) if len(n) == 2 else k.append('Only Two argument can support')
        return k

    def power(self, *b:list[int and float]) -> list:
        """
        # Insert two value in a list:
        as like a list [a,b], 'a' have power | 'b' is power
        the result will return a list -> [32.0]
        >>> mod = Simple()
        >>> mod.power([5,5])
        [3125.0]
        >>> mod.power([2,3], [6,8])
        [8.0, 1679616.0]
        """
        k = []
        if b:
            for n in b: k.append(float(n[0]**n[1])) if len(n) == 2 else k.append('Only Two argument can support')
        return k

    def table_of(self, num:int, fr:int=1, to:int=10) -> list:
        """
        # Simple number table will return
        Get table of number in a list, it's simple easy

        enter a value in\n
        parameter => num # for the table\n
        parameter => fr # starts from\n
        parameter => to # ends to\n

        simple Examples of the module:

        >>> mod = Simple()
        >>> print(mod.table_of(num=5))
        [5,10,15,20,25,30,35,40,45,50]

        >>> print(mod.table_of(num=5,fr=20, to=25))
        [100,105,110,115,120,125]

        >>> print(mod.table_of(num=5, to=20))
        [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
        """
        if num < 1: return []
        else: return [i*num for i in range(fr, to+1)]

    def is_prime(self, num:int) -> bool:
        """
        # Is it Prime?
        if the value is Prime -> it's True\n
        else the function -> return False
        
        >>> mod = Simple()
        >>> print(mod.is_prime(5))
        True
        >>> print(mod.is_prime(4))
        False
        """
        if num>1:
            for i in range(2, int(num/2)+1):
                if num%i==0: return False
            else: return True
        else: return True

    def sqrt(self, n:int and float=0, l:list=[]):
        """
        # Find the Square root of...
        
        It's Simple to use the function\n
        parameter = n[int or float] # for getting single number\n
        parameter = l[list] # for getting multiple of square roots\n\n

        # A example for explain it:
        >>> mod = Simple()
        >>> print(mod.sqrt(25))
        5.0\n
        for multiple roots
        >>> print(mod.sqrt(0, [121, 25, 12321, 100, 625, 64]))
        [11.0, 5.0, 111.0, 10.0, 25.0, 8.0]\n
        """
        if n>0: return n**.5
        elif l: return [self.sqrt(num) for num in l]
        else: return 0.0

    def cub_rt(self, n:int):
        """
        # Returns cube root of...
        
        Insert the value in parameter = n\n
        and get the value of root

        for example:
        >>> mod = Simple()
        >>> print(mod.cub_rt(8))
        2
        >>> print(mod.cub_rt(64))
        4

        # loop of the Method

        l = []\n
        ls = [64, 125, 12321, 100, 729]
        >>> for i in ls:
        ...     l.append(mod.cub_rt(i))
        >>> print(l)
        [4, 5, 24.593459580877163, 4.786300923226384, 9]
        """
        if n>0:
            for i in range(1, int(n/3)+1): 
                if int(i*i*i) == n: return i
            else: return n**.34
        else: return 0


class Geometry(Simple):

    __all__ = [
        'pythagorean', 'two_point_distance', 'midpoint'
    ]

    def pythagorean(self, h:int and float=0, p:int and float=0, b:int and float=0):
        """
        # Pythagorean Formula
        It is a simple and very useful formula in our daily life.
        as a Mathematician student, we use it very much.

        Some parameters in the pythagorean function are:
        h =-> Hypotenuse
        p =-> Perpendicular
        b =-> Base

        # Pythagorean Formula works

        >>> from Mathematician import Geometry
        >>> mod = Geometry()
        #-------------------------------------#
            # To find Base
        >>> print(mod.pythagorean(h=5, p=3))
        4.0
        #-------------------------------------#
            # To find Hypotenuse
        >>> print(mod.pythagorean(p=3, b=4))
        5.0
        #-------------------------------------#
            # To find Perpendicular
        >>> print(mod.pythagorean(h=5, b=4))
        3.0
        #-------------------------------------#

        """
        if h==0: return self.sqrt((p**2)+(b**2))
        elif p==0: return -(((b**2)-(h**2))**.5) if (h**2)-(b**2) <0 else self.sqrt((h**2)-(b**2))
        elif b==0: return -(((p**2)-(h**2))**.5) if (h**2)-(p**2) <0 else self.sqrt((h**2)-(p**2))
        elif h>0 and p>0 and b>0: return (((p**2)+(b**2))/h**2)
        else: return 0

    def two_point_distance(self, a:tuple=(1,1), b:tuple=(1,1)):
        """
        # Two Point Distance
        ### Distance Btw Two-points
        
        In the Math, We study most of the formula,
        the Distance Between two-points

        To find the distance we have two values: A and B\n
        the formula of two point distance is used by the value

        the Parameter in the function is taking to tuples.

        A = tuple() & B = tuple()\n
        the tuple takes only two arguments.
        
        Now check the function, How it's work?

        >>> geo = Geometry()
        >>> print(geo.two_point_distance(a=(8,2), b=(4,-1)))
        5.0
        >>> print(geo.two_point_distance(a=(2,4), b=(6,4)))
        4.0

        """
        p = self.power([(a[0]-b[0]),2],[(a[1]-b[1]),2])
        return self.sqrt((p[0]+p[1]))

    def midpoint(self, x:tuple=(1,1), y:tuple=(1,1)):
        """
        # Midpoint
        ### Find midpoint

        the function have two parameters, takes two value\n
        in the parameter: x = (x1, y1)
        in the parameter: y = (x2, y2)

        for example:
        
        >>> geo = Geometry()
        >>> print(geo.midpoint(x=(2,6), y=(4,-2)))
        (3.0, 2.0)
        >>> print(geo.midpoint(x=(8,4), y=(2,10)))
        (5.0, 7.0)

        """
        return ((x[0]+y[0])/2,(x[1]+y[1])/2)


class Area:

    __all__ = [
        'square', 'rectangle', 'triangle', 'rhombus',
        'trapezoid', 'regularPolygon', 'circle', 'cone', 'sphere'
        ]

    def square(self, side:int or float) -> float: return side*side

    def rectangle(self, weight:int or float, height:int or float): return weight*height

    def triangle(self, base:int or float, height:int or float): return (base*height)/2

    def rhombus(self, largeD:int or float, smallD:int or float): return (largeD*smallD)/2

    def trapezoid(self, largeSide:int or float, smallSize:int or float, height:int or float): return ((largeSide+smallSize)/2)*height

    def regularPolygon(self, perimeter:int or float, apothem:int or float): return (perimeter/2)*apothem

    def circle(self, radius:int or float): return (22/7)*(radius*radius)

    def cone(self, radius:int or float, slant_height:int or float): return (22/7)*radius*slant_height

    def sphere(self, radius:int or float): return 4*(22/7)*(radius*radius)


class Volume:

    __all__ = ['cube', 'parallelepiped', 'regularPrism',
               'cylinder', 'cone_pyramid', 'sphere']

    def cube(self, side:int or float): return side*side*side

    def parallelepiped(self, length:int or float, width:int or float, height:int or float): return length*width*height

    def regularPrism(self, base:int or float, height:int or float): return  base*height

    def cylinder(self, radius:int or float, height:int or float): return (22/7)*(radius*radius)*height

    def cone_pyramid(self, base:int or float, height:int or float): return (1/3)*base*height

    def sphere(self, radius:int or float): return (4/3)*(22/7)*(radius**3)


class exponents:

    __all__ = ['product', 'quotient', 'PoP', 'fractional']

    def product(self,a:int, b:int=0, pw:list=[1,1]):
        if b==0 or a==b and pw[0] != pw[1]: return a**(pw[0]+pw[1])
        elif a==b and pw[0] == pw[1]: return a**(pw[0]+pw[1])
        elif a!=b and pw[0] != pw[1]: return (a**pw[0])*(b**pw[1])
        else: return (a**pw[0])*(b**pw[0])

    def quotient(self,a:int, b:int=0, pw:list=[1,1]):
        if b==0 or a==b and pw[0] != pw[1]: return a**(pw[0]-pw[1])
        elif a==b and pw[0] == pw[1]: return a**(pw[0]-pw[1])
        elif a!=b and pw[0] != pw[1]: return (a**pw[0])/(b**pw[1])
        else: return (a**pw[0])/(b**pw[0])

    def PoP(self, a:int, p:int, P:int): return a*p*P

    def fractional(self, a:int, pw:list=[1,1]):
        if a**pw[0]>0:
            for i in range(1, int(a**pw[0]/2)):
                if i**pw[1] == (a**pw[0]): return i
            else: return (a**pw[0])**(1/pw[1])
        else: return 0
