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
| ASROCK M8              |   |     |                   |
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

| Machine      | SEQ | I/O | MER | CMP | Sum | Notes
|:-------------|:---:|:---:|:---:|:---:|:---:|:------------
| I3           | 
| Y710 Cygwin  |12.2 | 0.2 | 8.0 |11.1 | 7.9 | 7.5s make test
| Y710 Deb64   | 4.1 | 6.9 | 3.6 | 3.3 | 4.5
| Y710 Deb32   | 4.0 | 7.1 | 3.2 | 3.1 | 4.3
| Y710 Bodhi   | 5.5 | 7.1 | 3.6 | 3.2 | 4.9
| Y710 LLite   | 5.4 | 8.2 | 3.5 | 3.3 | 5.1
| Y710 RPi     | 4.1 | 7.3 | 3.1 | 3.3 | 4.5
| Y710 Haiku   | 1.3 | 0.2 | 1.3 | 1.2 | 1.0 | 7.0s make test
| iMac 2015    |
| MBA 2017     |
| MBA 2020     |
| Mini 2012    |
| Mini 2020    |
| Mini 2020 VM |
| RPi 3B       |  1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| RPi 4B       |  2.8 | 1.3 | 2.8 | 3.7 | 2.7 |
| spitfire     |

