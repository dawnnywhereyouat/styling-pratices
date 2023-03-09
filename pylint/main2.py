"""sadasdasd

Returns:
    _type_: _description_
"""

class MyClass:
    """
        Yo what
        Is upo
    """
    def __init__(self, fullname, SpecialCase=None): # pylint: disable=invalid-name
        self.fullname = fullname
        self.specialCase = SpecialCase  # pylint: disable=invalid-name

    def get_full_name(self):
        """
        Hello
        You
        """
        return self.fullname

    @staticmethod
    def haha():
        """
        Hello
        """
        return 'haha'

a= MyClass(fullname= 'ABC')
print(a.get_full_name())
