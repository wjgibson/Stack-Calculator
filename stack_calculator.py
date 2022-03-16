import unittest


class OverflowException( Exception): pass
class UnderflowException( Exception): pass

class Stack:
    """
    :var array: the array storing the values.
    :vartype array: list
    :ivar top: the index of the element that is currently at the top of the stack. 
    :vartype top: int
    """

    def __init__(self, size=100):
        """ Initialize a new Stack object.

        :param size: stack capacity (optional, default: 100)
        :type size: int
        """
        self.array = [None]*size
        self.top = -1

    def is_empty(self):
        """ 
        Test whether the stack is empty.

        :return: True if the stack is empty; False otherwise
        :rtype: bool
        """
        return self.top < 0


    def push(self, key):
        """ Insert a key at the top.

        :param key: the key value
        :type key: int or str
        """

        if self.top == len(self.array)-1:
            raise OverflowException()
        
        self.top += 1
        self.array[ self.top ] = key


    def pop(self):
        """ Retrieve last element from the top

        :return: a key value
        :rtype: int or str
        """
        if self.is_empty():
            raise UnderflowException()
        self.top -= 1
        return self.array[ self.top+1 ]

    def __str__(self):
        """ Console-friendly representation of the stack.

        :return: the list of active elements
        :rtype: str
        """
        return str(self.array[:self.top+1])

def evaluate(expr):
    """ Evaluate an arithmetical expression.

    :param expr: a list of numerical operands and operators, in prefix notation.
    :type expr: tuple
    :return: the numerical value of the expression
    :rtype: float or int
    """
    stack = Stack()
    
    for item in reversed( expr ):
        if isinstance( item, ( int, float ) ):
            stack.push( item )

        if isinstance(item,str):
            if item == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op1+op2
                stack.push( result )

            if item == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op1-op2
                stack.push( result )

            if item == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op1/op2
                stack.push( result )

            if item == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                result = op1*op2
                stack.push( result )

    return stack.pop()

class TestCalculator( unittest.TestCase ):

    def test_addition( self ):
        expr = ('+',14,2)
        self.assertEqual( evaluate(expr), 16)

    def test_multiplication( self ):
        expr = ('*',14,2)
        self.assertEqual( evaluate(expr), 28)

    def test_subtraction( self ):
        expr = ('-',14,2)
        self.assertEqual( evaluate(expr), 12)

    def test_division( self ):
        expr = ('/',14,2)
        self.assertEqual( evaluate(expr), 7)

    def test_expression_1( self ):
        expr = ('/','*',3,56, '+', 14, 2)
        self.assertEqual( evaluate(expr), 10.5)

    def test_expression_2(self):
        expr= ('-','/','*',3,56,'+',14,2,5)
        self.assertEqual( evaluate(expr), 5.5)




def main():
    unittest.main()

if __name__ == '__main__':
    main()

