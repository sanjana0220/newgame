class CustomError(Exception):
    def handle_index_error(index):
        print("The index", index,  "is incorrect and index should lie between -5 and 4.")

    def handle_value_error(index):
        print("Use an Integer value as the input.")
list_a = [1, 2, 3, 4, 5]
index= input("Enter the index =")
try:
    index= int(index)
    print(list_a[(index)])
except IndexError:

    CustomError.handle_index_error(index)

except ValueError:
    CustomError.handle_value_error(index)


