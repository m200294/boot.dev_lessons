# enumerate

The enumerate function takes any iterable (e.g. list, tuple, dict) and lets you loop over it as (index, item) pairs.

Take for example a list of items:

```python
items = ["Arkenstone", "Glamdring", "Palantiri"]
```

Using the enumerate function we can loop over the list and print out the (index, item) tuple like so:

```python
for pair in enumerate(items):
  print(pair)
```

Which gives us:

```
(0, 'Arkenstone')
(1, 'Glamdring')
(2, 'Palantiri')
```

We can also unpack each tuple into its index and item to gain more control over them like so:

```python
for index, item in enumerate(items):
    print(f"item number: {index + 1} is the GREAT {item}")
```

Which results in: 
```
item number: 1 is the GREAT Arkenstone
item number: 2 is the GREAT Glamdring
item number: 3 is the GREAT Palantiri
```

## Assignment: 
Players in Fantasy Quest just finished their horse racing tournament. Each player's name is added to a list the moment they cross the finish line. Write a function that takes the list of players and returns a list of strings, one per player, in the format Rank: 1, Name: Sauron.

