Numerical Methods in Python

This project implements fundamental numerical methods in Python for solving mathematical problems that cannot be solved analytically. The project focuses on root-finding techniques and numerical solutions of ordinary differential equations.

Overview

Numerical methods are essential tools in scientific computing, engineering, and applied mathematics. This project provides clean and structured Python implementations of the following methods:

Bisection Method
Newton’s Method
Euler’s Method
Each method is implemented to demonstrate its algorithm, accuracy, and limitations.

Implemented Methods

Bisection Method
Description

The Bisection Method is a root-finding algorithm that repeatedly divides an interval in half and selects the subinterval in which a root exists. It requires the function to be continuous on the given interval and the function values at the endpoints to have opposite signs.

Features

Guaranteed convergence for valid intervals
Simple and reliable implementation
Iterative approximation of roots
Newton’s Method
Description

Newton’s Method (Newton–Raphson Method) is an efficient root-finding technique that uses the derivative of a function to rapidly converge to a root, starting from an initial guess.

Features

Fast convergence near the root
Requires first derivative of the function
Sensitive to initial guess selection
Euler’s Method
Description

Euler’s Method is a numerical technique for solving first-order ordinary differential equations (ODEs) of the form:

dy/dx = f(x, y)

It approximates the solution by advancing step by step using a fixed step size.

Features

Simple numerical solution of ODEs
Step-by-step approximation
Suitable for introductory numerical analysis
Technologies Used

Programming Language: Python 3
Libraries: Python standard library (math)
Project Structure

numerical-methods-python/ │ ├── bisection_method.py ├── newtons_method.py ├── eulers_method.py

How the Program Works

The user defines the mathematical function and relevant parameters.
The selected numerical method is applied.
The algorithm iteratively computes approximations.
The final numerical solution is displayed in the console.
Applications

Solving nonlinear equations
Approximating roots of functions
Numerical solution of differential equations
Academic and educational purposes
Limitations

Accuracy depends on step size, tolerance, and initial guesses
Some methods may fail for poorly chosen parameters
Euler’s Method may accumulate error for large step sizes
Future Improvements

Add error analysis and convergence plots
Implement higher-order methods (Runge–Kutta)
Add user input validation
Include graphical visualization of results
Author My code commits are stored in the master branch of this repo Ssekamate Sharif