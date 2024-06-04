import math


class Point:
    '''Stores Cartesian point on 2D plane'''
    __counter = 0
    def __init__(self, x, y):
        '''Constructor'''
        Point.__counter += 1
        self.x_ = x
        self.y_ = y

    def __del__(self):
        '''Destructor'''
        Point.__counter -= 1

    def __str__(self):
        '''String representation'''
        return f'class representation: x={self.x_} and y={self.y_}. wow'
    
    def __repr__(self):
        '''Representation'''
        return f'classic class representation: x={self.x_} and y={self.y_}. wow'

    @property
    def x(self):
        #print('[trace]: x_getter() called')
        return self.x_

    @x.setter
    def x(self, new_x):
        #print('[trace]: x_setter() called')
        self.x_ = new_x
  
    @property
    def y(self):
        #print('[trace]: y_getter() called')
        return self.y_
  
    @y.setter
    def y(self, new_y):
        #print('[trace]: y_setter() called')
        self.y_ = new_y
  
    def translate_by_x(self, x_value):
        '''Translate x coordinate of point'''
        self.x_ += x_value

    def translate_by_y(self, y_value):
        '''Translate y coordinate of point'''
        self.y_ += y_value

    def get_distance_to_center(self):
        '''Return distance to center'''
        return ((self.x_)**2 + (self.y_)**2)**0.5

    def get_distance_to_point(self, another_point):
        '''Return distance between this point and another'''
        return ( (another_point.x_ - self.x_)**2 + (another_point.y_ - self.y_)**2 )**0.5

    def convert_to_polar_form(self):
        '''Converts coordinates from Cartesian to Polar form'''
        return {
            'r': ((self.x_)**2 + (self.y_)**2)**0.5,
            'theta': math.atan(self.y_ / self.x_)
        }

    #   ===============================
    #   Comparison operators overloading
    #   ===============================

    def __eq__(self, other):
        '''Operator: Equal'''
        if (self.x_ == other.x_) and (self.y_ == other.y_):
            return True
        else:
            return False

    def __ne__(self, other):
        '''Operator: Non-equal'''
        if (self.x_ != other.x_) or (self.y_ != other.y_):
            return True
        else:
            return False

    #   ===============================
    #   Arithmetic operators overloading
    #   ===============================

    def __add__(self, other):
        '''Binary Operator: Addition'''
        return Point(self.x_ + other.x_, self.y_ + other.y_)

    def __mul__(self, other):
        '''Binary Operator: Multiplication'''
        return Point(self.x_ * other.x_, self.y_ * other.y_)

    @classmethod
    def get_class_instances(self):
        '''Return all constructed and not-destructed instances of this class'''
        return Point.__counter
