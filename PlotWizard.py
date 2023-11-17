import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def plot_math_function():
    # Get mathematical function from user input
    function_str = input("Enter a mathematical function in terms of 'x': ")

    try:
        # Parse the input expression
        x = sp.symbols('x')
        expr = sp.sympify(function_str)
        
        # Convert the expression to a numpy function
        func = sp.lambdify(x, expr, 'numpy')

        # Create x values
        x_values = np.linspace(-10, 10, 1000)
        
        # Evaluate the function for y values
        y_values = func(x_values)

        # Plot the function
        plt.plot(x_values, y_values)
        plt.title(f'Graph of {function_str}')
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        print("Please enter a valid mathematical function.")


plot_math_function()
