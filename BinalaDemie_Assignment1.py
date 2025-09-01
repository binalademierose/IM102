while True: 
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    search = int(input("Enter the number you want to search: "))

    if rows or columns < 1:
        break
    else:
        
         for x in range (1, rows + 1):
            for y in range(1, columns + 1):
                value = x * y
                if value == search:
                    print(f"[{value}]", end="\t")
                else:
                    print(value, end="\t")
            print()

