from sorts import insertion_sort

def vyber_algorythm(cisla):
    min_max_index(cisla)

    print('\n\n Zvol cislo')
    print('1. Bubble Sort')
    print('2. Merge Sort ')
    print('3. Insertion Sort ')   
    print('4. Quick Sort ')   
    print('5. All Sorts ')   

    choice = int(input('Enter your choice:'))
    original_pole = cisla


    import time
    import sorts

    if (choice == 1):
        print('Choice 1\n')

        sorts.buble_sort(cisla)
        print("Sorted array: " + str(cisla))

    if (choice == 2):
        print('Choice 2\n')

        sorts.merge_sort(cisla, 0, len(cisla) -1)
        print("Sorted array: " + str(cisla))
    if (choice == 3):
        print('Choice 3\n')

        sorts.insertion_sort(cisla)
        print("Sorted array: " + str(cisla))
    if (choice == 4):
        print('Choice 4\n')
        sorts.quick_sort(cisla, 0, len(cisla) - 1)
        print("Sorted array: " + str(cisla))
    if (choice == 5):
        print('Choice 5\n')

        import time
        
        original_array = cisla
        buble_array = original_array
        merge_array = original_array
        insertion_array = original_array
        quick_array = original_array


        print('Execution time in seconds for:')

        startTime = time.time()
        sorts.buble_sort(buble_array)
        executionTime = (time.time() - startTime)
        print('Buble sort: ' + str(executionTime))

        startTime1 = time.time()
        sorts.merge_sort(merge_array, 0, len(merge_array) -1)
        executionTime = (time.time() - startTime1)
        print('Merge sort ' + str(executionTime))

        startTime2 = time.time()
        sorts.insertion_sort(insertion_array)
        executionTime = (time.time() - startTime2)
        print('Insertion sort: ' + str(executionTime))

        startTime3 = time.time()
        sorts.quick_sort(quick_array, 0, len(quick_array) - 1)
        executionTime = (time.time() - startTime3)
        print('Quick sort ' + str(executionTime))
        
        print("Sorted array: " + str(merge_array))

def min_max_index(cisla_uzivatele):

    max_cislo =  max(cisla_uzivatele)
    min_cislo = min(cisla_uzivatele)

    print ("Nejvyšší hodnota v seznamu: ", max_cislo)
    print ("Nejmenší hodnotu v seznamu: ", min_cislo)

    print ("Index pro nejvyšší hodnota v seznamu: ", cisla_uzivatele.index( max_cislo))
    print ("Index pro nejmensi hodnota v seznamu: ", cisla_uzivatele.index( min_cislo))   

