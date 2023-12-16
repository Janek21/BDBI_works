import random,os

algorithm_dictionary1 = {
    "Linear Search recursive": """
        function ALGORITHM(A, x, low, high):
            if low > high:
                return None
            elif x == A[low]:
                return low
            else:
                return ALGORITHM(A, x, low + 1, high)
    """,

    "Binary Search recursive": """
        function ALGORITHM(A, x, low, high):
            if low > high:
                return None
            m = ⌊(low + high)/2⌋
            if x == A[m]:
                return m
            elif x > A[m]:
                return ALGORITHM(A, x, m + 1, high)
            else:
                return ALGORITHM(A, x, low, m - 1)
    """,

    "Quicksort": """
        procedure ALGORITHM(A):
            ALGORITHM(A, 1, n)
        
        procedure ALGORITHM(A, p, r):
            if p < r:
                q = PARTITION(A, p, r)
                ALGORITHM(A, p, q - 1)
                ALGORITHM(A, q + 1, r)
    """,

    "Merge Sort": """
        procedure ALGORITHM(A):
            ALGORITHM(A, 1, n)
        
        procedure ALGORITHM(A, p, r):
            if p >= r:
                return
            q = ⌊(p + r)/2⌋
            ALGORITHM(A, p, q)
            ALGORITHM(A, q + 1, r)
            MERGE(A, p, q, r)
    """,

    "Tre Quicksort": """
        procedure ALGORITHM(A, p, r):
            while p < r:
                q = PARTITION(A, p, r)
                ALGORITHM(A, p, q - 1)
    """,

    "Linear Search non recursive": """
        function ALGORITHM(A, x):
            i = 1
            while i <= n and x != A[i]:
                i = i + 1
            if i > n:
                return None
            return i
    """,

    "Binary Search non recursive": """
        function ALGORITHM(A, x, low, high):
            while low <= high:
                mid = ⌊(low + high)/2⌋
                if x == A[mid]:
                    return mid
                elif x > A[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return None
    """,

    "Bubble Sort": """
        procedure ALGORITHM(A):
            for i = 1 to n - 1:
                for j = n downto i + 1:
                    if A[j] < A[j - 1]:
                        exchange A[j] with A[j - 1]
    """,

    "Selection Sort": """
        procedure ALGORITHM(A):
            for i = 1 to n - 1:
                smallest = i
                for j = i + 1 to n:
                    if A[j] < A[smallest]:
                        smallest = i
                exchange A[i] with A[smallest]
    """
    # Add more algorithms as needed
}
algorithm_dictionary = {}
for x in algorithm_dictionary1:
	algorithm_dictionary[algorithm_dictionary1[x]] = x
def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_algorithm(c):
    # Select a random algorithm
    algorithm_code = random.choice(list(algorithm_dictionary.keys()))

    # Display the code snippet
    print("Algorithm Code:", algorithm_code)

    # Ask the user to guess the algorithm's name
    user_guess = input("Guess the algorithm's name: ")

    # Check if the guess is correct
    correct_answer = algorithm_dictionary[algorithm_code]
    clear_screen()
    if user_guess.lower() == correct_answer.lower():
        print("Correct! Well done.")
        c+=1
    else:
        print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}")
    return c

continueover = True
while continueover:
	tries = 0
	x = 0
	while tries < 10:
		tries +=1
		x = guess_algorithm(x)
		print(f'------\nSCORE: {x}/{tries}\n------')
	decision = input("Want to try again?(Y/N)")
	if decision.lower() != "y":
		continueover = False
	clear_screen()
			
		

