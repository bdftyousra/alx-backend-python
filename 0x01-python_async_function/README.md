# :book: 0x00. 0x01. Python - Async
## :page_with_curl: Topics Covered
1. Python Async.

# :computer: Tasks.
## [0. The basics of async](0-basic_async_syntax.py)
### :page_with_curl: Task requirements.
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.
```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 0-basic_async_syntax.py
chmod +x 0-basic_async_syntax.py
./0-basic_async_syntax.py

# Lint checks
pycodestyle 0-basic_async_syntax.py
mypy 0-basic_async_syntax.py

# Tests
touch 0-main.py
chmod +x 0-main.py
./0-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 0-basic_async_syntax.py](0-basic_async_syntax.py)


## [1. Let's execute multiple coroutines at the same time with async](1-concurrent_coroutines.py)
### :page_with_curl: Task requirements.
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.
```
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

The output for your answers might look a little different and that’s okay.
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 1-concurrent_coroutines.py
chmod +x 1-concurrent_coroutines.py
./1-concurrent_coroutines.py

pycodestyle 1-concurrent_coroutines.py
mypy 1-concurrent_coroutines.py

# Tests
touch 1-main.py
chmod +x 1-main.py
./1-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 1-concurrent_coroutines.py](1-concurrent_coroutines.py)


## [2. Measure the runtime](2-measure_runtime.py)
### :page_with_curl: Task requirements.
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 2-measure_runtime.py
chmod +x 2-measure_runtime.py
./2-measure_runtime.py

pycodestyle 2-measure_runtime.py
mypy 2-measure_runtime.py

# Tests
touch 2-main.py
chmod +x 2-main.py
./2-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 2-measure_runtime.py](2-measure_runtime.py)


## [3. Tasks](3-tasks.py)
### :page_with_curl: Task requirements.
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.
```
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
<class '_asyncio.Task'>
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 3-tasks.py
chmod +x 3-tasks.py
./3-tasks.py

pycodestyle 3-tasks.py
mypy 3-tasks.py

# Tests
touch 3-main.py
chmod +x 3-main.py
./3-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 3-main.py](3-tasks.py)


## [4. Tasks](4-main.py)
### :page_with_curl: Task requirements.
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.
```
bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 4-tasks.py
chmod +x 4-tasks.py
./4-tasks.py

pycodestyle 4-tasks.py
mypy 4-tasks.py

# Tests
touch 4-main.py
chmod +x 4-main.py
./4-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 4-main.py](4-main.py)


## [5. Complex types - list of floats](5-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.
```
bob@dylan:~$ cat 5-main.py
#!/usr/bin/env python3

sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))

bob@dylan:~$ ./5-main.py
True
{'input_list': typing.List[float], 'return': <class 'float'>}
sum_list(floats) returns 6.470000000000001 which is a <class 'float'>
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 5-sum_list.py
chmod +x 5-sum_list.py
./5-sum_list.py

# Tests
touch 5-main.py
chmod +x 5-main.py
./5-main.py

# Lint
pycodestyle 5-sum_list.py
mypy 5-sum_list.py
```

### :heavy_check_mark: Solution
> [:point_right: 5-main.py](5-main.py)


## [0. Basic annotations - add](5-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
```
bob@dylan:~$ cat 5-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./5-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 6-sum_mixed_list.py
chmod +x 6-sum_mixed_list.py
./6-sum_mixed_list.py

# Tests
touch 6-main.py
chmod +x 6-main.py
./6-main.py

# Lint
pycodestyle 6-sum_mixed_list.py
mypy 6-sum_mixed_list.py
```

### :heavy_check_mark: Solution
> [:point_right: 5-main.py](5-main.py)


## [7. Complex types - string and int/float to tuple](7-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.
```
bob@dylan:~$ cat 7-main.py
#!/usr/bin/env python3

to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))

bob@dylan:~$ ./7-main.py
{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
('eggs', 9)
('school', 0.0004)
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 7-to_kv.py
chmod +x 7-to_kv.py
./7-to_kv.py

# Tests
touch 7-main.py
chmod +x 7-main.py
./7-main.py

# Lint
pycodestyle 7-to_kv.py
mypy 7-to_kv.py
```

