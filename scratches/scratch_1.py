def printresults(**kwargs):
    """
    prints results formatting dinamically the variables received

    syntax:
        printresults(varname=varvalue, ...)
    """
    fstrings = []
    for k, v in kwargs.items():
        fstrings.append(f'{k} = {v}')
        #print(fstrings)
    print("\tRESULTS: ", ", ".join(fstrings))


print(
"""
My apologies for the length of this post, but I decided to opt for completeness.
Once you know a few basic rules, it's not hard to generalize them. I'll do my best to explain with a few examples.
Since you're talking about evaluating these "by hand," I'll suggest some simple substitution rules.
Basically, you might find it easier to understand an expression if all the iterables are formatted in the same way.

For the purposes of unpacking only, the following substitutions are valid on the right side of the `=` (i.e. for _rvalues_):

    'XY' -> ('X', 'Y')
    ['X', 'Y'] -> ('X', 'Y')

If you find that a value doesn't get unpacked, then you'll undo the substitution. (See below for further explanation.)

Also, when you see "naked" commas, pretend there's a top-level tuple.
Do this on both the left and the right side (i.e. for _lvalues_ and _rvalues_):

    'X', 'Y' -> ('X', 'Y')
    a, b -> (a, b)

With those simple rules in mind, here are some examples:

    (a,b), c = "XY", "Z"'
""")

#code = '(a,b), c = "XY", "Z"'
#exec(code)
(a,b), c = "XY", "Z"                 # a = 'X', b = 'Y', c = 'Z'
printresults(a=a, b=b, c=c)

print(
"""
Applying the above rules, we convert `"XY"` to `('X', 'Y')`, and cover the naked commas in parens:

    ((a, b), c) = (('X', 'Y'), 'Z')
""")
((a, b), c) = (('X', 'Y'), 'Z')
printresults(a=a, b=b, c=c)

print(
"""
The visual correspondence here makes it fairly obvious how the assignment works.
Here's an erroneous example:

    (a,b), c = "XYZ"
""")
try:
    (a,b), c = "XYZ"
except ValueError as ve:
    print(f"""
    ERROR: {ve}
    correct version:
    (a,b), c = "XY", "Z"
    """)
    (a,b), c = "XY", "Z"
    printresults(a=a, b=b, c=c)

print("""
Following the above substitution rules, we get the below:

    ((a, b), c) = ('X', 'Y', 'Z')
""")
try:
    ((a, b), c) = ('X', 'Y', 'Z')
except ValueError as ve:
    print(f"""
    ERROR: {ve}
    correct version:
    ((a, b), c) = ('X', 'Y'), 'Z'
    """)
    ((a, b), c) = ('X', 'Y'), 'Z'
    printresults(a=a, b=b, c=c)

print(
"""
This is clearly erroneous; the nested structures don't match up. Now let's see how it works for a slightly more complex example:

    (a,b), c, = [1,2],'this'             # a = '1', b = '2', c = 'this'
""")
(a,b), c, = [1,2],'this'             # a = '1', b = '2', c = 'this'
printresults(a=a, b=b, c=c)

print("""
Applying the above rules, we get

    ((a, b), c) = ((1, 2), ('t', 'h', 'i', 's'))
""")
((a, b), c) = ((1, 2), ('t', 'h', 'i', 's'))
printresults(a=a, b=b, c=c)

print("""
But now it's clear from the structure that `'this'` won't be unpacked, but assigned directly to `c`. So we undo the substitution.

    ((a, b), c) = ((1, 2), 'this')
""")
((a, b), c) = ((1, 2), 'this')
printresults(a=a, b=b, c=c)

print("""
Now let's see what happens when we wrap `c` in a tuple:

    (a,b), (c,) = [1,2],'this'           # ERROR -- too many values to unpack
""")
try:
    (a, b), (c,) = [1, 2], 'this'
except ValueError as ve:
    print(f"""
    ERROR: {ve}
    correct version:
    """)
exit()

"""
Becomes

    ((a, b), (c,)) = ((1, 2), ('t', 'h', 'i', 's'))

Again, the error is obvious. `c` is no longer a naked variable, but a variable inside a sequence, and so the corresponding sequence on the right is unpacked into `(c,)`. But the sequences have a different length, so there's an error.

Now for extended unpacking using the `*` operator. This is a bit more complex, but it's still fairly straightforward. A variable preceded by `*` becomes a list, which contains any items from the corresponding sequence that aren't assigned to variable names. Starting with a fairly simple example:

    a, *b, c = "X...Y"                   # a = 'X', b = ['.','.','.'], c = 'Y'

This becomes

    (a, *b, c) = ('X', '.', '.', '.', 'Y')

The simplest way to analyze this is to work from the ends. `'X'` is assigned to `a` and `'Y'` is assigned to `c`. The remaining values in the sequence are put in a list and assigned to `b`.

Lvalues like `(*a, b)` and `(a, *b)` are just special cases of the above. You can't have two `*` operators inside one lvalue sequence because it would be ambiguous. Where would the values go in something like this `(a, *b, *c, d)` -- in `b` or `c`? I'll consider the nested case in a moment.

    *a = 1                               # ERROR -- target must be in a list or tuple

Here the error is fairly self-explanatory. The target (`*a`) must be in a tuple.

    *a, = (1,2)                          # a = [1,2]

This works because there's a naked comma. Applying the rules...

    (*a,) = (1, 2)

Since there are no variables other than `*a`, `*a` slurps up all the values in the rvalue sequence. What if you replace the `(1, 2)` with a single value?

    *a, = 1                              # ERROR -- 'int' object is not iterable

becomes

    (*a,) = 1

Again, the error here is self-explanatory. You can't unpack something that isn't a sequence, and `*a` needs something to unpack. So we put it in a sequence

    *a, = [1]                            # a = [1]

Which is eqivalent to

    (*a,) = (1,)

Finally, this is a common point of confusion: `(1)` is the same as `1` -- you need a comma to distinguish a tuple from an arithmetic statement.

    *a, = (1)                            # ERROR -- 'int' object is not

Now for nesting. Actually this example wasn't in your "NESTED" section; perhaps you didn't realize it was nested?

    (a,b), *c = 'XY', 2, 3               # a = 'X', b = 'Y', c = [2,3]

Becomes

    ((a, b), *c) = (('X', 'Y'), 2, 3)

The first value in the top-level tuple gets assigned, and the remaining values in the top-level tuple (`2` and `3`) are assigned to `c` -- just as we should expect.

    (a,b),c = 1,2,3                      # ERROR -- too many values to unpack
    *(a,b), c = 1,2,3                    # a = 1, b = 2, c = 3

I've already explained above why the first line throws an error. The second line is silly but here's why it works:

    (*(a, b), c) = (1, 2, 3)

As previously explained, we work from the ends. `3` is assigned to `c`, and then the remaining values are assigned to the variable with the `*` preceding it, in this case, `(a, b)`. So that's equivalent to `(a, b) = (1, 2)`, which happens to work because there are the right number of elements. I can't think of any reason this would ever appear in working code. Similarly,

    *(a, *b), c = 'this'                 # a = 't', b = ['h', 'i'], c = 's'

becomes

    (*(a, *b), c) = ('t', 'h', 'i', 's')

Working from the ends, `'s'` is assigned to `c`, and `('t', 'h', 'i')` is assigned to `(a, *b)`. Working again from the ends, `'t'` is assigned to `a`, and `('h', 'i')` is assigned to b as a list. This is another silly example that should never appear in working code.
"""
