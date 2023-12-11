# :book: 0x02. Python - Async Comprehension.
## :page_with_curl: Topics Covered.
1. Python - Async Comprehension.

# :computer: Tasks.
## [0. Async Generator](0-async_generator.py)
### :page_with_curl: Task requirements.
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 0-async_generator.py
chmod +x 0-async_generator.py
./0-async_generator.py

# Lint checks
pycodestyle 0-async_generator.py
mypy 0-async_generator.py

# Tests
touch 0-main.py
chmod +x 0-main.py
./0-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 0-async_generator.py](0-async_generator.py)


## [1. Async Comprehensions](1-async_comprehension.py)
### :page_with_curl: Task requirements.
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
```
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
```

### :wrench: Task setup.
```bash
# Create task files and set execute permission.
touch 1-async_comprehension.py
chmod +x 1-async_comprehension.py
./1-async_comprehension.py

pycodestyle 1-async_comprehension.py
mypy 1-async_comprehension.py

# Tests
touch 1-main.py
chmod +x 1-main.py
./1-main.py
```

### :heavy_check_mark: Solution
> [:point_right: 1-async_comprehension.py](1-async_comprehension.py)


## [2. Run time for four parallel comprehensions](2-measure_runtime.py)
### :page_with_curl: Task requirements.
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135
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

# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;

:iphone: WhatsApp [+254115227963](https://wa.me/254115227963)

:email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.
