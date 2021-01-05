# ECS Help Sheet

| Designing Data | Designing Functions |
|:--------------:|:-------------------:|
| Data Definition - what kind of data is allowed | Signature - what kind of data goes in and what kind of data comes out? |
| Interpretation - what does this data mean? | Purpose - what does this function do? |
| Examples (at least 2) | Testing - examples of how the function works (using check-expect) |
| Template (see [Designing Templates](#designing-templates)) | Code - using the template |

## Designing Templates

1. How many cases of data are there? If there is more than one option, you will need a
    **conditional expression** (this happens when you have union data)
2. How can you tell the cases apart? This will determine the question you ask in each clause of your
    conditional expression.
You can skip this step if you are not working with union data.
3. What can you pull out of the data in each case? If it is **structured data**
you must call the selectors here.
4. Is the data you pilled out complex with its own data definition? If you are referencing
another data definition that you made, you need to call the template for that data type on the
selected data.

## Designing Programs

1. What changes and what stays the same? Things that stay the same are **constants** and
things that change are your **WorldState** (you may need to design your own data here).
2. Which clauses do we need? Your options are: `to-draw`, `on-tick`, `on-mouse`, `on-key` and
`stop-when`.
3. Design your main function (the one that calls `big-bang`). This is the __***only***__
function you cannot write tests for. Make a wishlist of the functions you need to design.
4. Design the functions on your wishlist. Be sure to follow all the steps of the function
design recipe when you do so.
