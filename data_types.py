def boolean():
    """
    Question 1 - Boolean

    Using the variable below, give it the value 'True', then print it.
    """
    # enter your code here
    staying_alive = True
    print(staying_alive)


def integer():
    """
    Question 2 - Integer

    Create a program to accept two numbers from a user and multiply them, then print the product.
    """

    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))
    y =num1*num2
    x = "The product is {}"
    print(x.format(y))

    # enter your code here


def string():
    """
    Question 3 - String

    Assign a name to the variable below and print it.
    """

    # enter your code here

    your_name = "Precious" 
    print(your_name)


def convert_to_float():
    """
    Question 4 - Float

    Convert the following integer to a float then print it.
    """

    int_num = (60)
    int_num = float(int_num)
    print(int_num)

    #enter your code here


def all_data_types():
    """
    Question 5 - All Data Types

    Output the following sentence using the given variables.

    Welcome to the 2023 WeThinkCode_ bootcamp where True learning costs R0.00
    """

    string_one = "Welcome to the "
    string_two = " WeThinkCode_ bootcamp where "
    string_3 = " learning costs R"
    bool_condition = True
    int_year = 2023
    float_cost = 0.00
  
    print(string_one + str(int_year) + string_two + str(bool_condition) + string_3 + '{:.2f}'.format(float_cost))
  

#'Welcome to the 2023 WeThinkCode_ bootcamp where  True learning costs R 0.00
# Welcome to the 2023 WeThinkCode_ bootcamp where True learning costs R0.00")
    #enter your code here '{:.2f}' format.(float_cost)


if __name__ == "__main__":
    """
    Run the entire program from here
    """
    print()

    # boolean()
    boolean()
    # integer()
    integer()
    # string()
    string()
    # convert_to_float()
    convert_to_float()
    # all_data_types()
    all_data_types()
