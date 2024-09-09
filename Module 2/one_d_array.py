"""1D arrays
"""

import numpy as np

def main():
    """Driven Function
    """
    # create an array
    array = np.array([-2,1,-5,10])
    print(array, type(array))

    numbers = [-2, 1, -5, 10]
    print(numbers, type(numbers))
    # Convert list into arrays 'cast it'
    new_array = np.array(numbers)
    print(new_array)

    #2D arrays
    matrix = np.array([[-1, 0 , 4],[-3, 6, 9]])
    print(matrix)
    #3D arrays
    three_d = np.array([[[-1, 0, 4],[-3, 6, 9]],[[5, 3, -4],[3,2,5]]])
    print(f'3D array {three_d}')

    # use the dtype optional argument to explicitly
    # call the type of the array
    numbers = [-2, 1, -5, 10]
    new_array = np.array(numbers, dtype=np.short)
    print(new_array, new_array.dtype)

    #unsigned data
    pos_numbers = [2, 1, 5, 10]
    new_array = np.array(pos_numbers, dtype=np.ushort)
    print(new_array, new_array.dtype)

    #float data
    new_array = np.array(pos_numbers, dtype=np.float32)
    print(new_array, new_array.dtype)

    

if __name__ == '__main__':
    main()
    