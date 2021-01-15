# SuperMemo2
![Python](https://img.shields.io/badge/python-3.6+-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
[![Version](https://img.shields.io/pypi/v/supermemo2?logo=pypi&logoColor=white&style=flat-square&colorA=4c566a&colorB=90A2BC)](https://pypi.org/project/supermemo2/)
[![Build](https://img.shields.io/github/workflow/status/alankan886/SuperMemo2/CI?logo=github-actions&logoColor=white&style=flat-square&colorA=4c566a&colorB=90BCA8)](https://github.com/alankan886/SuperMemo2/actions?query=workflow%3ACI)
[![Coverage](https://img.shields.io/codecov/c/github/alankan886/SuperMemo2?logo=codecov&logoColor=white&style=flat-square&colorA=4c566a&colorB=90BCA8)](https://codecov.io/gh/alankan886/SuperMemo2)
[![Download](https://img.shields.io/badge/downloads-2k-light--blue.svg?style=flat-square&colorA=4c566a&colorB=90A2BC)](https://pepy.tech/project/SuperMemo2)

A package that implemented the spaced repetition algorithm SuperMemo-2/SM-2 for you to quickly calculate your next review date for whatever you are learning.

📦 &nbsp;[PyPI page](https://pypi.org/project/supermemo2/)

## Table of Contents
- [Motivation](#motivation)
- [Installing and Supported Versions](#install-versions)
- [A Simple Example](#example)
- [Features](#features)
	- [Potential Features](#potential)
- [What is SuperMemo-2?](#sm2)
- [API Reference](#api)
	- [Main Interface](#main-interface)
	- [Exceptions](#excep)
	- [Lower-Level Classes](#classes)
- [Testing](#testing)
- [Changelog](#changelog)
- [Credits](#credits)

<a name="motivation">

## Motivation
The goal was to have an efficient way to calculate the next review date for studying/learning. Removes the burden of remembering the algorithm, equations, and math from the users.

<a name="install-versions">

## Installation and Supported Versions

### Package Install
Install and upate the package using [pip](https://pip.pypa.io/en/stable/quickstart/):

```bash
pip3 install -U supermemo2
```

<a name="download">

### To Play Around with the Code
Download the code:

```bash
git clone https://github.com/alankan886/SuperMemo2.git
```

Install dependencies to run the code:
```bash
pip3 install -r requirements.txt
```

supermemo2 supports Python 3.6+.

<a name="example">

## A Simple Example

We start with a recall quality of 3, and the review date defaults to today (let's pretend it's 2021-01-01). 

Using the current values from the first review can help us calculate for the second review.

Grab the current values from the first review, and update the recall quality. Then calculate the next review date.

```python
>>> from supermemo2 import first_review
>>> smtwo = first_review(3)
>>> print(smtwo.review_date)
2021-01-02
>>> record = smtwo.as_dict(curr=True)
>>> record["quality"] = 5
>>> smtwo.calc(**record)
>>> print(smtwo.review_date)
2021-01-08
```

<a name="features">

## Features
📣 &nbsp;Calculates the next review date of the task following the SuperMemo-2/SM-2 algorithm.
<br/> 📣 &nbsp;The first_review method to create a new instance at ease without having to know the initial values.
<br/> 📣 &nbsp;The modify method to modify existing instance values that recalculates the new values.
<br/> 📣 &nbsp;The json and dict methods to export the instance values and to help calculate the next review date.

<a name="potential">

### Potential Features
- Allow users to pass the review date as a string in many formats.
- Provide a modified option to configure the intervals for repetitions 1 and 2. And an option to reduce quality responses to 4, since 0 to 2 doesn't do much.

<a name="sm2">

## What is SuperMemo-2?
🎥 &nbsp;If you are curious of what spaced repetition is, check this [short video](https://youtu.be/-uMMRjrzPmE?t=94) out.

📌 &nbsp;A longer but interactive [article](https://ncase.me/remember/) on spaced repetition learning.

📎 &nbsp;[The SuperMemo-2 Algorithm](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2)

### What are the "values"?
The values are the:

- Quality: The quality of recalling the answer from a scale of 0 to 5.
	- 5: perfect response.
	- 4: correct response after a hesitation.
	- 3: correct response recalled with serious difficulty.
	- 2: incorrect response; where the correct one seemed easy to recall.
	- 1: incorrect response; the correct one remembered.
	- 0: complete blackout.
- Easiness: The easiness factor, a multipler that affects the size of the interval, determine by the quality of the recall.
- Interval: The gap/space between your next review.
- Repetitions: The count of correct response (quality >= 3) you have in a row.

✏️ &nbsp;quality from 0 to 2 doesn't have much impact; it doesn't affect the easiness. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you are building a program on top of this package, you may group them as one response. So instead of &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6 responses, you have 4 (5, 4, 3, and incorrect response).

<a name="api">

## API Reference

<a name="main-interface">

### Main Interface
supermemo2.**first_review**(quality, review_date=datetime.date.today())

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcualtes next review date without having to know the initial values,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and returns an SMTwo object with new values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**
- **quality**(int) - the quality of the response/recall from a scale of 0 to 5.
- **review_date** (Optional[datetime.date]) - the last review date.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Returns:** SMTwo object

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Return Type:** supermemo2.SMTwo

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usage:
```python
>>> from supermemo2 import first_review
>>> from datetime import date
>>> smtwo = first_review(3, date(2021, 1, 1))
>>> print(smtwo.review_date)
2021-01-02
```

supermemo2.**modify**(instance, quality=None, easiness=None, interval=None, repetitions=None, review_date=None)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Modifies previously inserted values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**
- **instance** (SMTwo) - the SMTwo instance to modify.
- **quality** (Optional[int]) - the quality value to replace the previous quality value.
- **easiness** (Optional[float])- the easiness value to replace the previous easiness value.
- **interval** (Optional[int]) - the interval value to replace the previous interval value.
- **repetitions** (Optional[int])  - the repetitions value to replace the previous reptitions value.
- **review_date** (Optional[datetime.date]) - the review date to replace the previous review date.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Returns:** None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Return Type:** None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usage:
```python
>>> from supermemo2 import first_review, modify
>>> smtwo = first_review(3)
>>> print(smtwo.quality)
3
>>> modify(smtwo, quality=5)
>>> print(smtwo.quality)
5
```

<a name="excep">

### Exceptions
exception supermemo2.exceptions.**CalcNotCalledYet**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Other methods are called before the values are calculated.

<a name="classes">

### Lower-Level Classes
class supermemo2.**SMTwo()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generates all the instances and contains the tools.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I would not recommend directly generating an instance from this class.

**calc**(quality, easiness, interval, repetitions, review_date)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculates the values. For the first review, the initial/previous values &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;would be 2.5 for easiness, 1 for interval and 1 for repetitions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**
- **quality** (Optional[int]) - the quality value received from the last calculation.
- **easiness** (Optional[float])- the easiness value received from the last calculation.
- **interval** (Optional[int]) - the interval value received from the last calculation.
- **repetitions** (Optional[int])  - the repetitions value received from the last calculation.
- **review_date** (Optional[datetime.date]) - the review date received from the last calculation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Returns:** None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Return Type** None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usage:
```python
>>> from supermemo2.models import SMTwo
>>> from datetime import date
>>> smtwo = SMTwo()
>>> smtwo.calc(3, 2.5, 1, 1, date(2021, 1, 1))
>>> print(smtwo.review_date)
2021-01-02
```

**json**(prev=None, curr=None)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a string of the values in JSON format.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**
- **prev** (Optional[bool]) - If true, export only previous values.
- **curr** (Optional[bool]) - If true, export only current values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Returns:** String in JSON format

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Return Type** String

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usage:
```python
>>> from supermemo2 import first_visit
>>> from datetime import date
>>> smtwo = first_visit(3, date(2021, 1, 1))
>>> print(smtwo.json())
'{"quality": 3, "prev_easiness": 2.5, "prev_interval": 1, "prev_repetitions": 1, "prev_review_date": datetime.date(2021, 1, 1),"easiness": 2.36, "interval": 2, "repetitions": 1, "review_date": datetime.date(2021, 1, 2)}'
```

**dict**(prev=None, curr=None)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns a the values in dictionary format.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**
- **prev** (Optional[bool]) - If true, export only previous values.
- **curr** (Optional[bool]) - If true, export only current values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Returns:** Dictionary

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Return Type** Dict

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usage:
```python
>>> from supermemo2 import first_visit
>>> from datetime import date
>>> smtwo = first_visit(3, date(2021, 1, 1))
>>> print(smtwo.dict())
'{"quality": 3, "prev_easiness": 2.5, "prev_interval": 1, "prev_repetitions": 1, "prev_review_date": datetime.date(2021, 1, 1),"easiness": 2.36, "interval": 2, "repetitions": 1, "review_date": datetime.date(2021, 1, 2)}'
```

class supermemo2.SMTwo.**Prev**(easiness, interval, repetitions, review_date)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stores the previous values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**
- **easiness** (float)- the previous easiness value.
- **interval** (int) - the previous interval value.
- **repetitions** (int)  - the previous repetitions value.
- **review_date** (datetime.date) - the previous review date.

<a name="testing">

## Testing

Assuming you [dowloaded the code and installed requirements](#download).

### Run the tests
```bash
pytest tests/
```

### Check test coverages
```bash
pytest --cov=supermemo2
```
Check coverage on [Codecov](https://codecov.io/gh/alankan886/SuperMemo2).

<a name="changelog">

## Changelog
1.0.2 (2021-01-15): Minor bug fix
- Add required attrs package version to setup.py 

1.0.1 (2021-01-02): Fix tests, update README and add Github actions, Update not required
- Add missing assertions to test_api.py.
- Update README badges and fix format.
- Add Github actions to run tests against Python versions 3.6 to 3.9 in different OS, and upload coverage to Codecov.

1.0.0 (2021-01-01): Complete rebuild, Update recommended
- Build a new SMTwo class using the attrs package.
- Provide API methods to quickly access the SMTwo class.
- Develop 100% coverage integration and unit tests in a TDD manner.
- Write new documentation.

0.1.0 (2020-07-14): Add tests, Update not required
- Add passing unit tests with a coverage of 100%.

0.0.4 (2020-07-10): Minor bug fix, Update recommended
- Fix interval calculation error when q < 3.

0.0.3 (2020-07-06): Documentation Update, Update not required
- Add new section about SuperMemo-2 in documentation, and fix some formats in README.

0.0.2 (2020-07-05): Refactor feature, Update recommended
- Refactor the supermemo2 algorithm code into a simpler structure, and remove unnecessary methods in the class.

0.0.1 (2020-07-02): Feature release
- Initial Release

<a name="credits">

## Credits

1. [attrs](https://www.attrs.org/en/stable/index.html)
2. [pytest](https://docs.pytest.org/en/stable/)
3. [The SuperMemo-2 Algorithm](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2)

