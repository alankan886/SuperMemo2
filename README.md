# SuperMemo2
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)    ![Version](https://img.shields.io/badge/Version-0.0.4-light--blue.svg?style=flat-square&colorA=4c566a&colorB=90A2BC) ![Build](https://img.shields.io/badge/Build-Passing-light--green.svg?style=flat-square&colorA=4c566a&colorB=90BCA8) ![Coverage](https://img.shields.io/badge/Coverage-100%25-light--green.svg?style=flat-square&colorA=4c566a&colorB=90BCA8)
![Twitter](https://img.shields.io/twitter/url/https/twitter.com/alankan2004.svg?style=social&label=Follow%20%40alankan2004)

A package that implemented the famous spaced repetition algorithm SuperMemo-2/SM-2. A lot of software that does spaced repetition learning based their algorithm on SM-2, and there are a lot of research done around it.

:package: Link to the PyPI page: [https://pypi.org/project/supermemo2/](https://pypi.org/project/supermemo2/)

:paperclip: The implementation of the algorithm is followed by [https://www.supermemo.com/en/archives1990-2015/english/ol/sm2](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2).

## Table of Contents

 - [Motivation](#motivation)
 - [Requirements](#requirements)
 - [Installation](#installation)
 - [Quick Intro to SuperMemo-2](#qism2)
 - [Features](#features)
 - [Quickstart](#quickstart)
 - [To-do](#todo)

<a name="motivation"/> </br>
## Motivation
The motivation behind making this package was for my API. I'm making a RESTful API for spaced repetition learning called CYA, I was planning on adding the feature of calculating the next review date, then I came across SM-2.

I assumed there would be a package I can import since it's well known and been around for decades. Surprisedly, I didn't find one for Python, so I thought I would make one for other people that might need it.

:books: If you are curious of what spaced repetition is, check this out: [https://ncase.me/remember/](https://ncase.me/remember/)

<a name="requirements"/> </br>
## Requirements

:one: Python 3.7 <br/> :two: pip

<a name="installation"/> </br>
## Installation
To install the package, you may do...

`pip3 install supermemo2`

Now you can use the package in Python 3!

:page_facing_up: Make sure you are installing for Python 3, Python 2 is **NOT** supported.

<a name="qism2"/> </br>
## Quick Intro to SuperMemo-2

#### Quality
> The quality of your response by recalling the answer from a scale from 0 to 5.

	0 - complete blackout
	1 - incorrect response; the correct one remembered
	2 - incorrect response; where the correct one seemed easy to recall
	3 - correct response recalled with serious difficulty
	4 - correct response after a hesitation
	5 - perfect response

#### Interval
> The interval is the amount of days you have between now (if you just reviewed) and the next review date.

#### Easiness
> The easiness is the how easy it was to recall the answer.

	1.3 <= Easiness <= infinite, where 1.3 is the most difficult to recall, you can graduate the card after a certain value of easiness is reached.

**NOTE:** On the first visit, easiness starts off with 2.5.

#### Repetitions
> The repetitions is the number of times the attempts have a quality larger than or equal to 3 in a row.
> The repetitions value is set to 0 when quality of the attempt is lower than 3.


<a name="features"/> </br>
## Features
:mega: Implements the SM-2 algorithm. <br/> :mega: Calculates the next review date for the task you are learning using the algorithm.

### SuperMemoTwo(quality, interval=0, repetitions=0, easiness=2.5, first_visit=False, last_review=datetime.date.today())

#### Input Types

 - *quality: int*
 - *interval: int*
 - *repetitions: int*
 - *easiness: float*
 - *first_visit: boolean*
 - *last_review: **string** or **datetime.date objects***

#### Default Values
 - *interval = 0*
 - *repetitions = 0*
 - *easiness = 2.5*
 - *first_visit = False*
 - *last_review = current date/today*

**NOTE:** The default value for interval, repetitions and easiness are the values for the very first attempt.

So if the task that you learning is completely new and you just learned it today, you may create the instance like this...

```
# To create an instance when the task is completely new
sm_two = SuperMemoTwo(quality=3, first_visit=True)
```
<br/>

#### Addition Attributes
- *new_interval*
- *new_repetitions*
- *new_easiness*
- *next_review*

To access these attributes just like how you access the other ones...
```
from supermemo2 import SMTwo

sm_two = SMTwo(quality=3, first_visited=True, last_review="2020-07-05")

# Prints 2020-07-06
print(sm_two.next_review)
```

<br/>

### SuperMemoTwo.json( )
> Returns new information in json format.

Information like...

	- next_review: the next review date.
	- new repetitions: the new repetition value.
	- new_easiness: the new easiness value.
	- new_interval: the new interval value.

<br/>

### SuperMemoTwo.new_sm_two()
> Calculates the new_repetitions, new_easiness and new_interval values.

**NOTE:** If you make any changes to an existing instance's attributes, you most likely will need to call this method to re-calculate the values.

<br/>

**Example**
```
from supermemo2 import SMTwo

# Creating a SuperMemoTwo instance
sm_two = SMTwo(quality=3, interval=24, repetitions=3, easiness=1.7)

# Prints 2020-08-15
print(sm_two.next_review)

# Modified an existing instance's attributes
sm_two.interval =  12

# Prints 2020-08-15, not updated yet
print(sm_two.next_review)

# Re-calculates the values
sm_two.new_sm_two()

# Prints 2020-07-25, now you have the updated values
print(sm_two.next_review)
```
<a name="quickstart"/> </br>
## Quickstart

**NOTE:** The package DOES NOT record the values, you would need to store the values somewhere. For me, I'm using this package for my CYA API, so all the records will be stored on AWS cloud.

For example, let's say you are learning "Hello" in Spanish, which would be "Hola".
<br/>
You can start off with...
```
from supermemo2 import SMTwo

# You can leave the other arguments blank, since their default values are setup for new tasks.
# last_review can be left blank if the date is today
# First attempt of recalling the Spanish word of Hello
sm_two = SMTwo(quality=3, first_visited=True, last_review="2020-07-05")

# Prints 2020-07-06
print(sm_two.next_review)

# Second attempt of recalling the Spanish word of Hello
next_sm_two = SMTwo(quality=3, interval=sm_two.new_interval, repetitions=sm_two.new_repetitions, easiness=sm_two.new_easiness, last_review="2020-07-06")

# Prints 2020-07-12, your next attempt date
print(next_sm_two.next_review)

# Third attempt of recalling the Spanish word of Hello
next_next_sm_two = SMTwo(quality=4, interval=next_sm_two.new_interval, repetitions=next_sm_two.new_repetitions, easiness=next_sm_two.new_easiness, last_review="2020-07-12")

# Prints 2020-07-25, your next attempt date
print(next_next_sm_two.next_review)

```
And so on.

<a name="todo"/> </br>
## To-do

 - [x] More unit testing on the functions
 - [ ] Check which different Python versions before 3.7 the package can run on.
 - [x] ~~Add some basic background introduction on SuperMemo-2 (Like the quality values).~~
 - [ ] Look for good practices for designing a package for user experiences.