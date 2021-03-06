"""
This file contains the classes for the data structures
that store one's interests in swapping courses


It has classes Want, Have and Pair. Pair uses the last two
to store pairs of what someone would.


"""

class Desire:
    def __init__(self, name_of_class, int_enrol_waitlisted):
        assert( type(name_of_class)== str and type(int_enrol_waitlisted)==int)
        
        self.name = name_of_class
        self.position = int_enrol_waitlisted # 0 if enrolled, otherwise
        #it is position on waitlist

    def __repr__(self):
        return "({name}, {position})".format(**self.__dict__)

    def __eq__(self, other):
      return self.name == other.name and self.position == other.position
    

class Have(Desire):
    def __init__(self, name_of_class, int_enrol_waitlisted):
        Desire.__init__(self, name_of_class, int_enrol_waitlisted)

class Want(Desire):
    def __init__(self, name_of_class, int_enrol_waitlisted):
        Desire.__init__(self, name_of_class, int_enrol_waitlisted)
        # you give the lowest waitlist postition you would be happy to
        #trade for




class Pair:

    def __init__(self, have, want, int_identity):

        assert(type(have)== Have and type(want)== Want)
        assert (type(int_identity) == int)
        self.have = have
        self.want = want
        self.id = int_identity

    def __hash__(self):
        return hash(str(self.id) + self.have.name + str(self.have.position) + self.want.name + str(self.want.position))

    def __eq__(self, other):
        if type(other) != Pair:
            raise TypeError()
        return self.id == other.id and self.have == other.have and self.want == other.want

    def __repr__(self):
        return "{id} has {have} and wants {want}".format(**self.__dict__)



    def satisfies(self, other):
        """
        Asking whether self --> other
        in the loop we are trying to build

        so it returns a bool
        """
        assert type(other) == Pair

        return self.want.name == other.have.name and \
            other.have.position <= self.have.position


    def get_want(self):return self.want
    def get_have(self):return self.have
    def get_id(self):return self.id

    
 
        