### :heavy_check_mark: Solution
> [:point_right: 7-main.py](7-main.py)


## [8. Complex types - functions](8-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

```
bob@dylan:~$ cat 8-main.py
#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))

bob@dylan:~$ ./8-main.py
{'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
4.928400000000001
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 8-make_multiplier.py
chmod +x 8-make_multiplier.py
./8-make_multiplier.py

# Tests
touch 8-main.py
chmod +x 8-main.py
./8-main.py

# Lint
pycodestyle 8-make_multiplier.py
mypy 8-make_multiplier.py
```

### :heavy_check_mark: Solution
> [:point_right: 8-main.py](8-main.py)


## [9. Let's duck type an iterable object](9-main.py)
### :page_with_curl: Task requirements.
Annotate the below function’s parameters and return values with the appropriate types
```
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

```
bob@dylan:~$ cat 9-main.py 
#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)

bob@dylan:~$ ./9-main.py 
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 9-element_length.py
chmod +x 9-element_length.py
./9-element_length.py

# Tests
touch 9-main.py
chmod +x 9-main.py
./9-main.py

# Lint
pycodestyle 9-element_length.py
mypy 9-element_length.py
```

### :heavy_check_mark: Solution
> [:point_right: 9-main.py](9-main.py)


## [10. Duck typing - first element of a sequence](100-basic_async_syntax.py)
### :page_with_curl: Task requirements.
Augment the following code with the correct duck-typed annotations:
```
# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```

```
bob@dylan:~$ cat 100-basic_async_syntax.py 
#!/usr/bin/env python3

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)

bob@dylan:~$ ./100-basic_async_syntax.py 
{'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 100-safe_first_element.py
chmod +x 100-safe_first_element.py
./100-safe_first_element.py

# Tests
touch 100-basic_async_syntax.py
chmod +x 100-basic_async_syntax.py
./100-basic_async_syntax.py

# Lint
pycodestyle 100-safe_first_element.py
mypy 100-safe_first_element.py
```

### :heavy_check_mark: Solution
> [:point_right: 100-basic_async_syntax.py](100-basic_async_syntax.py)


## [11. More involved type annotations](101-main.py)
### :page_with_curl: Task requirements.
Given the parameters and the return values, add type annotations to the function

Hint: look into TypeVar
```
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
```

```
bob@dylan:~$ cat 101-main.py 
#!/usr/bin/env python3

safely_get_value = __import__('101-safely_get_value').safely_get_value
annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print( ("{}: {}".format(k, v)))

bob@dylan:~$ ./101-main.py 
Here's what the mappings should look like
dct: typing.Mapping
key: typing.Any
default: typing.Union[~T, NoneType]
return: typing.Union[typing.Any, ~T]
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 101-safely_get_value.py
chmod +x 101-safely_get_value.py
./101-safely_get_value.py

# Tests
touch 101-main.py
chmod +x 101-main.py
./101-main.py

# Lint
pycodestyle 101-safely_get_value.py
mypy 101-safely_get_value.py
```

### :heavy_check_mark: Solution
> [:point_right: 101-main.py](101-main.py)


## [0. Basic annotations - add](102-measure_runtime.py)
### :page_with_curl: Task requirements.
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
```
bob@dylan:~$ cat 102-measure_runtime.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./102-measure_runtime.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 102-type_checking.py
chmod +x 102-type_checking.py
./102-type_checking.py

# Tests
touch 102-measure_runtime.py
chmod +x 102-measure_runtime.py
./102-measure_runtime.py

# Lint
pycodestyle 102-type_checking.py
mypy 102-type_checking.py
```

### :heavy_check_mark: Solution
> [:point_right: 102-measure_runtime.py](102-measure_runtime.py)