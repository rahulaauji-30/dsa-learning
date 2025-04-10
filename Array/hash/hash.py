hash_set = [None] * 10

def hash_fn(value)->int:
    sum_of_characters = 0
    for char in value:
        sum_of_characters+= ord(char)
    return sum_of_characters % 10

if __name__ == "__main__":
    while True:
        choice = int(input("1.Insert\n2.Search\n3.Delete\n4.Display\nEnter yourc choice:- "))
        if choice == 1:
            value = input("Enter the element to be stored: ")
            index = hash_fn(value)
            hash_set[index] = value
        elif choice == 2:
            value = input("Enter the element to be searched: ")
            index = hash_fn(value)
            if hash_set[index] == value:
                print(f"\nElement Exists at index {index}")
            else:
                print("\nElement Not Stored.")
        elif choice == 3:
            value = input("Enter the element to be deleted: ")
            index = hash_fn(value)
            if hash_set[index] == value:
                print(f"Deleted {value}")
                hash_set[index] = None
            else:
                print("Element is not stored.")
        elif choice == 4:
            for element in hash_set:
                if element:
                    print(element)
        else:
            print("Please Choose from the given options only.")