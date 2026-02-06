# Python Practice Programs

This repository contains basic Python programs implemented for learning
and interview preparation.

---

## Fibonacci Generator

A Python project to generate Fibonacci sequences using generators.

### Features
- Generate first N Fibonacci numbers
- Command-line interface
- Input validation
- Unit tests

### Usage
```bash
python main.py 10
```

## Factorial Program

    A Python program to calculate the factorial of a non-negative integer.

### Features
- Iterative approach using loop
- Recursive approach
- Input validation and error handling

### Concepts Used
- Loops
- Recursion
- Functions
- Error handling

### Time Complexity
- O(n)

### Usage
```bash
python factorial.py
```
## Prime Number Checker

    This Python program checks whether a given number is a prime number.

---

## Features
- Optimized prime number checking
- Command-line input
- Input validation for non-integer values

---

## Concepts Used
- Loops
- Conditional statements
- Functions
- Mathematical optimization

---

## Time Complexity
- **O(√n)** — checks divisibility only up to the square root of the number

---

## How to Run

```bash
python prime_number.py
```

## Number reversal program
    This Python program reverses a given integer and displays both the original
    number and its reversed form.
---

## Features
- Reverses a given integer
- Uses arithmetic operations (no string conversion)
- Command-line input

---


## Algorithm
1. Read the input number
2. Store the original number in a temporary variable
3. Extract the last digit using modulus
4. Build the reversed number by shifting digits
5. Remove the last digit using integer division
6. Repeat until the number becomes zero

---

## Time Complexity
- **O(d)** where `d` is the number of digits

---

## How to Run

```bash
python reverse_number.py
```

## String reversal program
    
    This Python program reverses a given string using a loop.

---

## Features
- Reverses a string without using built-in reverse functions
- Simple and beginner-friendly logic

---

## Concepts Used
- For loop
- String concatenation
- Variables

---

## Time Complexity
- **O(n)** where `n` is the length of the string

---

## How to Run

```bash
python reverse_string.py
```

## Compound Interest Calculator (Python)

    This is a simple Python program that calculates **Compound Interest** based on user input.  
    The user provides the **principal amount**, **rate of interest**, and **time period**, and the program outputs the compound interest.

---

## Formula Used

    A = P × (1 + R / 100) ^ T  

    Compound Interest = A − P  

    Where:
- **P** = Principal amount  
- **R** = Rate of interest (percentage)  
- **T** = Time in years  
- **A** = Total amount after interest  

---

## How the Program Works

1. Takes principal amount as input  
2. Takes rate of interest as input  
3. Takes time period in years as input  
4. Calculates the total amount using the compound interest formula  
5. Displays the compound interest  

---
```bash
python compound_interest.py
```
Swap Two Numbers Without Using a Temporary Variable
📌 Description

This project demonstrates how to swap the values of two variables without using a temporary variable. The logic is based on simple arithmetic operations and is commonly used to help beginners understand variable manipulation.

🧠 Concept Used

The swapping is achieved using addition and subtraction. By carefully updating the values step by step, the original values of the variables are exchanged without needing extra memory.

▶️ Program Flow

Take two integer inputs from the user

Apply arithmetic operations to swap their values

Display the values after swapping

✅ Key Features

No temporary variable required

Easy to understand logic

Suitable for beginners

Works efficiently with integer values

⚠️ Important Note

This approach is ideal for learning purposes. While Python safely handles large integers, in some other programming languages this method may cause overflow for very large numbers.

📚 Learning Outcomes

Understanding variable reassignment

Practicing arithmetic operations

Learning alternative swapping techniques