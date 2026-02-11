
def square_root_bisection(number, tolerance = 0.1e-7, max_iteration = 50):

    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number in (0,1):
        print(f"The square root of {number} is {number}")
        return number
    low = 0
    high = max(1,number)

    for i in range(max_iteration):
        mid = (low + high) / 2
        

        if (high - low) / 2 < tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        
        if mid*mid < number:
            low = mid
        else:
            high = mid
    print(f"Failed to converge within {max_iteration} iterations")
    return None
        


print(square_root_bisection(0.001, 1e-7, 50))