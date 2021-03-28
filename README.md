# SuperMemo2
![Python](https://img.shields.io/badge/python-3+-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
[![Version](https://img.shields.io/pypi/v/supermemo2?logo=pypi&logoColor=white&style=flat-square&colorA=4c566a&colorB=90A2BC)](https://pypi.org/project/supermemo2/)
[![Build](https://img.shields.io/github/workflow/status/alankan886/SuperMemo2/CI?logo=github-actions&logoColor=white&style=flat-square&colorA=4c566a&colorB=90BCA8)](https://github.com/alankan886/SuperMemo2/actions?query=workflow%3ACI)
[![Coverage](https://img.shields.io/codecov/c/github/alankan886/SuperMemo2?logo=codecov&logoColor=white&style=flat-square&colorA=4c566a&colorB=90BCA8)](https://codecov.io/gh/alankan886/SuperMemo2)
[![Download](https://img.shields.io/badge/downloads-4k-light--blue.svg?style=flat-square&colorA=4c566a&colorB=90A2BC)](https://pepy.tech/project/SuperMemo2)

A package that implemented the spaced repetition algorithm SM-2 for you to quickly calculate your next review date for whatever you are learning.

📌 &nbsp;**Note:** The algorithm SM-2 doesn't equal to the computer implementation SuperMemo2. In fact, the 3 earliest implementations (SuperMemo1, SuperMemo2 and SuperMemo3) all used algorithm SM-2. I didn't notice that when I first published the package on PyPI, and I can't change the package name.

📦 &nbsp;[PyPI page](https://pypi.org/project/supermemo2/)

## Table of Contents
- [Motivation](#motivation)
- [Installing and Supported Versions](#install-versions)
- [A Simple Example](#example)
- [Features](#features)
- [What is SM-2?](#sm2)
- [Code Reference](#code)
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

supermemo2 supports Python 3+

<a name="example">

## A Simple Example

```python
from supermemo2 import SMTwo

# first review
# using quality=4 as an example, read below for what each value from 0 to 5 represents
# review date would default to date.today() if not provided
review = SMTwo.first_review(4, "2021-3-14")
# review prints SMTwo(easiness=2.36, interval=1, repetitions=1, review_date=datetime.date(2021, 3, 15))

# second review
review = SMTwo(review.easiness, review.interval, review.repetitions).review(4, "2021-3-14")
# review prints similar to example above.
```

<a name="features">

## Features
📣 &nbsp;Calculates the review date of the task following the SM-2 algorithm.
<br/> 📣 &nbsp;The first_review method to calculate the review date at ease without having to know the initial values.

<a name="sm2">

## What is SM-2?
🎥 &nbsp;If you are curious of what spaced repetition is, check this [short video](https://youtu.be/-uMMRjrzPmE?t=94) out.

📌 &nbsp;A longer but interactive [article](https://ncase.me/remember/) on spaced repetition learning.

📎 &nbsp;[The SM-2 Algorithm](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2)

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

<a name="code">

## Code Reference
### *class* supermemo2.SMTwo(easiness, interval, repetitions)

**Parameters:**
- easiness (float) - the easiness determines the interval.
- interval (int) - the interval between the latest review date and the next review date.
- repetitions (int) - the count of consecutive reviews with quality larger than 2.

<br>

**first_review(** quality, review_date=None, date_fmt=None **)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Static method that calcualtes the next review date for the first review without having to know the initial values, and returns a dictionary containing the new values.

**Parameters:**
- quality (int) - the recall quality of the review.
- review_date (str or datetime.date) - optional parameter, the date of the review.
- date_fmt (string) - optional parameter, the format of the review_date. Formats like `year_mon_day`, `mon_day_year` and `day_mon_year`.

**Returns:** dictionary containing values like quality, easiness, interval, repetitions and review_date.

**Return Type:** Dict

**Usage:**
```python
from supermemo2 import SMTwo, mon_day_year
# using default date date.today()
SMTwo.first_review(3)

# providing string date in Year-Month-Day format
SMTwo.first_review(3, "2021-12-01")

# providing string date in Month-Day-Year format
SMTwo.first_review(3, "12-01-2021", mon_day_year)

# providing date object date
from datetime import date
d = date(2021, 12, 1)
SMTwo.first_review(3, d)
```

**review(** quality, review_date=None, date_fmt=None **)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calcualtes the next review date based on previous values, and returns a dictionary containing the new values.

**Parameters:**
- quality (int) - the recall quality of the review.
- review_date (str or datetime.date) - optional parameter, the date of the review.
- date_fmt (string) - optional parameter, the format of the review_date. Formats like `year_mon_day`, `mon_day_year` and `day_mon_year`.

**Returns:** dictionary containing values like quality, easiness, interval, repetitions and review_date.

**Return Type:** Dict

**Usage:**
```python
from supermemo2 import SMTwo, mon_day_year
# using previous values from first_review call
r = SMTwo.first_review(3)

# using default date date.today()
SMTwo(r.easiness, r.interval, r.repetitions).review(3)

# providing string date in Year-Month-Day format
SMTwo(r.easiness, r.interval, r.repetitions).review(3, "2021-12-01")

# providing string date in Month-Day-Year format
SMTwo(r.easiness, r.interval, r.repetitions).review(3, "12-01-2021", mon_day_year)

# providing date object date
from datetime import date
d = date(2021, 12, 1)
SMTwo(r.easiness, r.interval, r.repetitions).review(3, d)
```

<a name="testing">

## Testing

Assuming you [dowloaded the code and installed requirements](#download).

### Run the tests
```bash
pytest tests/
```

### Check test coverages
```bash
pytest --cov
```
Check coverage on [Codecov](https://codecov.io/gh/alankan886/SuperMemo2).

<a name="changelog">

## Changelog
2.0.0 (2021-03-28): Major changes/rebuild, Update recommended
- Rebuilt and simplfied the package.

1.0.3 (2021-01-30): Minor bug fix, Update recommended
- Re-evaluate the default date argument to first_review() on each call.

1.0.2 (2021-01-18): Major and Minor bug fix, Update recommended
- Add required attrs package version to setup.py.
- Allow users to access SMTwo model.
- Fix E-Factor calculation when q < 3.

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
- Add new section about SM-2 in documentation, and fix some formats in README.

0.0.2 (2020-07-05): Refactor feature, Update recommended
- Refactor the supermemo2 algorithm code into a simpler structure, and remove unnecessary methods in the class.

0.0.1 (2020-07-02): Feature release
- Initial Release

<a name="credits">

## Credits

1. [pytest](https://docs.pytest.org/en/stable/)
2. [The SM-2 Algorithm](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2)

