class Shape:

    cat = 'Geometrical'

    def __init__(self, type):
        # instance variable
        self.typ = type


    def show(self):
        # accessing class variable
        print('Shape is of category: ', Shape.cat)

        print('And shape is: ', self.type)


tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')

tr.show()
sq.show()
rec.show()