def calculate_percentage(percentage):
    calculate_percentage=obtain/total
    return  calculate_percentage





def grade(sub1,sub2,sub3):
    obtain=sub1+sub2+sub3
    total=300
    return calculate_percentage (obtain,total)
    if calculate_percentage >=85:
        return "A+"
    elif calculate_percentage >=75:
        return "A"
    elif calculate_percentage >=65:
        return "B+"
    else :
        return "B"


grades=grade(int(input("enter your marks")))
print(grades)





