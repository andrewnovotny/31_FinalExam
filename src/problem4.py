"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Andrew Novotny.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    oinker = Pig(200)
    print("Oinker's weight is", oinker.get_weight())
    oinker.eat(50)
    print("Oinker's weight after eating 50 lbs slop", oinker.get_weight())
    oinker.eat_for_a_year()
    print("Oinker's weight after eating for a year", oinker.get_weight())
    oinker2 = Pig(100)
    oinker3 = Pig(200)
    print("Oinker2's weight:", oinker2.get_weight())
    print("Oinker3's weight:", oinker3.get_weight())
    print("Should show Oinker3's weight:",oinker2.heavier_pig(oinker3).get_weight())
    print("Should show Oinker3's weight:", oinker3.heavier_pig(oinker2).get_weight())
    oinker4 = oinker2.new_pig(oinker)
    print("Oinker 4 should have the same weight as Oinker")
    print("Oinker's weight:", oinker.get_weight())
    print("Oinker4's weight:", oinker4.get_weight())


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.
        self.weight = weight

    def get_weight(self):
        """ Returns this Pig's weight. """
        # DONE: Implement and test this method.
        return self.weight

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DONE: Implement and test this method.

        #### I think this ratio is a little extreme, but I don't think it makes much of a difference
        #### The premise to the problem should be the same
        #### Only other thing that might be useful is increment by pounds eaten // some number, but this
        #### Meets the docstring so it should be fine

        self.weight += pounds_of_slop

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DONE: Implement and test this method.
        for k in range(365):
            self.eat(k+1)

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DONE: Implement and test this method.
        if self.get_weight() > other_pig.get_weight():
            return self
        else:
            return other_pig

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DONE: Implement and test this method.
        return Pig(self.heavier_pig(other_pig).get_weight())

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
