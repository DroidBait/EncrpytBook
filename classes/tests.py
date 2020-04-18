from dimension import tuplexy

def testSetXY():
    data = tuplexy(2, 3)
    assert data.getx() == 2
    assert data.gety() == 3

def testGetXY():
    data = tuplexy(5, 5)
    data.setx(7)
    data.sety(8)
    assert data.getx() == 7
    assert data.gety() == 8

def test25():
    data = tuplexy(8,4)
    assert data.getx25() == 2
    assert data.getx75() == 6
    data.setx(10)
    assert data.getx25() == 2
    assert data.getx75() == 7