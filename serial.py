"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0): 
        """
        Make a new generator, starting at start. 

        ----------------------------

        We set the values for our start number and the one we will keep iterating from
        """ 
        self.start = start 
        self.next = start 

    def __repr__(self): 
        """Show Representation""" 
        return f"SerialGenerator start={self.start} next={self.next}"

    def generate(self): 
        """return next iteration""" 

        self.next += 1 
        return self.next - 1 

    def reset(self):
        """reset number to original start"""

        self.next = self.start