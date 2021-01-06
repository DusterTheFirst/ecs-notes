# Lists

[Jump to TL;DR (summary)](#too-long-didnt-read)

Lists in python are very simple to create. They are specified by a square bracket `[`, a comma
separated list of the data you would like, and a closing square bracket `]`. Below are a few
examples of lists.

```python
{{#include lists.py:3:4}}
```

Lists alone are pretty cool, but we sometimes might want to get a single value from a list.
To do so, we need to use some more square brackets. This time, our square brackets go after the name
of the list, and within them is the `index` of the value we want.

If I had a list `MY_LIST` and wanted to get the 2nd element, I would write `MY_LIST[1]`. And yes,
that is not a typo, you use the number 1 to refer to the 2nd element. Why is that? Well it has to do
with a whole lot of how computers work, but the main thing to remember is that `1` is not the first
element, `0` is.

> Lists in python are what are called 0 indexed lists, or their first value has the index of 0

Here is another example of getting data from a list

```python
{{#include lists.py:8:12}}
```

## Mutation

Just having a list of items is cool, but what if we want to change what is in the list? Well that is
where list mutation comes into play.

There are a few ways we can mutate a list. We can change the value stored in one of the indexes,
like so

```python
{{#include lists.py:16:20}}
```

> Note how the list's name is `lower_snake_case` instead of `UPPER_SNAKE_CASE` since it is mutable
or not constant

Or, we can add items to the end of the list, with the `append` method

```python
{{#include lists.py:24:26}}
```

> `print` can print out whole lists for us which is useful for making sure the list has what we
think it has in it

As well as adding items to lists, we can remove items.

```python
{{#include lists.py:30:31}}
```

> **WATCH OUT** `remove` takes in the value to remove, not the index

## Length

We all know the size of your list is not what matters, but instead how you use it. Sometimes it is
useful to know its length every once and a while though. Luckily for us, python provides a handy
dandy `len` function, the same one we have been using to get the length of a string.

```python
{{#include lists.py:35:37}}
```

## Looping

Sometimes, just getting one element is not enough for us, and instead we want to do something with
or to the whole list. To do so, we can use a loop to go over each element of the list, and do
something. The simplest thing to do is to just print out each element in a list.

```python
{{#include lists.py:41:44}}
```

We might also want to produce a single value based on all the items in the list, such as a sum.
Let's make a function to calculate the sum of a list of numbers. Its signature would look as such:

```python
{{#include lists.py:52:54}}
```

Since we need a place to store our sum, we will create a variable and call it `result`

```python
{{#include lists.py:55}}
```

And then we can loop over every element

```python
{{#include lists.py:57:58}}
```

And then finally, we can return the result, leaving us with

```python
{{#include lists.py:52:63}}
```

If we were to use our function, we could do so as such:

```python
{{#include lists.py:65:67}}
```

## Example: Counting

```python
{{#include lists.py:71:80}}
```

## Too Long; Didn't Read

If you want an abridged version, you can look at just the code that I have gone over
[here][python-code]

[python-code]: https://github.com/DusterTheFirst/ecs-notes/tree/main/src/python/lists.py
