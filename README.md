# SuperMemo2
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Version](https://img.shields.io/badge/Version-1.0.0-light--blue.svg?style=flat-square&colorA=4c566a&colorB=90A2BC)
[![Download](https://img.shields.io/badge/Downloads-2.2k+-light--blue.svg?style=flat-square&colorA=4c566a&colorB=90A2BC)](https://pepy.tech/project/SuperMemo2)
![Coverage](https://img.shields.io/badge/Coverage-100%25-light--green.svg?style=flat-square&colorA=4c566a&colorB=90BCA8)

A package that implemented the spaced repetition algorithm SuperMemo-2/SM-2 for you to quickly calculate your next review date for whatever you are learning.

:package: [PyPI page](https://pypi.org/project/supermemo2/)

:paperclip: [The SuperMemo-2 Algorithm](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2)

## Table of Contents
 - [Motivation](#motivation)
 - [Installing and Supported Versions](#install-versions)
 - [A Simple Example](#example)
 - [Quick Intro to SuperMemo-2](#qism2)
 - [Features](#features)

<a name="motivation"/> </br>
## Motivation
The goal was to have an efficient way to calculate the next review date for studying/learning. Removes the burden of remembering the algorithm, equations, and math from the users.

<a name="install-versions"/> </br>
## Installing and Supported Versions

Install and upate using [pip](https://pip.pypa.io/en/stable/quickstart/)

```bash
pip3 install -U supermemo2
```

<a name="example"/> </br>
## A Simple Example

```python
>>> from supermemo2 import first_review
>>> # a recall quality of 3 and review date defaults to today's date
>>> # let's pretend today is 2021-01-01
>>> smtwo = first_review(3)
>>> print(smtwo.review_date)
2021-01-02
>>> # on your second review, 2021-01-02, grab your current values from your last review
>>> record = smtwo.as_dict(curr=True)
>>> # update your recall quality
>>> record["quality"] = 5
>>> smtwo.calc(**record)
>>> print(smtwo.review_date)
2021-01-08
```
<a name="qism2"/> </br>
## Quick Intro to SuperMemo-2
:books: If you are curious of what spaced repetition is, check this [short video](https://youtu.be/-uMMRjrzPmE?t=94) out.

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
:mega: Calculates your next review date of your task following the SuperMemo-2 algorithm.
<br/> :mega: first_visit method available to create a new instance at ease without the need to remember the inital values.
<br/> :mega: modify method available to quickly modify existing instance's values.
<br/> :mega: as_json and as_dict available to swiftly export the instance's values, and simply calculate the next review date using as_dict.

### SMTwo.calc(quality, interval, repetitions, easiness, review_date)

#### Input Types

 - *quality: int*
 - *interval: int*
 - *repetitions: int*
 - *easiness: float*
 - *review_date: **datetime.date object***


```

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
