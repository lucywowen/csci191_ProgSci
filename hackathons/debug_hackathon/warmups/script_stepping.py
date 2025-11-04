def inner_function(x):
    print(f"Inside inner_function with x: {x}")
    return x * 2

def outer_function(y):
    print(f"Inside outer_function with y: {y}")
    val = inner_function(y + 1) # Set a breakpoint here
    return val + 10

data = 5
final_result = outer_function(data)
print(f"Final result: {final_result}")
