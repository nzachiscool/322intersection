def Orientation(p1,p2,p3):
    ori = (p2[1]-p1[1])*(p3[0]-p2[0])-(p3[1]-p2[1])*(p2[0]-p1[0])
    if ori == 0:
        return "Collinear"
    elif ori > 0:
        return 'Clockwise'
    else :
        return "Counter-clockwise"


if __name__ == "__main__":
    p1 = (1,1)
    p2 = (3,3)
    p3 = (4,5)
    print(Orientation(p1,p2,p3))
