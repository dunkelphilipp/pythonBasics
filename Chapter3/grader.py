A_score = 90
B_score = 80
C_score = 70
D_score = 60

score = int(input("Enter your score: "))

match score:
    case score if score >= A_score:
        print("A")
    case score if score >= B_score:
        print("B")
    case score if score >= C_score:
        print("C")
    case score if score >= D_score:
        print("D")
    case _:
        print("Invalid score")