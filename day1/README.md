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

## How This Changes for Part 2

TBA
