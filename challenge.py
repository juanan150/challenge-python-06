def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def division_n(x):
        return x/n
    
    return division_n


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def test_closure_make_division_by(self):

            self.assertEqual(5, make_division_by(3)(15))

            self.assertEqual(8, make_division_by(5)(40))

            self.assertEqual(9, make_division_by(18)(162))


    #unittest.main()
    run()
