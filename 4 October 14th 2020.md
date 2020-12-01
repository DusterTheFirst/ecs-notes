# Text Editor v2
[Jump to TL;DR (summary)](#too-long-didnt-read-october-14-2020)\
[Jump to Table Of Contents](#file-1-ecs-notes-md)\
[Code for this lesson on wescheme](https://www.wescheme.org/openEditor?publicId=Cy6jDDBlgN)

In our previous text editor, we only used the text as the world state,
limiting us to not be able to move the cursor around the screen

Currently, we can only store data one at a time, it could be a union
(Such as a String **or** a Number) but it could never store both at
the same time.

To hold more than 1 data at a time, we can use *structures*

## Designing structures

### An address
When creating a structure, you should figure out what data you want to store.
For our example, we will create a structure to store an address. In an address,
we want to store a `house-number`, `city`, `street`, and `zipcode`.
As with all definitions, we want to start out with a comment describing it:
```scheme
; An Address is a (make-address Nat String String String Nat)
```
> Nat in this case is used to tell us that it is a natural number

In the code snippet, we specify the name, and then a function `make-address` to create
an address, now to define it in scheme to actually use, we can use the `define-struct` tool
```scheme
(define-struct address [house st city state zip])
```
Now, once we have `define-struct`, we can create one using the automatically created `make-address`
function.
```scheme
(make-address false "hello" 2 -7 true)
```
and that would return
```scheme
(address false "hello" 2 -7 true)
```
> Notice that this does not match our comment, but scheme cant read our comment, so it doesn't know better.

To make sure that we match our address definition, we can make some samples and a more detailed
description of the structure.

The more detailed description looks like:
```scheme
; and represents someone's address
; - where house is the house number
; - st s the name of the street
; - city is the name of the city
; - state is the abbreviation for the state
; - and zip is the zip code
```
and would be placed after the structure definition.

Now that we have a good description, we can make some samples for reference
```scheme
(define ADDRESS1 (make-address 50 "Rice St" "Wellesley" "MA" 02482))
(define ADDRESS2 (make-address 1 "a" "b" "c" 7))
```

Now that we have the structure defined, we need a way to access the different members of it.
Lucky for us, Scheme creates a bunch of helper functions for us:
```scheme
(address-<field> address)
```
where `<field>` is replaced by the name of the field defined above. ie.
```scheme
(address-house ADDRESS1)
```
would return 50, since it is the value we put in the structure when we made it
or "constructed it"

We can put all of these helper methods together into a template for future use
```scheme
(define (address-template a)
    (... (address-house a)
         (address-st a)
         (address-city a)
         (address-state a)
         (address-zip a) ...))
```
> Remember, the ...s are there for us to replace later when we copy the template function.

Another helper function created for us is the `address?` function which lets us check if
a type is an address. 
```scheme
(address? ADDRESS1) ; true
(address? (make-address false false false false false)) ; also true
(address? 3) ; false
```
> The second example returned true because scheme does not know about our capitol A Address type and does
not know that we want the fields to be specific types. Because of that, as long as we made a structure using
the `make-address` function scheme will see it as a structure

### Making a structure that uses another structure
Now that we have the address structure created, we can make a student structure that uses our address structure
as one of the fields. To start making our student structure, which will hold a name, year of graduation, and an address we start with the comment to describe it:
```scheme
; A Student is a (make-stdnt String Nat Address)
```
> We are going to name our structure `stdnt` to help show that the name of the structure can be whatever you want

Once we have the comment, we need to tell scheme about it, using the `define-struct` tool
```scheme
(define-struct stdnt [name gradyr house])
```
> Remember the names can be anything we want, but we need to use the same ones defined here
later in our project, ***NOT* the data type**

Once we have the structure defined for scheme, we now need to describe each field
```scheme
; and represents a student
; - where name is the student's full name
; - grad-yr is the student's graduation year
; - and house is the address where the student lives
```

Now, we define 2 sample students:
```scheme
(define STUDENT1 (make-stdnt "Sheev" 4 ADDRESS1))
(define STUDENT2 (make-stdnt "Alice" 1234567789 ADDRESS2))
```

As always, after setting up the struct and creating the samples, we should
create a template for us to use later.
```scheme
(define (student-template s)
  (... (stdnt-name s)
       (stdnt-grad-yr s)
       (address-template (stdnt-house s)) ...))
```
> Notice how in this template, we also use the address-template. That is because the house
member of the `student` structure is an `address` structure, so we need to use the tools from the address-template
to get the data out of the address

## Using a structure in a function
What if we want to use our new fandangled structure in a function? Well, lets try it out!
As always, we can start by making a function, say one that adds one to a student's
year-of-graduation (holds them back)

### Holding a student back
As always, start by laying out the function you want.

**Name:** `stay-back`\
**Input:** `Student`\
**Output:** `Student`\
**Description:** `Adds 1 to a student's graduation year.`

And now we can put that into a nice comment for us to read:
```scheme
; stay-back : Student -> Student
; Adds 1 to a Student's graduation year
```

Once we have the comment for the function, we can create (at least) 2 check-expect tests
to verify that it is working how we expect.
```scheme
(check-expect
    (stay-back STUDENT1)
    (make-stdnt "Sheev" 5 ADDRESS1))
(check-expect
    (stay-back STUDENT2)
    (make-stdnt "Alice" 123456790 ADDRESS2))
```

Okay, that all looks great, now we have to define the function:
```scheme
(define (stay-back s)
    (+ 1 (stdnt-gradyr s)))
```
> This above code with not work, remember **you cannot modify a structure**. In order to make
a change, you have to create a whole new one, created from the old one with the new value in place of the old.

Heres how you would do that:
```scheme
(define (stay-back s)
    (make-stdnt (stdnt-name s) (+ 1 (stdnt-gradyr s)) (stdnt-house s)))
```
> Notice that we have to re-create the structure with `make-stdnt` but with the difference being
that the gradyr is now one more than the given

## Changing the zip code
As always, start by laying out the function you want.
> I know it can get repetitive, but your later self with thank you

**Name:** `update-zip-for-student`\
**Input:** `Student and Nat`\
**Output:** `Student`\
**Description:** `Update a student's zip code to be a new, given a new zip code`

And now as a nice concise comment
```scheme
; update-zip-for-student : Student Nat -> Student
; Update a student's zip code to be a new, given a new zip code
```

Now that we have the function all layed out, we can start with some check-expects
```scheme
(check-expect
    (update-zip-for-student STUDENT1 12345)
    (make-stdnt "Sheev" 4
        (make-address 50 "Rice St" "Wellesley" "MA" 12345)))
(check-expect
    (update-zip-for-student STUDENT2 98765)
    (make-stdnt "Alice" 123456789
        (make-address 1 "a" "b" "c" 98765)))
```
> Looks normal, and it is, all that changes is the zip code. This should be easy, right?

Well yes, but we have a lot of writing to do. We can define our function, copying the student template,
but, we cant just update the zip by replacing the last parameter with a new zip code, cause it takes in a whole
structure. We need to make another function that can update the zip in the structure for us.

> Whenever you write a function, try to keep it limited to using only one data type at a time. In our case, we
only use the student structure in this function, and we will make another `update-zip` function to handle the
address structure
```scheme
(define (update-zip-for-student s new-zip)
  (make-stdnt (stdnt-name s)
              (stdnt-grad-yr s)
              (update-zip (stdnt-house s) new-zip)))
```

Now, its time to make the update-zip function. Ill go quick with this one, assuming
you have gotten faster with them aswell.
```scheme
; update-zip : Address Nat -> Address
; Update the zip code for this address to the given #
```
**Bam**, theres our signature and description

```scheme
(check-expect
    (update-zip ADDRESS1 02020)
    (make-address 50 "Rice St" "Wellesley" "MA" 02020))
(check-expect
    (update-zip ADDRESS2 13579)
    (make-address 1 "a" "b" "c" 13579))
```
**Whamo**, we have some check expects

And then we can, very simply, just create the `update-zip` function
```scheme
(define (update-zip a new-zip)
    (make-address
        (address-house a)
        (address-st a)
        (address-city a)
        (address-state a)
        new-zip))
```
It may look like a lot of code, but if you break it down, all it does is create a new
address, give it the house, st, city, and state of the old address, and just replace the
zip with the new zip

## Tying it together into a text editor
Now that we have learned to use structures, we can put them to good use. We can use them in our
text editor. Remember when we had our text editor, it could type and delete, but you could not move
the cursor around. That was because our world state was a single string: The text that was in the editor.
We had no way of storing the cursor position. Well, using these new hot structures that we have learned
about, that is all about to change.

So. first thing you do with any data type, function, or struct is a simple, one line comment describing it.
In our case, we will make a structure called `TextEditor` or `te` for short with the text and cursor position
as members. We can write this out in a comment like so:
```scheme
; A TextEditor is a (make-te String Nat)
```

Now that we know about the text editor, we need to tell scheme about it. (remember, anything after a `;` is
invisible to scheme and is only for us to read).

We can define the struct as such:
```scheme
(define-struct te [text cursor])
```

And now we can describe the types in the text editor further
```scheme
; and represents a text editor
; - where text is the text you have typed
; - and cursor is the index of the cursor
```

<details>
<summary>All together they will look as such:</summary>

```scheme
; A TextEditor is a (make-te String Nat)
(define-struct te [text cursor])
; and represents a text editor
; - where text is the text you have typed
; - and cursor is the index of the cursor
```

</details>

Now that we have the struct created and layed out. We need to make 2 samples:
```scheme
(define TE1 (make-te "hello" 1))
(define TE2 (make-te "ECS" 0))
```

Although we don't have time to implement it into our text editor but we can make a simple
function that we may be able to use as the on key handler for our big-bang program. Since it
will handle key events, it take in our world state, in this case the `TextEditor` structure and the key event.
```scheme
; insert-text : TextEditor KeyEvent -> TextEditor
; Insert text the user typed at the cursor's location
```
An example check expect could exist as such:
```scheme
(check-expect (insert-text TE1 "a")
              (make-te "haello" 2))
```

# Too Long; Didn't Read (October 14, 2020)
- Structures are a way to store more than one data piece in the same place
- Structures can be created like so:
```scheme
(make-struct my-struct-name [field1-name field2-name ...])
```
- When using structures, you can use the generated function `<name-of-structure>-<name-of-field>`
where `<name-of-structure>` is replaced with the name of your structure. (ex: `address`) and
`<name-of-field>` is replaced with the name of the field that you want to read. (ex: `st`). So
to access an address's st(reet), we can use the helper function `(address-st a)`
- When using structures in a function, only access one data type at a time, make different functions
for deeply nested data, such as the address inside of the student [see: Changing the zip code](#changing-the-zip-code)
- ALL DATA IN SCHEME IS IMMUTABLE (unable to be mutated (changed))
    - To be able to modify a structure, you have to create a whole new one with the new data [see:  Holding a student back](#holding-a-student-back)
- Scheme is very lax and does not enforce the types you want in your structures, you have to be
weary of that and enforce it yourself

[Jump to Table Of Contents](#file-1-ecs-notes-md)