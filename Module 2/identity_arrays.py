"""My template
"""
import numpy as np

def main():
    """Driven Function
    """
    # create a 2D 3x3 identity matrix 
    identity_3x3 = np.eye(3,3)
    print(identity_3x3)
    identity_3x5 = np.eye(3,5)
    print(identity_3x5)

    # create a 2D Diagonal array, with given entries
    diagonal_2D = np.diag([2, 3, 4, 5])
    print(diagonal_2D)

    # Create a 5x3 2D array of unsigned integers filled with zeros
    arr_5x3 = np.zeros((5,3), dtype = np.uint)
    print(f'arr_5x3: \n{arr_5x3}')

    #create a 5x3 2D array of unsigned integers filled with ones
    arr_5x3_ones = np.ones((5,3), dtype=np.uint)
    print(f'arr_5x3_ones: \n{arr_5x3_ones}')

    #create a 5x3 2D array of unsigned integers filled with another value
    arr_5x3_pi = np.full((5,3), np.pi)
    print(f'arr_5x3_pi: \n{arr_5x3_pi}')

    #create a 5x3 2D array of unsigned integers filled with random numbers
    arr_5x3_rand = np.random.random((5,3))
    print(f'arr_5x3_rand: \n{arr_5x3_rand}')

if __name__ == '__main__':
    main()
    