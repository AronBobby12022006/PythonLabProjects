def is_right_triangle(side1,side2,side3):
    '''
    Function to check the right angle triangle
    :param side1:
    :param side2:
    :param side3:
    :return:True if the triangle is right angle or not,False:Otherwise
    '''
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False


side1=int(input("Enter side 1:"))
side2=int(input("Enter side 2:"))
side3=int(input("Enter side3 3:"))
if is_right_triangle(side1,side2, side3):
    print("Its a right triangle")
else:
    print("Its not a right triangle")




