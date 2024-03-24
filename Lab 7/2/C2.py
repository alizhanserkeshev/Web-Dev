sys_answer = int(input())
stu_answer = int(input())

if stu_answer != 1:
    if sys_answer == 1:
        print("NO")
    else:
        print("YES")
else:
    if sys_answer != 1:
        print("NO")
    else:
        print("YES")