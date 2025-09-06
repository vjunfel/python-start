def format_name(f_name, l_name):
    return f"{f_name} {l_name}".title()


result = format_name("junfel", "velasco")
# print(result)


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return True
    elif year % 4 == 0:
        return True
    elif year == 2100 or year == 1700:
        return False
    else:
        return False
        
        
output = is_leap_year(2020)
print(output)