# comprehensions

In Python, a comprehension is a one-line way to build a new collection from an iterable. 

That's cool but what does that actually mean? 
You're probably comfortable with Python lists by now. 
Comprehensions make writing lists faster

Say we want to make a list containing numbers 1 through 10. Here's the conventional way to do it:

```python
numbers = []
for x in range(1, 11):
    numbers.append(x)
```

That gives us:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

It works, but it takes 3 lines to express one simple idea. This is where list comprehensions come in:

```python
numbers = [x for x in range(1, 11)]
```

## The formula
Every list comprehension follows the same pattern:

```
[expression for item in iterable]
```

<img width="6360" height="4768" alt="IMG_0042" src="https://github.com/user-attachments/assets/3eeae038-8fb2-4be7-a7aa-296b33d8ef39" />


Mapping that onto `[x for x in range(1, 11)]`:

- The first `x` is the **expression** (what gets added to the list each pass)
- The second `x` is the item in the iterable
- `range(1, 11)` is the iterable itself

## Assignment
Complete the `comprehension` function. Using a list comprehension, return a list of the numbers from 0 up to and including `int`.
