# Unions and data design
[Jump to TL;DR (summary)](#tldr-october-13-2020)\
[Jump to Table Of Contents](#file-ecs-notes-md)\
[Code for this lesson on wescheme](https://www.wescheme.org/openEditor?publicId=wRuHb37cbQ)

## Lab 2 Problem 2
> Design a function message-to-employee which takes in the kind of data you defined above and
produces a message about the employee’s paycheck. For example if the employee receives a paycheck
every week you should produce “Here is your weekly paycheck!”. Is the template useful here? Why or
why not?

**Define what the data is**\
    Paycheck can be weekly, biweekly, or monthly.
    
**What does it represent?**\
    Paycheck represents how often an employee is paid.

Now that we have it all in our head, we should put it down in a comment:
```scheme
; A Paycheck is one of:
; - "weekly"
; - "biweekly"
; - "monthly"
; and represents how often an employee is paid
```
    
Once you have the idea, define some constants (if there are a finite amount).
 ```scheme
 (define PC-W "weekly")
 (define PC-B "biweekly")
 (define PC-M "monthly")
```

Once you have the idea and the data, create a template:
```scheme
(define (paycheck-template pc)
    (cond [(string=? pc PC-W) ...]
          [(string=? pc PC-B) ...]
          [(string=? pc PC-M) ...]))
```
> The `...`s are not valid scheme, they just tell us that we will come back to them later.

*Now we can move onto creating a function to tell the employee about their paycheck.*
**Always** start by laying out the function you want.

**Name:** `message-to-employee`\
**Input:** `Paycheck`\
**Output:** `String`\
**Description:** `Message an employee about when their paycheck arrives.`

Now that you have it in your head, put it in a comment.
```scheme
; message-to-employee : Paycheck -> String
; Message an employee about when their paycheck arrives
```

Once you have the layout of your function, **ALWAYS** write out (at least) 2 check-expect tests.
```scheme
(check-expect
    (message-to-employee PC-W)
    "Here is your weekly paycheck!")
(check-expect
    (message-to-employee PC-B)
    "Here is your biweekly paycheck!")
(check-expect
    (message-to-employee PC-M)
    "Here is your monthly paycheck!")
```
> In this case, we create 3 tests since there are 3 variants of our type.

*Now that we have it all layed out, we can create a function by pasting our template.*
```scheme
(define (message-to-employee pc)
    (cond [(string=? pc PC-W) ...]
          [(string=? pc PC-B) ...]
          [(string=? pc PC-M) ...]))
```

Now we need to change the `...`s to something more useful.
*In our case, the `...`s would all become the same thing:*
```scheme
(define (message-to-employee pc)
    (cond [(string=? pc PC-W) (string-append "Here is your " pc " paycheck!")]
          [(string=? pc PC-B) (string-append "Here is your " pc " paycheck!")]
          [(string=? pc PC-M) (string-append "Here is your " pc " paycheck!")]))
```

Since they are all the *same*, we can simplify the function down to just one line.
```scheme
(define (message-to-employee pc)
    (string-append "Here is your " pc " paycheck!"))
```

In the end, our template and custom type were not used since they were more or less extrenious,
we did not need to create a custom type for this since there is one code path for every paycheck type

## Lab 2 Problem 3
> Design a function calculate-annual which takes in a Number, representing the amount an employee makes
on a single paycheck, and the data describing how often they receive the paycheck. It produces a Number
with an estimate of their annual wages. For example, if the employee gets their paycheck once per month
you will need to multiply the input number by 12 since there are 12 months in a year. Is the template useful
here? Why or why not?

*As always, start your function definition with its signature*

**Name:** `calculate-annual`\
**Input:** `Number and Paycheck`\
**Output:** `Number`\
**Description:** `Estimates how much an employee will earn by the end of the year`

Now that you have it all out, put it in a comment:
```scheme
; calculate-annual : Number Paycheck -> Number
; Estimates how much an employee will earn by the end of the year
```

*Check expect time!*
```scheme
(check-expect (calculate-annual 4 PC-M) 48)
(check-expect (calculate-annual 34 PC-W) (* 34 52))
(check-expect (calculate-annual 450 PC-B) (* 450 26))
```

Now that we have the check-expects all out, its time to make the function:
```scheme
(define (calculate-annual single-paycheck pc)
    (cond [(string=? pc PC-W) (* single-paycheck 52)]
          [(string=? pc PC-B) (* single-paycheck 26)]
          [(string=? pc PC-M) (* single-paycheck 12)]
```
> In this case, the custom data type is useful since we are able to use the seperate paths to calculate the paycheck differently

## Lab 2 problem 4
> Design data to represent the name of someone who has donated to a charity. Your data should account for the fact that the 
donor may wish to remain anonymous. Why can’t we use a String to represent the anonymous donor? What can we use instead? Don’t 
forget to follow all 4 steps of the design recipe for data.

The first thing we need to do when defining a data type is to define what it can be:
```scheme
; A DonorName is one of:
;   - String
;   - false
; and represents the name of someone donating to charity
```

Now that we have our data type all layed out for us, we should now create (at least) 2 examples of the data type.
```scheme
(define DONORNAME1 "Paul")
(define DONORNAME2 false)
```

Once we have some examples we can make a template:
```scheme
(define (donor-template dn)
    (cond [(string? dn) ...]
          [(boolean? dn) ...]))
```
> Remember, the ...s are there for us to replace later when we copy this template

## Lab 2 problem 5
> Design a function email-donor which takes in the type of data you defined above. If the donor is not anonymous it produces a 
message to send via email such as “Thank you, Bob!” if the donor’s name was Bob. If the donor was anonymous it produces false. 
What kind of data do you need to design in order to write the signature for this function?

As always, start your function definition with its signature:

**Name:** `email-donor`\
**Input:** `DonorName`\
**Output:** `String or false` (we could make another data type, but to save time I will not)\
**Description:** `To send a message to the given donor if they are not anonymous`

Now that you know it, put it in a comment:
```scheme
; email-donor : DonorName -> String or false
; To send a message to the given donor if they are not anonymous
```

Now that we have the signature, we can write some check expects
```scheme
(check-expect (email-donor DONORNAME1) "Thank you, Paul!")
(check-expect (email-donor DONORNAME2) false)
```

And finally, we can write the function itself, copying the template and replacing the `...`s
```scheme
(define (email-donor dn)
    (cond [(string? dn) (string-append "Thank you, " dn "!")]
          [(boolean? dn) false]))
```

# TL;DR (October 13 2020)
- Unions are useful for if you need to hold 2 different data types in the same spot
- Unions can be one data type or the other, but never both
- Unions are invisible to scheme, so scheme cannot enforce the types for us
- Unions can be separated using the `type?` functions, such as `string?` or `number?`
- Cond is very powerful for using unions. ie. the above function
- **ALWAYS** define at least 2 examples of the union if it has an infinite amount of possibilities [see Lab 2 Problem 4](#lab-2-problem-4)
- **If Possible** define all variants of the union (only for non infinite ones) [see Lab 2 Problem 2](#Lab-2-Problem-2)

[Jump to Table Of Contents](#file-ecs-notes-md)