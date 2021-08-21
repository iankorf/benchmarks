Computers
=========

Various machines around the house or lab.

## Machines ##

| Computer               | N | GHz | CPU               | Notes
|:-----------------------|:-:|:---:|:------------------|:----------------------
| Apple iMac Retina 2015 | 4 | 3.1 | Intel i5-5675R    | 
| Apple Mac Mini 2020    | 6 | 3.0 | Intel i5-8500B    | 
| Apple Mac Mini 2012    | 2 | 2.5 | Intel i5-3210M    |
| Apple MacBook Air 2017 | 2 | 1.8 | Intel i5-5350U    |
| Apple MacBook Air 2020 | 8 |     | Apple M1          |
| Lenovo IdeaPad 3       | 4 | 2.1 | AMD Ryzen 5 3500U |
| Lenovo Y710C           | 4 | 2.7 | Intel i5-6400     |
| spitfire               | 64| 2.5 | AMD Opteron 6380  |
| RPi model 4B           | 4 | 1.5 | ARMv7 rev 3       |
| RPi model 3B           | 4 | 1.2 | ARMv7 rev 4       |



## pybench ##

pybench is my benchmarking script tuned so that a speed of 1.0 represents
a Raspberry Pi 3B. There are 4 components designed to test different things.

+ SEQ - random sequence generation
+ I/O - write files, system calls
+ MER - dictionaries of k-mers
+ CMP - python loops and comparisons

It's amazing that depending on how python is built and how it interacts with the
system, the speed can be really different. Cygwin is the fastest for pure
python, but as soon as it interacts with the system, it's terrible. Haiku has a
slow python, but compiling and running C programs is as fast as anything (not
shown). Virtual machines sometimes outperform native OSes.

| Machine         | SEQ  | I/O  | MER  | CMP  | Ave  | Notes
|:----------------|:----:|:----:|:----:|:----:|:----:|:------------
| I3 Cygwin       | 10.0 |  0.2 |  6.4 |  6.4 |  5.7 |
| I3 VM Deb64     | 13.0 |  7.0 |  9.1 |  8.8 |  9.5 |
| I3 VM Ubuntu64  | 17.6 |  8.0 | 11.3 | 14.1 | 12.7 |
| Y710 Cygwin     | 12.2 |  0.2 |  8.0 | 11.1 |  7.9 | 
| Y710 VM Deb64   |  4.1 |  6.9 |  3.6 |  3.3 |  4.5 |
| Y710 VM Deb32   |  4.0 |  7.1 |  3.2 |  3.1 |  4.3 |
| Y710 VM Bodhi   |  5.5 |  7.1 |  3.6 |  3.2 |  4.9 |
| Y710 VM LLite   |  5.4 |  8.2 |  3.5 |  3.3 |  5.1 |
| Y710 VM RPi     |  4.1 |  7.3 |  3.1 |  3.3 |  4.5 |
| Y710 VM Haiku   |  1.3 |  0.2 |  1.3 |  1.2 |  1.0 | 
| iMac 2015 Deb   |
| MBA 2017        |  8.0 |  1.7 |  5.9 |  6.2 |  5.5 | 
| MBA 2017 vD64   |  8.0 |  4.3 |  8.2 | 10.3 |  7.7 | 
| MBA 2017 vHaiku |  1.8 |  0.3 |  2.0 |  2.1 |  1.5 | 
| MBA 2020        | 23.1 |  6.2 | 17.0 | 18.1 | 16.1 |
| Mini 2012 Mint  |
| Mini 2020       |
| Mini 2020 vMint |
| RPi 3B          |  1.0 |  1.0 |  1.0 |  1.0 |  1.0 |
| RPi 4B          |  2.8 |  1.3 |  2.8 |  3.7 |  2.7 |
| spitfire        |


