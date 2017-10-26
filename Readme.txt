Author: Aditya Geria
School: Rutgers University - New Brunswick
Class of 2018
KPCB Fellows Engineering Program Summer 2018

I was able to successfully complete the challenge problems under the given constraints, provided
the assumptions I list in "chainedhashmap.py" hold true. This program uses Python 2

This implementation uses chaining, which means that when a collision happens with keys,
the table will still add the value in the table under ".next" in the chain. Refer to the diagram
below for explanation:

[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] <-- Hash table, currently empty

[ ] [3] [ ] [ ] [ ] [ ] [7] [ ] [ ] [1] <-- Hash table, some values inserted

[ ] [3] [ ] [ ] [ ] [ ] [7] [ ] [ ] [1] <-- Collision happens with index 1 at value 3 when we try to insert 13
     X
    [13]
[ ] [3] [ ] [ ] [ ] [ ] [7] [ ] [ ] [1] <-- Hash table, after collision is resolved
     V
    [13]
[ ] [3] [ ] [ ] [ ] [ ] [7] [ ] [ ] [1] <-- Hash table, collision happens with index 1 at value 3 when we try to insert 33
     V
    [13]
     X
    [33]
[ ] [3] [ ] [ ] [ ] [ ] [7] [ ] [ ] [1] <-- Hash table, after collision is resolved
     V
    [13]
     V
    [33]

This means that when we delete at the key of index 1 (where 3, 13 and 33 are), all values will be deleted. This can
easily be changed if we wish to match by value by iterating through the chain and finding the specific value.
When we use get() the first value in the chain will always be returned, but the chain can be traversed to find the
rest of the chain.

Runtime:
    Insert/Set:
        -Best case: O(1) insert, when the bucket is empty.
        -Worst case: O(n) insert, if all elements hash to the same key, they will be placed on a chain
    Get:
        -All cases O(1) - this is simply a return operation
    Delete:
        -All cases O(1) - this is a reset operation
        -Can also be O(n) if a whole chain must be deleted because we need to count how many values the table lost
        for load factor analysis

Running the program:
Simply run “python hashtest.py” in the command line to execute a series of insert/get/delete tests.
