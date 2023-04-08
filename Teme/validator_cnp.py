cnp=input("Introduceti Codul Numeric Personal :")
S=cnp[0]
A1=cnp[1]
A2=cnp[2]
L1=cnp[3]
L2=cnp[4]
Z1=cnp[5]
Z2=cnp[6]
J1=cnp[7]
J2=cnp[8]
N1=cnp[9]
N2=cnp[10]
N3=cnp[11]
C=cnp[12]


if len(cnp) != 13:
    print("Codul Numeric Personal introdus nu este valid !")

elif not cnp.isdigit():
    print("Codul Numeric Personal nu contine DOAR cifre !")
else:
    cod_control=int(S)*2+int(A1)*2+int(A2)*int(L1)*1+int(L2)*4+int(Z1)*6+int(Z2)*3+int(J1)*5+int(J2)*8+int(N1)*2+int(N2)*7+int(N3)*9
    rest=cod_control%11
    if rest ==10:
        rest=1
    if rest != int(C):
        print("Codul Numeric Personal este valid !")
    else:
        print("Codul Numeric Personal NU este valid !")


