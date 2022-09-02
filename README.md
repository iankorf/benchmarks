Benchmarks
==========

Computer, language, and algorithm benchmarks


Computer
--------

Run a suite of programs through different computers to see how fast they run.

+ Int
+ Float
+ Pointers
+ I/O


Language
--------

Implement the same algorithm in multiple computers.


Algorithm
---------

Comparisons of different ways to find overlapping features.

+ overlap_1a.py - file-by-file, line-by-line
+ overlap_1b.py - fancy file-based
+ overlap_2a.py - 2 files in memory
+ overlap_2b.py - 1 file in memory
+ overlap_3.py - 2 files indexed by chromosome
+ overlap_4.py - 2 files indexed by chromosome and _zipcode_
+ overlap_5.py - 1 file binary search
+ overlap_6.py - 2 files sorted


Instructions
------------

```
git clone https://github.com/iankorf/benchmarks
git clone https://github.com/KorfLab/algorithms
# probably some go-build thing here...
git clone https://github.com/KorfLab/genomikon
cd genomikon
make
cd ../benchmarks
python3 benchmark.py
```







