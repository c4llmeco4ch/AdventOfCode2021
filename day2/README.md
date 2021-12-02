# Day 2 Write-up

## Language

Python

## Key Takeaways

- Tuple unpacking is a nice way to initialize multiple variables on a single line
- Ternary operators are a nifty way to condense simple if-else blocks

## Question

Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

```md
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

## Process

As we discussed in our [day 1 write-up](https://github.com/c4llmeco4ch/AdventOfCode2021/blob/main/day1/README.md#process), we first need to read in data from our input file. This can be nearly identical to our day 1 code, only changing the file path to its new location.

```python
with open(file_path) as f:
    # code goes here
```

At this point, a good thing to take note of for our solution is that we need to keep track of two numbers throughout the course of our solution. I frequently refer to these types of variables as "running totals". They start at whatever the base value is for that specific data type (0 for numbers, empty strings and lists, false for booleans, etc.) and are simply updated throughout the solution to keep track of the total answer up to that point in the algorithm.

Since we are effectively referring to a 2-D plane, I find a simple `x` and `y` is perfectly sufficient for these values:

```python
x = 0
y = 0
```

If we want to consolidate these values a little bit, we can use our first bit of tech for the day...

### Tuple Unpacking

[Tuple unpacking](https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/) is a nice way to consolidate initialization of variables or combine values concisely into a single tuple. By putting multiple values on the left side of an assignment separtated by commas and matching that to comma-separated values on the right side, we can cleanly combine assignments into a single line:

```python
# without unpacking
x = 0
y = 0

# with unpacking
x, y = 0, 0
```

When we discussed `enumerate()` in yesterday's write-up, that was also an example of tuple unpacking in a more subtle manner. While this feature can be overdone (like any other), it's a nice tool to have in your pocket when you want to keep things tidy.

---

Moving on, we now need to loop through each line and determine what it instructs us to do. Because we know how many times we are going to repeat this process (as many lines as there are in the file), we can use a for loop. Also, because we do not need to manipulate any values coming in from the file, we can use a for-each loop: `for line in f.readlines()`.

At this point, we need to split up each line into its respective instruction and amount. Using `str.split()` is perfect here:

```python
s = line.split()
instr = s[0]
amount = int(s[1])
```

We could even combine those last two lines using tuple unpacking if we feel so inclined: `instr, amount = s[0], int(s[1])`. We've done a lot up to this point, so let's put it all together and evaluate what is left:

```python
x, y = 0, 0
with open(my_file) as f:
    for line in f.readlines():
        s = line.split()
        instr, amount = s[0], int(s[1])
```

From here, we just need to evaluate what the instruction is and perform the correct operation to either `x` or `y`. An if-else block works perfectly here as, depending on what the instruction is, we need to change either either the vertical or horizontal position. Since only "forward" alters the x-value, it makes sense to check that instruction first: `if instr == 'forward':`. Should that be the case, we just need to increase `x` by `amount`. Combining these two lines, we get...

```python
if instr == 'forward':
    x += amount
```

There are two ways we can approach dealing with the remaining instructions. The first way is to use an elif statement for one of the remaining instructions (say, "down") and an else block to deal with the last option:

```python
elif instr == 'down':
    y += amount
else:
    y -= amount
```

The alternative is to use nested if statements:

```python
if instr == 'forward':
    x += amount
else:
    if instr == 'down':
        y += amount
    else:
        y -= amount
```

At first, the second option seems much clunkier. After all, it is usually bad form to have nested if statements if they are not required. So why would we consider that here? That leads us to our second new piece of tech for the day...

### Ternary Operators

[Ternary operators](https://www.geeksforgeeks.org/ternary-operator-in-python/) are an entire if-else block shoved into a single line. By following the syntax, `value_when_true if condition else value_when_false`, we are able to take what would normally need 4 lines and turn it into a single statement. For our needs, this allows us to change the unattractive alternative above into something quite interesting:

```python
if instr == 'forward':
    x += amount
else:
    y += amount if instr == 'down' else -amount
```

Ultimately, there is always a balancing act between readability and conciseness. As you develop your programming skills, you will need to evaluate whether shaving off the extra few lines is worth the headache of having to parse a more complex piece of code. In this instance, however, we are given a nice opportunity to use a tool that can come in handy throughout our programming journey.

---

When we combine everything, we are left with our final working solution of...

```python
x, y = 0, 0
with open(my_file) as f:
    for line in f.readlines():
        s = line.split()
        instr, amount = s[0], int(s[1])
        if instr == 'forward':
            x += amount
        else:
            y += amount if instr == 'down' else -amount
```

With all of that out of the way, we simply need to print the product of `x` and `y`, which results in a final answer of _1840243_.

## How This Changes for Part 2

With part 2, the difficulty comes from adding a third value, `aim`, into our calculations. Our first line can be updated easily due to our tuple unpacking: `x, y, aim = 0, 0, 0`.

Afterwards, all we need to do is alter our if-else block to accommodate for aim's place in our logic:

```python
if instr == 'forward':
    x += amount
    y += aim * amount
else:
    aim += amount if instr == 'down' else -amount
```

With this updated code, all we need to do is re-run our algorithm to reach a final product of _1727785422_.
