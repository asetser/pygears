"""Provides rendering transforms.

The transforms provided by this module, such as Translation,
are implemented as Decorators (Gang of Four Decorators, not
Python decorators) which implement the same interface as the
objects they wrap. In other words, you can wrap a primitive,
such as a Triangle, with a Translation, and code that only
knows how to call render() will correctly render a translated
triangle.

By using the decorator pattern, we can create classes with
render() methods that draw objects (such as those in
gears.draw.primitives) independently of the transformations
on those objects, such as Translation, Rotation, and Scale.

"""
from OpenGL import GL
import math

class SkewX(object):
    """Decorator wrapping a node to skew it on the X-axis."""
    def __init__(self, node, degree):
        """Initializes a SkewX to skew node by degree.

        :node: any object with a render() method
        :degree: amount of x-axis skew

        """
        self._node = node
        self._degree = degree
        
    
    def render(self):
        """Renders the wrapped node skewed on the y-axis by the given degree."""
        #Push Identity matrix
        GL.glPushMatrix()
        #Multiply by the x-axis skew transformation matrix
        GL.glMultMatrixf([1,0,0,0, math.tan(self._degree),1,0,0, 0,0,1,0, 0,0,0,1])
        #Preceed with rendering
        self._node.render()
        #remove transform matrix
        GL.glPopMatrix()

class SkewY(object):
    """Decorator wrapping a node to skew it on the Y-axis."""
    def __init__(self, node, degree):
        """Initializes a SkewY to skew node by degree.

        :node: any object with a render() method
        :degree: amount of y-axis skew

        """
        self._node = node
        self._degree = degree
    
    def render(self):
        """Renders the wrapped node skewed on the y-axis by the given degree."""
        #Push Identity matrix
        GL.glPushMatrix()
        #Multiply by the x-axis skew transformation matrix
        GL.glMultMatrixf([1,math.tan(self._degree),0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1])
        #Preceed with rendering
        self._node.render()
        #remove transform matrix
        GL.glPopMatrix()
        
class Translation(object):
    """Decorator wrapping a node to translate it across the screen."""
    def __init__(self, node, x, y):
        """Initializes a Translation to translate node to (x,y).

        :node: any object with a render() method
        :x: x-axis offset
        :y: y-axis offset

        """
        self._node = node
        self._x = x
        self._y = y

    def render(self):
        """Renders the wrapped node translated to the given offset."""
        # glPushMatrix loads an identity matrix into OpenGL...
        GL.glPushMatrix()
        # Then we do some matrix math to translate our object...
        GL.glTranslatef(self._x, self._y, 0)
        # render the underlying node (which could be anything)...
        self._node.render()
        # And 'pop' our matrix off of the stack so we don't mess
        # with future rendering calls
        GL.glPopMatrix()

class Rotation(object):
    """Decorator wrapping a node to rotate it about the origin."""
    def __init__(self, node, theta):
        """Initializes a Rotation to rotate node anti-clockwise
        through angle theta
        
        :node: any object with a render() method
        :theta: the angle to rotate through, in radians
        
        """
        self._node = node
        self._theta = theta
    
    def render(self):
        """Renders the wrapped node rotated through the given
        angle theta, in radians"""
        GL.glPushMatrix()
        GL.glRotatef(self._theta * 180 / pi, 0, 0, 1)
        self._node.render()
        GL.glPopMatrix()

class Scaling(object):
    """Decorator wrapping a node to scale it with respect to the origin
    
    Note: I would have called this class Homothety, but that
    just seems a bit _too_ pretentious. :)"""
    def __init__(self, node, factor):
        """Initializes a Scaling to scale the node by the given factor"""
        self._node = node
        self._factor = factor
    
    def render(self):
        """Renders the wrapped node scaled by the given factor
        with respect to the origin"""
        GL.glPushMatrix()
        #pdb.set_trace()
        GL.glScalef(self._factor, self._factor, 1.0)
        self._node.render()
        GL.glPopMatrix()
