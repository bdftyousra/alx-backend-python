# :book: 0x00. Python - Variable Annotations
## :page_with_curl: Topics Covered
1. Python Type Annotation.

# :computer: Tasks.
## [0. Basic annotations - add](0-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 0-add.py
chmod +x 0-add.py
./0-add.py

# Lint checks
pycodestyle 0-add.py
mypy 0-add.py

# Tests
touch 0-main.py
chmod +x 0-main.py
./0-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 0-main.py](0-main.py)


## [1. Basic annotations - concat](1-concat.py)
### :page_with_curl: Task requirements.
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
```
bob@dylan:~$ cat 1-concat.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./1-concat.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 1-concat.py
chmod +x 1-concat.py
./1-concat.py

pycodestyle 1-concat.py
mypy 1-concat.py

# Tests
touch 1-main.py
chmod +x 1-main.py
./1-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 1-concat.py](1-concat.py)


## [2. Basic annotations - floor](2-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.
```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

bob@dylan:~$ ./2-main.py
True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) returns 3, which is a <class 'int'>
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 2-floor.py
chmod +x 2-floor.py
./2-floor.py

pycodestyle 2-floor.py
mypy 2-floor.py

# Tests
touch 2-main.py
chmod +x 2-main.py
./2-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 2-main.py](2-main.py)


## [3. Basic annotations - to string](3-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.
```
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))

bob@dylan:~$ ./3-main.py
True
{'n': <class 'float'>, 'return': <class 'str'>}
to_str(3.14) returns 3.14, which is a <class 'str'>
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 3-to_str.py
chmod +x 3-to_str.py
./3-to_str.py

pycodestyle 3-to_str.py
mypy 3-to_str.py

# Tests
touch 3-main.py
chmod +x 3-main.py
./3-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 3-main.py](3-main.py)


## [4. Define variables](4-main.py)
### :page_with_curl: Task requirements.
Define and annotate the following variables with the specified values:

  * a, an integer with a value of 1
  * pi, a float with a value of 3.14
  * i_understand_annotations, a boolean with a value of True
  * school, a string with a value of “Holberton”
```
bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))

bob@dylan:~$ ./4-main.py
a is a <class 'int'> with a value of 1
pi is a <class 'float'> with a value of 3.14
i_understand_annotations is a <class 'bool'> with a value of True
school is a <class 'str'> with a value of Holberton
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 4-define_variables.py
chmod +x 4-define_variables.py
./4-define_variables.py

pycodestyle 4-define_variables.py
mypy 4-define_variables.py

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


## [10. Duck typing - first element of a sequence](100-main.py)
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
bob@dylan:~$ cat 100-main.py 
#!/usr/bin/env python3

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)

bob@dylan:~$ ./100-main.py 
{'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 100-safe_first_element.py
chmod +x 100-safe_first_element.py
./100-safe_first_element.py

# Tests
touch 100-main.py
chmod +x 100-main.py
./100-main.py

# Lint
pycodestyle 100-safe_first_element.py
mypy 100-safe_first_element.py
```

### :heavy_check_mark: Solution
> [:point_right: 100-main.py](100-main.py)


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


## [0. Basic annotations - add](102-main.py)
### :page_with_curl: Task requirements.
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
```
bob@dylan:~$ cat 102-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./102-main.py
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
touch 102-main.py
chmod +x 102-main.py
./102-main.py

# Lint
pycodestyle 102-type_checking.py
mypy 102-type_checking.py
```

### :heavy_check_mark: Solution
> [:point_right: 102-main.py](102-main.py)