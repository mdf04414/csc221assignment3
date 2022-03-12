# -*- coding: utf-8 -*-
"""Assignment_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bV7HKiZzT5zggUEsFscmsmzjH00QnhJe

# Part - A

Write Python code that does the following. 

- Given a list of event log **'log_event_list'** where each element is an actual software event log of the format 'log [action] [status] [time]', where [time] is of format 'XX:XX PM or AM'.
- Create a list of valid time **'valid_time_list'** where each elememt is the [time] section of the log

Ex: Consider a log_event_list = ['log run failed 11:20 PM', 'log event error 00:00', 'log event failed 11:50 PM'] and here
- 'log run failed 11:20 PM' -> we need to fetch '11:20 PM'
- 'log event succes 00:00' -> Nothing to fetch since we do not have a valid time format here
- 'log event failed 11:50 PM' -> we need to fetch '11:50 PM'

Hence the valid_time_list = ['11:20 PM', '11:50 PM']

**Conditions to follow:**
- The output should be a string format similar to test cases mentioned below
- Inbuilt functions which require no import and Datatype methods can be used to solve this problem but No arbitray functions or library can be used except re module which is allowed to be used.
- The code you write should pass both the test cases given. The second test case will be just difference in the input which in this case is the log_event_list

Tip: You can hardcode the list input value

---

TEST CASES - 1:
- INPUT:

log_event_list = ['log run failed 11:20 PM', 'log event failed 11:50 PM', 'log event error 00:00', 'log deploy failed 2:30 AM']

- OUTPUT:

Log Event List: ['log run failed 11:20 PM', 'log event failed 11:50 PM', 'log event error 00:00', 'log deploy failed 2:30 AM']

Valid Time List: ['11:20 PM', '11:50 PM', '2:30 AM']

---

TEST CASES - 2:
- INPUT:

log_event_list = ['log start success 01:25 AM', 'log compile success 1:50 AM', 'log segment_fault error 2:X1 AM', 'log restart success 2:45 AM']

- OUTPUT:

Log Event List: ['log run failed 11:20 PM', 'log event failed 11:50 PM', 'log event error 00:00', 'log deploy failed 2:30 AM']

Valid Time List: ['01:25 AM', '1:50 AM', '2:45 AM']

---

Hint: You can use re module and its methods to find if the pattern exists and Iteration to solve this problem.
You can come up with a solution that does not use this hint but it should satisfy all the TEST CASES.
"""

import re

# Initialize the log_event_list
log_event_list = ['log run failed 11:20 PM', 'log event failed 11:50 PM', 'log event error 00:00', 'log deploy failed 2:30 AM']
# Initialize the valid_time_list
valid_time_list = []

time_regex = re.compile('\d+:\d+ \w+')

for log_event in log_event_list:
  time_match = time_regex.search(log_event)
  if time_match:
    valid_time = time_match.group()
    valid_time_list.append(valid_time)

# Print the output
print("Log Event List: {0}\n".format(log_event_list))
print("Valid Time List: {0}\n".format(valid_time_list))

"""# Part - B

Write Python code that does the following. 

- Given a string **"input_string"** of data which contains website URLs like 'http://newwebsite.com', 'https://bakery.eu'
- Create a list of valid URLs **"valid_url_list"** from the string data where the elements match the valid date format

Ex: Consider the input_string = "We can often visit https://bakery.eu or http://newbakery.com and find amazing recepies, Which you can share at https://www.socialmedia.com" 

Here the valid_url_list = ['https://bakery.eu', 'http://newbakery.com', 'https://www.socialmedia.com']

**Conditions to follow:**
- The output should be a string format similar to test cases mentioned below
- Inbuilt functions which require no import and Datatype methods can be used to solve this problem but No arbitray functions or library can be used except **re module which is allowed to be used.**
- The code you write should pass both the test cases given. The second test case will be just difference in the input which in this case is the input_string

Tip: You can hardcode the string input value

---

TEST CASES - 1:
- INPUT:

input_string = "We can often visit https://bakery.eu or http://newbakery.com and find amazing recepies, Which you can share at https://www.socialmedia.com, http://imageshare.nz and http://www.musicstreamer.com, many more socialmedia platforms!"

- OUTPUT:

Input String: We can often visit https://bakery.eu or http://newbakery.com and find amazing recepies, Which you can share at https://www.socialmedia.com, http://imageshare.nz and http://www.musicstreamer.com, many more socialmedia platforms!

Valid URL List: ['https://bakery.eu', 'http://newbakery.com', 'https://www.socialmedia.com', 'http://imageshare.nz', 'http://www.musicstreamer.com']

---

TEST CASES - 2:
- INPUT:

input_string = "The exam portal is https://exam.com and it is linked from http://college.edu site, We can further see that many other sites like http://www.facelook.io, https://www.twetter.tv and http://pinstar.io are also linked."

- OUTPUT:

Input String: The exam portal is https://exam.com and it is linked from http://college.edu site, We can further see that many other sites like http://www.facelook.io, https://www.twetter.tv and http://pinstar.io are also linked.

Valid URL List: ['https://exam.com', 'http://college.edu', 'http://www.facelook.io', 'https://www.twetter.tv', 'http://pinstar.io']


---

Hint: You can use re module and its methods to find if the pattern exists and Iteration to solve this problem.
You can come up with a solution that does not use this hint but it should satisfy all the TEST CASES.
"""

