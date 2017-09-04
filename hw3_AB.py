import sys

def month_to_string(month_num):
    # TODO: write month return logic here
    month_name = ["0","January","February","March","April","May","June","July","August","September","October","November","December"]
    return month_name[month_num]

def main():
    # TODO: write user input gathering and function call here
    month_num = input("Enter a month number between 1 and 12\n")
    month_num = int(month_num)
    if month_num >=1 and month_num <=12:
        print("Month #",month_num,"is",month_to_string(month_num))
    else: print("Try again")

if __name__ == "__main__": main()
