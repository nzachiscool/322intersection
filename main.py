def get_orientation(p1,p2,p3):
    ori = (p2[1]-p1[1])*(p3[0]-p2[0])-(p3[1]-p2[1])*(p2[0]-p1[0])
    if ori == 0:
        return  0 #"Collinear"
    elif ori > 0:
        return 1 #'Clockwise'
    else :
        return 2 #"Counter-clockwise"
    

def on_segment(p,q,r):

    if not get_orientation(p,q,r) == 0: # if not colinear, then q is not on pr
        return False
    else:
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))


def do_segments_intersect(seg1, seg2):
    # find the four orientations needed
    # for general and special cases
    o1 = get_orientation(seg1[0], seg1[1], seg2[0])
    o2 = get_orientation(seg1[0], seg1[1], seg2[1])
    o3 = get_orientation(seg2[0], seg2[1], seg1[0])
    o4 = get_orientation(seg2[0], seg2[1], seg1[1])

    # general case
    if o1 != o2 and o3 != o4:
        return True

    # special cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if on_segment(seg1[0], seg2[0], seg1[1]):
        return True

    if on_segment(seg1[0], seg2[1], seg1[1]):
        return True

    if on_segment(seg2[0], seg1[0], seg2[1]):
        return True

    if on_segment(seg2[0], seg1[1], seg2[1]):
        return True

    return False

    

if __name__ == "__main__":
    p1 = (1.0, 1.0)
    p2 = (4.0, 4.0)
    p3 = (2.0, 4.0)
    p4 = (4.0, 2.0)
    seg1 = (p1, p2)
    seg2 = (p3, p4)
    print(do_segments_intersect(seg1, seg2)) # Output: True
