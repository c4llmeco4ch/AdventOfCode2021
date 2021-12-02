# Day 1 Write-up

## Language

Python

## Key Takeaways

- We can use `enumerate()` in a for loop to gain the benefits of both C-style for loops _and_ for-each loops
- List comprehension is an incredible feature in Python

## Question

--- Day 1: Sonar Sweep ---

You're minding your own business on a ship at sea when the overboard alarm goes off! You rush to see if you can help. Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this. It's covered in Christmas lights (because of course it is), and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

```md
199
200
208
210
200
207
240
269
260
263
```

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

```md
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

## Process

The first thing we need to do is learn how to read in a file. To do this, our best bet is to utilize the following code snippet:

```python
with open('my_file.txt') as f:
    lines = f.readlines()
    # the rest of our code goes here
```

By using the `with` reserved word, we are able to automatically close the file when our code is finished, saving us a minor headache later. `my_file.txt` should also be replaced with the file path of wherever you saved your input data. Finally, we read all the lines from the file and save it to a variable, `lines`, using the `f.readlines()` function. More information on reading from files can be found [here](https://pythonspot.com/read-file/).

We also need to keep track of how many increases in depth we have seen. This can be solved by creating a simple variable to track our progress: `count = 0`

Now that we have all of our data, we need to decide how we are going to compare each line against the line that follows it. We know that we need to repeat a certain section of code over and over, so we can quickly deduce a loop of some kind is needed. But how do we decide whether to use a for loop or a while loop? __If you know how many times a loop will be repeated with a high degree of certainty, it can be simpler to use a for loop. Any other situation usually calls for a while loop__. Since we know how many lines of data we have (`len(lines)`), a for loop seems like a solid decision.

### C-Style Loops vs For-Each Loops

Now that we know to use a for loop, we need to make a decision on what the structure of that for loop is. If we consider a language like Java, there are two distinct forms: a traditional "C-Style" for loop and a for-each loop:

```java
char[] myArray = new char[5];

// C-Style
for(int i = 0; i < myArray.length; i++){}

// For-each
for(char c : myArray){}
```

When working with an iterable (arrays, lists, vectors, etc.), the benefit of the former is that we have direct access to the index of each item. This means we have the ability to not only _read_ the values from the iterable but also _write_ new values. In Python, we might see a piece of code like this:

```python
my_list = [1, 2, 3, 4]
for i in range(len(my_list)):
    my_list[i] *= 2 # double the value of each element in the list
print(my_list) # prints [2, 4, 6, 8]
```

For-each loops, on the other hand, are great when we only want to _read_ data from the iterable. While this might seem like a net negative, the code can be a more concise and, by extension, easier to read when utilizing this type of loop:

```python
my_list = [1, 2, 3, 4]
for val in my_list:
    val *= 2
    print(val) # prints 2, 4, 6, 8
print(my_list) # prints [1, 2, 3, 4]
```

So we have a type of for loop that is better generally and a type that has more restrictions but is more concise. It would be pretty neat if there were a way to do both...

### enumerate()

`enumerate()` ([link](https://www.tutorialspoint.com/enumerate-in-python)) is an absolute workhorse and I would highly recommend acquainting yourself with it early on if you plan on using Python for the majority of your AoC problems. Combining the benefits of a C-Style for loop and a for-each loop, this function will carry you far. Syntactically, we provide the for loop with an index variable (much like `i` in our C-Style example) and a value variable (much like `val` in our for-each example) to get the following:

```python
my_list = [1, 2, 3, 4]
for i, val in enumerate(my_list):
    val *= 2
    my_list[i] = val
print(my_list) # prints [2, 4, 6, 8]
```

This applies to our problem because while we do need to read our current value (so we might want to use a for-each loop), we also need to know where our value is in the list to compare it to the next value. By using `enumerate()` over each value from `lines`, we can keep track of both the current value and the value that comes after through the following snippet:

```python
for pos, num in enumerate(lines[:-1]):
    if int(num) < int(lines[pos + 1]):
        count += 1
```

Putting it all together, we get our final bit of code:

```python
with open('my_file.txt') as f:
    lines = f.readlines()
    count = 0
    for pos, num in enumerate(lines[:-1]):
        if int(num) < int(lines[pos + 1]):
            count += 1
```

By printing `count` after our for loop is completed, we arrive at our final answer to part 1, _1482_

## Part 2

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

```md
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
```

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

```md
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
```

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

## What Changes in Our Solution for Part 2

When dealing with the sliding window, there are multiple ways to approach this problem. The solution I opted for is to detemine the groups beforehand, then compare the sums of each group to receive our final count.

A simple way to calculate the groups would be to utilize a for loop similar to the following:

```python
groups = []
for pos, val in enumerate(lines[:-2]):
    total = int(val) + int(lines[pos + 1]) + int(lines[pos + 2])
    groups.append(total)
```

This is perfectly acceptable, but we have the opportunity to use one of the most powerful tools that Python has to offer here: [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)!

A simple implementation of list comprehension here might look like the following:

```python
converted_vals = [int(i) for i in lines]
groups = [sum(converted_vals[pos : pos + 3]) for pos in range(len(converted_vals[:-2])]
```

Already, this code is much more concise than the previous iteration. However, we can actually take the code a step futher by implementing a list comprehension _inside of_ a list comprehension! `groups = [sum(int(i) for i in lines[pos : pos + 3]) for pos in range(len(lines) - 2)]` does exactly what we had before condensed into a single line.

When we put everything together from part 1 and update our if statement to compare group sums as opposed to individual values, we can rerun the code and produce a final answer of _1518_.
