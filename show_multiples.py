

def show_multiples_3_5():
    """Prints numbers from 1 to 100; replacing multiples of 3, 5 and 15 by 'Three', 'Five', 'ThreeFive' respectively"""

    # For loop to iterate through numbers 1 to 100
    for i in range(1, 101):

        # If i is multiples of 15; print "ThreeFive"
        if i % 15 == 0:
            print("ThreeFive")

        # If i is multiples of 3; print "Three"
        elif i % 3 == 0:
            print("Three")

        # If i is multiples of 5; print "Five"
        elif i % 5 == 0:
            print("Five")

        # Else print the number i itself
        else:
            print(i)


if __name__ == "__main__":
    show_multiples_3_5()