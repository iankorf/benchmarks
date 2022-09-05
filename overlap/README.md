Overlap Problem
===============

Given two files in GFF, BED, or some related format, which _features_ overlap
other features? For our purposes, a feature has 3 values.

+ chromosome
+ beginning coordinate
+ ending coordinate

A feature file is a plain text file where each line represents a separate
record. Records may appear in any order and their coordiantes may overlap. For
example:

```
chrA 100 200
chrA 300 400
chrA 500 600
chrB 100 200
chrA 200 700
```

A program that solves the overlap problem reads in 2 files and reports which
features in file 1 overlap which features in file 2. For example, the command
line might look like the following:

```
python3 find_overlaps.py file1 file1
```

There are several ways to solve the problem. When writing code, one must choose
among several design goals.

+ Correct - it solves the problem
+ Robust - it always solves the problem
+ Simple - the code is easy to read and not complicated
+ Low memory - it doesn't use much memory
+ High speed - it doesn't take much time
+ Elegant - the code is beautiful
+ Clever - the algorithm is beautiful

Each choice of algorithm makes some compromises on these design goals. This
table summarizes a handful of solutions to the problem. See the specific notes
farther below.

| P# | Li | Wor | Char | Mem  | b1k   | b10k  |  v10k | v100k |
|:--:|:--:|:---:|:----:|:----:|------:|:-----:|:-----:|:-----:|
| 01 | 19 |  60 |  390 | Low  | 2.038 |  201  |  107  |   ND  |
| 02 | 12 |  47 |  338 | Low  | 1.985 |  193  |  175  |   ND  |
| 03 | 28 |  90 |  566 | High | 0.716 |   68  |   56  |   ND  |
| 04 | 16 |  62 |  379 | Med  | 0.574 |   53  |   33  |   ND  |
| 05 | 91 | 337 | 1866 | Med  | 0.164 |   49  | 0.727 |  135  |
| 06 | 27 |  88 |  598 | High | 0.592 |   55  | 2.778 |  291  |
| 07 | 45 | 162 | 1074 | High | 0.061 | 0.324 | 0.948 | 2.002 |
| 08 | 44 | 142 |  998 | Huge | 6.847 |   11  |   ND  |   ND  |
| 09 |


Testing Procedures
------------------

The first test files (b1k) are 1000 features in the size of a typical bacterial
genome.

```
python3 randomfeatures.py --chroms 1 --length 4500000 --features 1000
```

None of the tests take very long. The big loser is the bucket sort because it
spends a long time creating a data structure that it only uses 1000 times.
Another "loser" is the chromosome index, which fares no better than a
record-by-record approach because there is only 1 chromosome.


The second test (b10k) is similar to the above, but the files are each 10x
larger, making the problem 100x larger.

```
python3 randomfeatures.py --chroms 1 --length 4500000 --features 10000
```

Here, the bucket sort solution works very well. However, the positional
indexing is the fastest.

This third test (v10k) mimics something like a vertebrate genome with 3 billion
bp and 20 chromosomes. Again, the files are 10k each.

```
python3 randomfeatures.py --chroms 20 --length 150000000 --features 10000
```

Here, the binary search is fastest because the data is so sparse. There wasn't
enough RAM to run the bucket sort.


The fourth test (v100k) is like the above with 100k features. The positional
index is more than 100x faster than any other algorithm.



01_file_ugly
------------

A novice programmer might come up with this solution. One file is read in
line-by-line and the compared to another file, line-by-line. It would be very
hard to mess up this code.

Advantages:

+ Simple
+ Low memory (except as noted below)

Disadvantages:

- Slow
- Ugly

Notes:

In most languages, this solution would use very little memory because only 2
features (lines) are in memory at any one time. However, python's `readlines()`
reads an entire file into memory and then hands back one line at a time. For
this reason, it may be better to use `readline()`, which only reads one line.
You'll have to roll your own iterator. This comment about memory applies to
several of the programs here.


02_file_pretty
--------------

A more experienced programmer might write a file-by-file comparison like this.
Note that nothing has really changed. The difference is that the code looks
prettier.

Advantages:

+ Simple
+ Low memory
+ Elegant

Disadvantages:

- Slow


03_arrays
---------

An intermediate programmer enamored with functions might write functions to
read, compare, and output features. In the example, each feature is represented
as a tuple (a dictionary would also be appropriate, and is often more
appropriate). Note that this solution is still just comparing features in 2
nested loops. The primary advantage is that one doesn't have to open and close
files over and over. This represents a small increase in speed (about 2-fold).

Advantages:

+ Simple
+ Elegant

Disadvantages:

- Slow
- High memory


04_array
--------

An intermediate programmer concerned with efficiency might write code like
this. They recognize that only one file needs to be in memory. Also, since
there's some overhead in function calls, the code would run faster if they were
removed. This solution uses less memory and CPU than any of the previous.
However, it is still very slow because the algorithm hasn't really changed from
a line-by-line approach.

Advantages:

+ Simple

Disadvantages:

- Slow
- Medium memory


05_binary
---------

Every CS student learns that binary search is much more efficent than linear. A
knee-jerk solution is to sort one list of features and use a binary search to
find overlaps. One problem is that features don't sort perfectly. Is a feature
than spans an entire chromosome at the start or end of a sorted list? Another
problem is that there may be many overlaps. The code must therefore "seed" a
search and then extend it. The extension is effectively a linear search and
uses a heuristic for feature size. The implementation here works 99.9% of the
time, but there are unusual cases where it fails.

Advantages:

+ Faster
+ Clever

Disadvantages:

- Complex
- Buggy
- Medium memory


06_chromindex
-------------

A simple way to improve the `03_arrays` solution is to index each feature by
its chromosome. Instead of storing the features in arrays, they are stored in a
dictionary of arrays. The advantage is that that you never have to compare
features on different chromosomes. For a genome with 20 chromosomes, the search
space for each chromosome is 1/400th the size of the entire search space. In
other words, the algorithm is about N times faster, where N is the number of
chromosomes.

The code is only a few lines longer, but novice programmers may not understand
how to use a 2-dimenstional data structure (dictionary of arrays).

Advantages:

+ Much faster
+ Moderate complexity

Disadvantages:

- High memory
+ Confusing to novices


07_posindex
-----------

This solution extends the previous one by indexing the position along the
chromosome. You can think of this as each part of a chromosome having its own
zip code. Features that exist in more than one zip code represent a problem.
The code here checks the output and doesn't report anything twice. This has the
disadvantage of not reporting duplicate features (not that there _should_ be
duplicate features).

Advantages:

+ Very fast

Disadvantages:

- High memory
- Moderately complex


08 bucketsort
-------------

Since chromosomes have fixed lengths, they are a good candidate for a bucket
sort strategy. Well, except that chromosomes are HUGE. This solution might work
well if the chromosomes were small and the number of lookups was large.

Advantages:

+ Very fast after indicies are built

Disadvantages:

- Extremely high memory
- Initial indexing is slow
- Complex


09_doublesort
-------------

All of the previous solutions involve some kind of NxM comparison of features,
whether that's in an entire file, chromosome, or zip code. An alternative is to
sort both lists of features and then navigate them simultaneously, from
beginning to ending.

Advantages:

+ Very fast

Disadvantages:

- High memory
- Complex
- Unusual algorithm
