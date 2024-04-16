# Sort Compare
# This version of Sort Compare uses global variables 
# to store the statistics for a set of numbers using a given sort

# Read numbers from input and return them in a list
def get_nums(line):
    return [int(num) for num in line.split()]

# Exchange nums[n] and nums[m]
def swap(nums, n, m):
    nums[n], nums[m] = nums[m], nums[n]
  
# Print the results of a given sort for a given list of numbers    
def print_results (type, numbers, swaps, comparisons, extra_bytes):
    print (type, "Results")
    print(f'Sorted numbers: {numbers}')
    print(f'Comparisons: {comparisons}')
    print(f'Swaps: {swaps}')
    print(f'Extra Bytes: {extra_bytes}\n')
    

###############  Zybooks Selction Sort
def selection_sort(numbers):
    comparisons = 0
    swaps = 0
    extra_bytes = 0  
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            comparisons += 1;
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
    
        # Swap numbers[i] and numbers[index_smallest]
        swaps += 1
        swap(numbers, i, index_smallest)

    print_results ("Selection Sort", numbers, swaps, comparisons, extra_bytes)

###############  Zybooks Insertion Sort
def insertion_sort(numbers):
    comparisons = 0
    swaps = 0
    extra_bytes = 0 
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] is in correct position
        while j > 0:
            comparisons += 1                    
            if numbers[j] < numbers[j - 1]:    
                swaps += 1
                swap(numbers, j, j-1)                               
                j -= 1
            else:
                break                          
    print_results ("Insertion Sort", numbers, swaps, comparisons, extra_bytes)

        
##############  Zybooks Merge Sort        
def merge(numbers, i, j, k):

    global comparisons 
    global swaps 
    global extra_bytes 
                 
    merged_size = k - i + 1  
    merged_numbers = []
    for l in range(merged_size):
        extra_bytes += 4
        merged_numbers.append(0)

    merge_pos = 0                         

    left_pos = i                         
    right_pos = j + 1                   

    while left_pos <= j and right_pos <= k:
        # Added for solution
        comparisons += 1                  
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    merge_pos = 0
    while merge_pos < merged_size:
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        merge_pos = merge_pos + 1


def merge_sort(numbers, i, k):

    global comparisons 
    global swaps 
    global extra_bytes 

    j = 0
    if i < k:
        j = (i + k) // 2 

        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)

        merge(numbers, i, j, k)

        
############## Zybooks Quick Sort
def partition(numbers, i, k):
    global comparisons 
    global swaps 
    global extra_bytes 
    #  Pick middle element as pivot 
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]

    #  Initialize variables
    done = False
    l = i
    h = k
    while not done:
        #  Increment l while numbers[l] < pivot 
        while numbers[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h] 
        while pivot < numbers[h]:
            h = h - 1
        """  If there are zero or one items remaining,
              all numbers are partitioned. Return h """
        comparisons += 1      
        if l >= h:
            done = True
        else:
            swaps += 1
            swap(numbers, l, h)      
            l = l + 1
            h = h - 1
    return h


def quick_sort(numbers, i, k):
    global comparisons 
    global swaps 
    global extra_bytes 

    j = 0
    """  Base case: If there are one or zero entries to sort,
          partition is already sorted  """ 
    comparisons += 1      
    if i >= k:
        return
    """  Partition the data within the array. Value j returned
          from partitioning is location of last item in low partition. """ 
    j = partition(numbers, i, k)
    """  Recursively sort low partition (i to j) and
          high partition (j + 1 to k) """
    quick_sort(numbers, i, j)
    quick_sort(numbers, j + 1, k)
    
    return
        

def main():
    # required here for merge and quick sort only
    global comparisons 
    global swaps 
    global extra_bytes 

    # open file
    debug = True
    if debug:
        in_data = open('sort.in')
    else:
        in_data = sys.stdin        
        
    # read each line and analyze, each line is a set of number to sort
    line = in_data.readline()
    while line != "":
        original_nums = get_nums(line)
        print ("########################### New Numbers")
        print(f'##### Original numbers: {original_nums}\n')
        
        # Selection Sort
        nums_to_sort = original_nums.copy()
        selection_sort (nums_to_sort)
        
        # Insertion Sort
        nums_to_sort = original_nums.copy()      
        insertion_sort (nums_to_sort)
        
        # Merge Sort
        nums_to_sort = original_nums.copy()
        comparisons = 0
        swaps = 0
        extra_bytes = 0
        merge_sort (nums_to_sort, 0, len(nums_to_sort)-1)
        print_results ("Merge Sort", nums_to_sort, swaps, comparisons, extra_bytes)

        # Quick Sort
        nums_to_sort = original_nums.copy()
        comparisons = 0
        swaps = 0
        extra_bytes = 0
        quick_sort (nums_to_sort, 0, len(nums_to_sort)-1)
        print_results ("Quick Sort", nums_to_sort, swaps, comparisons, extra_bytes)

        print()
        line = in_data.readline()


if __name__ == "__main__":
    main()