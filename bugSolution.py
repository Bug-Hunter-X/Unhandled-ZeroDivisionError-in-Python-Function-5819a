def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1/x # ZeroDivisionError
        else:
            return 1/x
    except ZeroDivisionError:
        return float('inf') # Or handle it appropriately
        # print("Error: Division by zero")
        # return None

# Example usage
result = function_with_uncommon_error(0)
print(result) # Output: inf 