"""Do array operations
"""
import numpy as np

def main():
    """Driven Function
    """
    numbers_lst = [2, 4, 6, 8, 10]
    print(numbers_lst)
    # Increment each element by 3 *SUCKS by just using what python has*
    for item in range(len(numbers_lst)):
        numbers_lst[item] = numbers_lst[item] + 3
    
    print(numbers_lst)

    # Convert list to numpy array
    numbers_arr = np.array(numbers_lst)
    print(f'Numpy before array: {numbers_arr}')
    # Add 3 to each element
    numbers_arr +=3
    print(f'Numpy after array: {numbers_arr}')

if __name__ == '__main__':
    main()
    