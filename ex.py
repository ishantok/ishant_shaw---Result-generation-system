def Calculation(marks):
    if marks >= 90 and marks <= 100:
        Grade = 'O'
        Point = 10

    elif marks >= 80 and marks <= 89:
        Grade = 'E'
        Point = 9

    elif marks >= 70 and marks <= 79:
        Grade = 'A'
        Point = 8

    elif marks >= 60 and marks <= 69:
        Grade = 'B'
        Point = 7

    elif marks >= 50 and marks <= 59:
        Grade = 'C'
        Point = 6

    elif marks >= 40 and marks <= 49:
        Grade = 'D'
        Point = 5

    elif marks <= 40:
        Grade = 'F'
        Point = 2

    else:
        Grade = 'I'
        Point = 2

    print('Grade: ', Grade)
    print('Point: ', Point)
    return Point


def CreditPoints(credit, point):
    return credit * point


def CA():
    CA1 = int(input('Marks in CA1: '))
    CA2 = int(input('Marks in CA2: '))
    CA3 = int(input('Marks in CA3: '))
    CA4 = int(input('Marks in CA4: '))
    ca = [CA1, CA2, CA3, CA4]
    return max(ca)


def PCA():
    PCA1 = int(input('Marks in PCA1: '))
    PCA2 = int(input('Marks in PCA2: '))
    pca = [PCA1, PCA2]
    return max(pca)


def Physics():
    print('Physics')

    P = CA()
    print('Highest CA marks of Physics: ', P)

    Pp = PCA()
    print('Highest PCA marks of Physics: ', Pp)

    Pa = int(input('Enter marks out of 5 for attendance: '))

    Ps = int(input('Enter Physics marks out of 70 for Semester: '))

    Pps = int(input('Enter marks obtained in semester practical exam out of 60: '))
    print('Physics theory marks: ', P + Pa + Ps)
    print('Physics practical marks: ', Pp + Pps)

    print('Grade for Physics Theory exam:')
    Point_Physics = Calculation(P + Pa + Ps)
    print('Grade for Physics Practical exam:')
    Point_Physics_Practical = Calculation(Pp + Pps)

    credit_Physics = 4.0
    Credit_Point_Physics = CreditPoints(credit_Physics, Point_Physics)
    print('Credit Point: ', Credit_Point_Physics)

    credit_Physics_Practical = 1.5
    Credit_Point_Physics_Practical = CreditPoints(credit_Physics_Practical, Point_Physics_Practical)
    print('Credit Point: ', Credit_Point_Physics_Practical)


def PPS():
    print('PPS')

    pps = CA()
    print('Highest CA marks of PPS: ', PPS)

    PPSp = PCA()
    print('Highest PCA marks of PPS: ', PPSp)

    PPSa = int(input('Enter marks out of 5 for attendance: '))

    PPSs = int(input('Enter PPS marks out of 70 for Semester: '))

    PPSps = int(input('Enter marks obtained in semester practical exam out of 60: '))
    print('PPS theory marks: ', pps + PPSa + PPSs)
    print('PPS practical marks: ', PPSp + PPSps)

    print('Grade for PPS Theory exam:')
    Point_PPS = Calculation(pps + PPSa + PPSs)
    print('Grade for PPS Practical exam:')
    Point_PPS_Practical = Calculation(PPSp + PPSps)

    credit_PPS = 3.0
    Credit_Point_PPS = CreditPoints(credit_PPS, Point_PPS)
    print('Credit Point: ', Credit_Point_PPS)

    credit_PPS_Practical = 2.0
    Credit_Point_PPS_Practical = CreditPoints(credit_PPS_Practical, Point_PPS_Practical)
    print('Credit Point: ', Credit_Point_PPS_Practical)


def English():
    print('Physics')

    E = CA()
    print('Highest CA marks of English: ', E)

    Ep = PCA()
    print('Highest PCA marks of English: ', Ep)

    Ea = int(input('Enter marks out of 5 for attendance: '))

    Es = int(input('Enter English marks out of 70 for Semester: '))

    Eps = int(input('Enter marks obtained in semester practical exam out of 60: '))
    print('English theory marks: ', E + Ea + Es)
    print('English practical marks: ', Ep + Eps)

    print('Grade for English Theory exam:')
    Point_English = Calculation(E + Ea + Es)
    print('Grade for English Practical exam:')
    Point_English_Practical = Calculation(Ep + Eps)

    credit_English = 2.0
    Credit_Point_English = CreditPoints(credit_English, Point_English)
    print('Credit Point: ', Credit_Point_English)

    credit_English_Practical = 1.0
    Credit_Point_English_Practical = CreditPoints(credit_English_Practical, Point_English_Practical)
    print('Credit Point: ', Credit_Point_English_Practical)


