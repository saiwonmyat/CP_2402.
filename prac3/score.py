def caculate_score(score):
    if score <= 0:
        mark = ("Invalid score")
    elif score >= 100:
        mark = ("Invalid score")
    elif score >= 90:
        mark = ("Excellent")
    elif score >= 50:
        mark = ("Passable")
    else:
        mark = ("Bad")
    return (mark)

def main():
    putscore = int(input("Enter the user score: "))
    ans = caculate_score(putscore)
    print(ans)
main()