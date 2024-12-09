from datetime import datetime

def calculate_days_between(date1, date2):
    date1_obj = datetime.strptime(date1, "%Y-%m-%d")
    date2_obj = datetime.strptime(date2, "%Y-%m-%d")

    diff = date2_obj - date1_obj

    return diff.days


if __name__ == "__main__":
    #格式为YYYY-MM-DD
    date1 = input()
    date2 = input()
    print(calculate_days_between(date1, date2))