import re

# Initialize the input_string
input_string = "hello world"

# Initialize the valid_url_list
valid_url_list = []

# Write your code here
input_list = input_string.split(" ")

print(input_list)

# Import the re module to perform regex operations
import re

# Initialize the input_string
input_string = """We can often visit https://bakery.eu or http://newbakery.com and find amazing recepies, Which you can share at https://www.socialmedia.com, http://imageshare.nz and http://www.musicstreamer.com, many more socialmedia platforms!"""

# Initialize the valid_url_list
valid_url_list = []

# Write your code here
input_list = input_string.split(" ")

valid_url_pattern = '\w+://w*.*\w+.\w+'

valid_url_pattern = re.compile(valid_url_pattern)

for x in input_list:
  regex_match_object = valid_url_pattern.search(x)

  if regex_match_object:
    valid_url_list.append(x)

# Print the output
print("Input String: {0}\n".format(input_string))
print("Valid URL List: {0}\n".format(valid_url_list))

"""# Part - C

Write Python code that does the following. 

- Given a string **"input_string"** of data which contains html from a website
- Create a list of valid headings **"valid_heading_list"** from the html where the headings are present in between the paragragh tags, Format: `<hX>*HEADING*</hX>` where X is an integer usually between 1-5

Ex: Consider the  
```
input_string = "<div>
<h1> The Science of Nature </h1>
<p> Today we will learn the science</p>
<p> of all natural things that surround us</p>
<h2>Introduction  </h2> 
<p>We will start with a simple example</p>
<h7>of trees that provide us oxygen</h7>
</div>" 
```

Here the valid_heading_list = ['The Science of Nature', 'Introduction'], Since h1 and h2 tags are valid where as h7 is an invalid heading tag

Note that each heading should not contain leading or trailing space.

**Conditions to follow:**
- The output should be a string format similar to test cases mentioned below
- Inbuilt functions which require no import and Datatype methods can be used to solve this problem but No arbitray functions or library can be used except **re module which is allowed to be used.**
- The code you write should pass both the test cases given. The second test case will be just difference in the input which in this case is the input_string

Tip: You can hardcode the string input value

---

TEST CASES - 1:
- INPUT:
```bash
input_string = '''<div>
<h1> The Science of Nature </h1>
<p> Today we will learn the science</p>
<p> of all natural things that surround us</p>
<h2>Introduction  </h2> 
<p>We will start with a simple example</p>
<h7>of trees that provide us oxygen</h7>
</div>'''
```
- OUTPUT:
```bash
Input String: <div>
<h1> The Science of Nature </h1>
<p> Today we will learn the science</p>
<p> of all natural things that surround us</p>
<h2>Introduction  </h2> 
<p>We will start with a simple example</p>
<h7>of trees that provide us oxygen</h7>
</div>
```
Valid heading List: ['The Science of Nature', 'Introduction']

---

Hint: You can use string methods like strip() and re module and its methods to find if the pattern exists and Iteration to solve this problem.
You can come up with a solution that does not use this hint but it should satisfy all the TEST CASES.
"""

# Import the re module to perform regex operations
import re

# Initialize the input_string
input_string = """<div>
<h1> Welcome to New Bakery!</h1>
<h3> Our new flavors are <h3>
<p>Chocolate Coco</p>
<p> Coconut Tropic Thunder </p>
<p>Vanilla Velvet </p>
<p> Mango Magic</p>
<a href="https://newbakery.com"> This is Page 1</a>
</div>"""

# Initialize the valid_url_list
valid_flavor_list = []

# Write your code here
input_list = input_string.split('\n')

code_pattern  = '<h\d>\s\w+\s'

flavors = re.compile(code_pattern)

for x in input_list:
  objects = flavors.search(x)
  if objects:
    valid_flavor_list.append(x)

# Print the output
print("Input String: {0}\n".format(input_string))
print("Valid FLAVOR List: {0}\n".format(valid_flavor_list))

import re

# Initialize the input_string
input_string = """<div>
<h1> Welcome to New Bakery!</h1>
<h3> Our new recipies are <h3>
<p>Blue Berry Bash</p>
<p> Cheese Chaos </p>
<p>Crazy Cream </p>
<p> Pista Power Punch</p>
<a href="https://newbakery.com"> This is Page 2</a>
</div>"""

# Initialize the valid_url_list
valid_flavor_list = []

valid_flavor_regex = re.compile('<p>([\w\s]+)</p>')

valid_flavor_list = valid_flavor_regex.findall(input_string)
valid_flavor_list = [valid_flavor.strip() for valid_flavor in valid_flavor_list]

# Print the output
print("Input String: {0}\n".format(input_string))
print("Valid FLAVOR List: {0}\n".format(valid_flavor_list))