def Maths():
    print('Maths')
    M = CA()
    print('Highest CA marks of Maths: ', M)

    Ma = int(input('Enter marks out of 5 for attendance: '))

    Ms = int(input('Enter Maths marks out of 70 for Semester: '))

    Point_Maths = Calculation(M + Ma + Ms)

    print('Maths theory marks: ', M + Ma + Ms)

    credit_Maths = 4.0
    Credit_Point_Maths = CreditPoints(credit_Maths, Point_Maths)
    print('Credit Point: ', Credit_Point_Maths)


def BEE():
    print('BEE')
    B = CA()
    print('Highest CA marks of BEE: ', B)

    Bp = PCA()
    print('Highest PCA marks of Bee: ', Bp)

    Ba = int(input('Enter marks out of 5 for attendance: '))

    Bs = int(input('Enter BEE marks out of 70 for Semester: '))

    Bps = int(input('Enter marks obtained in semester practical exam out of 60: '))

    Point_BEE = Calculation(B + Ba + Bs)
    Point_BEE_Practical = Calculation(Bp + Bps)

    print('BEE theory marks: ', B + Ba + Bs)
    print('BEE practical marks: ', Bp + Bps)

    credit_BEE = 4.0
    Credit_Point_BEE = CreditPoints(credit_BEE, Point_BEE)
    print('Credit Point: ', Credit_Point_BEE)

    credit_BEE_Practical = 1.0
    Credit_Point_BEE_Practical = CreditPoints(credit_BEE_Practical, Point_BEE_Practical)
    print('Credit Point: ', Credit_Point_BEE_Practical)


def Chem():
    print('Chem')

    C = CA()
    print('Highest CA marks of Chem: ', C)

    Cc = PCA()
    print('Highest PCA marks of Chem: ', Cc)

    Ca = int(input('Enter marks out of 5 for attendance: '))

    Cs = int(input('Enter Chem marks out of 70 for Semester: '))

    Ccs = int(input('Enter marks obtained in semester practical exam out of 60: '))
    print('Chem theory marks: ', C + Ca + Cs)
    print('Chem practical marks: ', Cc + Ccs)

    Point_Chem = Calculation(C + Ca + Cs)
    Point_Chem_Practical = Calculation(Cc + Ccs)

    credit_Chem = 4.0
    Credit_Point_Chem = CreditPoints(credit_Chem, Point_Chem)
    print('Credit Point: ', Credit_Point_Chem)

    credit_Chem_Practical = 1.5
    Credit_Point_Chem_Practical = CreditPoints(credit_Chem_Practical, Point_Chem_Practical)
    print('Credit Point: ', Credit_Point_Chem_Practical)


def Workshop():
    print('Workshop/Manufacturing Practices:')

    Wp = PCA()
    print('Highest PCA marks: ', Wp)

    Wps = int(input('Enter marks obtained in semester practical exam out of 60: '))

    print('Total marks: ', Wp + Wps)

    Point_Workshop_Practical = Calculation(Wp + Wps)

    credit_Workshop_Practical = 3.0
    Credit_Point_Workshop_Practical = CreditPoints(credit_Workshop_Practical, Point_Workshop_Practical)
    print('Credit Point: ', Credit_Point_Workshop_Practical)


def Graphics():
    print('Engineering Graphics:')

    Gp = PCA()
    print('Highest PCA marks: ', Gp)

    Gps = int(input('Enter marks obtained in semester practical exam out of 60: '))

    print('Total marks: ', Gp + Gps)

    Point_Graphics_Practical = Calculation(Gp + Gps)

    credit_Graphics_Practical = 3.0
    Credit_Point_Graphics_Practical = CreditPoints(credit_Graphics_Practical, Point_Graphics_Practical)
    print('Credit Point: ', Credit_Point_Graphics_Practical)


name = input('Enter name of student: ')
roll = int(input('Enter university roll of student: '))
sem = int(input('Enter semester: '))
dept = input('Enter department: ')

if dept == 'IT':

    if sem == 1:
        Physics()
        Maths()
        BEE()
        Workshop()

    if sem == 2:
        Chem()
        Maths()
        Graphics()
        PPS()
        English()

elif dept == 'CSE':

    if sem == 1:
        Physics()
        Maths()
        BEE()
        Workshop()

    if sem == 2:
        Chem()
        Maths()
        Graphics()
        PPS()
        English()

elif dept == 'AIML':

    if sem == 1:
        Physics()
        Maths()
        BEE()
        Workshop()

    if sem == 2:
        Chem()
        Maths()
        Graphics()
        PPS()
        English()

elif dept == 'ECE':

    if sem == 1:
        Chem()
        Maths()
        BEE()
        Graphics()

    if sem == 2:
        Physics()
        Maths()
        Workshop()
        PPS()
        English()

elif dept == 'EE':

    if sem == 1:
        Chem()
        Maths()
        BEE()
        Graphics()

    if sem == 2:
        Physics()
        Maths()
        Workshop()
        PPS()
        English()