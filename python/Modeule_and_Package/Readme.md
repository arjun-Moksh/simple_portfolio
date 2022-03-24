# Modules
Modules are files that contain Python code statements and definitions that can be imported into other files.

## User-defined Modules
User-defined modules are created by writing Python code in a file and then importing that file into another file.

### Creating and importing a module
To create a module, write Python code in a file and save it as a .py file.
```
# Create a file named my_module.py
def my_function():
    print("Hello, world!")

def add_numbers(x, y):
    return x + y
```
To import a module, use the import statement in the file that you want to use the module in.

Create a file named my_module_import.py
```
# Import the my_module file
import my_module

print(dir(my_module))

my_module.my_function()

result = my_module.add_numbers(1, 2)
print(result)
```

## Built-in Modules(Python Standard Library)
Built-in modules are modules that are included in the Python standard library.

example:
<ul>
<li>math</li>
<li>random</li>
<li>datetime</li>
<li>os</li>
<li>sys</li>
</ul>

```
import math                           
import random as r
import datetime
import os
import sys


x=math.sqrt(16)
print(x)

random_number=r.randint(1,10)
print(random_number)

print(datetime.datetime.now())

cwd=os.getcwd()
directories=os.listdir(cwd)
print(cwd)
print(directories)

pathforallmodules=sys.path
print(pathforallmodules)

```

## External Modules
External modules are modules that are not included in the Python standard library.

External modules are installed using the pip package manager.

```
pip install module_name
```
### Install pip package manager
1.Download get-pip.py from https://bootstrap.pypa.io/get-pip.py and save it to your local folder.

2.Navigate command prompt or terminal to the folder where you have downloaded the file and run the command:
```
python get-pip.py
```
3.Check if pip is installed by running the command:
```
pip --version
```

#### Install an external module (requests)
```
pip install requests
```

note: we should always install external modules/libraries inside a virtual environment.

## Modules Attributes
```
#__name__ attribute returns the name of the module
import math
import my_module

math.__name__ # returns 'math'
my_module.__name__ # returns 'my_module'
```

When we run any Python script (i.e. a module), its __name__ attribute is also set to __main__
```
# Create a file named welcome.py

print("__name__ = ", __name__) # __name__ is set to __main__
```

# Packages
Packages are directories that contain modules.


## Creating a package
1. Create a directory named my_package
2. Create a file named <code> __init__.py </code> in the my_package directory
3. Create a file named my_module.py in the my_package directory

## Importing a module from a package
```
from my_package import my_module
from my_package.my_module import my_function

my_module.my_function()

my_function()
```
