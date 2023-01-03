def testTriangle(a,b,c):
    
    triangle = [a, b, c]
    triangle.sort()

    if (triangle[2] < (triangle[0] + triangle[1]) ):
        
        if (triangle[2]**2 == (triangle[0]**2 + triangle[1]**2)):
            print("rectangle")

        if(len(set(triangle)) == 2):
            print("isocele")

        elif(len(set(triangle)) == 1):
            print("equilateral")
            
        else:
            print("quelconque")
        print("")

    else:
        print("impossible \n")



testTriangle(5,4,6)
testTriangle(5,4,3)
testTriangle(5,48,3)
testTriangle(1,2,3)
testTriangle(4,4,6)