# mobileclick
mobileclick provides baseline methods and scripts for the NTCIR-12 MobileClick-2 task: http://www.mobileclick.org/

[![PyPI version](https://badge.fury.io/py/mobileclick.svg)](http://badge.fury.io/py/mobileclick)
[![Circle CI](https://circleci.com/gh/mpkato/mobileclick.svg?&style=shield)](https://circleci.com/gh/mpkato/mobileclick)
[![Coverage Status](https://coveralls.io/repos/mpkato/mobileclick/badge.svg)](https://coveralls.io/r/mpkato/mobileclick)
[![Code Climate](https://codeclimate.com/github/mpkato/mobileclick/badges/gpa.svg)](https://codeclimate.com/github/mpkato/mobileclick)

## Requirements

Minimum requirements:
- Python 2.7
- NumPy
- nltk (>= 3.1)
- BeautifulSoup

Requirements for Japanese runs:
- mecab-python


## Installation
Install mobileclick via PyPI:

```
$ pip install mobileclick
```

You can also install mobileclick from the source code:

```
$ python setup.py install
```

NLTK corpus download (for English):
```
$ sh nltk_download.sh
```

Mecab and mecab-python installation (for Japanese):
```
$ sh mecab_install.sh
```

## Installed scripts

### Download

Download MobileClick training data (Please sign up at http://www.mobileclick.org/ ):
```
$ mobileclick_download_training_data
Please input the email and password for http://www.mobileclick.org
Email: <Your email address>
Password: <Your password>
```

Download MobileClick test data:

```
$ mobileclick_download_test_data
Please input the email and password for http://www.mobileclick.org
Email: <Your email address>
Password: <Your password>
```

### Baseline Runs

#### iUnit Ranking Subtask

Replicate the random iUnit ranking baseline:
```
$ mobileclick_random_ranking_method \
--runname random_ranking_method \
--query data/MC2-training/en/1C2-E-queries.tsv \
--iunit data/MC2-training/en/1C2-E-iunits.tsv \
--indexdir data/MC2-training-documents/1C2-E.INDX \
--pagedir data/MC2-training-documents/1C2-E.HTML
```

Replicate the LM-based iUnit ranking baseline:
```
$ mobileclick_lang_model_ranking_method \
--runname lang_model_ranking_method \
--query data/MC2-training/en/1C2-E-queries.tsv \
--iunit data/MC2-training/en/1C2-E-iunits.tsv \
--indexdir data/MC2-training-documents/1C2-E.INDX \
--pagedir data/MC2-training-documents/1C2-E.HTML \
--language english
```

#### iUnit Summarization Subtask

Replicate the random iUnit summarization baseline:
```
$ mobileclick_random_summarization_method \
--runname random_summarization_method \
--query data/MC2-test/en/MC2-E-queries.tsv \
--iunit data/MC2-test/en/MC2-E-iunits.tsv \
--intent data/MC2-test/en/MC2-E-intents.tsv \
--indexdir data/MC2-test-documents/MC2-E.INDX \
--pagedir data/MC2-test-documents/MC2-E.HTML
```

Replicate the LM-based iUnit summarization baseline:
```
$ mobileclick_lang_model_summarization_method \
--runname lang_model_summarization_method \
--query data/MC2-test/en/MC2-E-queries.tsv \
--iunit data/MC2-test/en/MC2-E-iunits.tsv \
--intent data/MC2-test/en/MC2-E-intents.tsv \
--indexdir data/MC2-test-documents/MC2-E.INDX \
--pagedir data/MC2-test-documents/MC2-E.HTML \
--language english
```

Replicate the LM-based two-layer iUnit summarization baseline:
```
$ mobileclick_lang_model_two_layer_summarization_method \
--runname lang_model_two_layer_summarization_method \
--query data/MC2-test/en/MC2-E-queries.tsv \
--iunit data/MC2-test/en/MC2-E-iunits.tsv \
--intent data/MC2-test/en/MC2-E-intents.tsv \
--indexdir data/MC2-test-documents/MC2-E.INDX \
--pagedir data/MC2-test-documents/MC2-E.HTML \
--language english
```

## Generate your runs

Both of the subtasks are supported.
Please look at examples in `examples`.
A typical workflow is shown below:

### 1. Create a subclass of BaseRankingMethod/BaseSummarizationMethod

For iUnit Ranking
```python
from mobileclick.methods import BaseRankingMethod

class YourRankingMethod(BaseRankingMethod):
    def init(self, tasks):
    	'''
    	Initialization
    	'''
 	def rank(self, task):
	'''
        Output ranked pairs of an iUnits and a score
    '''
```

For iUnit Summarization
```python
from mobileclick.methods import BaseSummarizationMethod
from mobileclick import Summary

class YourSummarizationMethod(BaseSummarizationMethod):
    def init(self, tasks):
        '''
        Initialization
        '''
    def summarize(self, task):
        '''
        Output an instance of Summary.
        '''
```

### 2. Generate a run

For iUnit Ranking
```python
from mobileclick import Task
tasks = Task.read(
	"data/MC2-training/en/1C2-E-queries.tsv",
	"data/MC2-training/en/1C2-E-iunits.tsv",
	"data/MC2-training-documents/1C2-E.INDX",
	"data/MC2-training-documents/1C2-E.HTML")
method = YourRankingMethod()
run = method.generate_run("YourRun", "This is your run", tasks)
run.save('./')
```

For iUnit Summarization
```python
from mobileclick import Task
tasks = Task.read(
    "data/MC2-test/en/MC2-E-queries.tsv",
    "data/MC2-test/en/MC2-E-iunits.tsv",
    "data/MC2-test-documents/MC2-E.INDX",
    "data/MC2-test-documents/MC2-E.HTML",
    "data/MC2-test/en/MC2-E-intents.tsv")
method = YourSummarizationMethod()
run = method.generate_run("YourRun", "This is your run", tasks)
run.save('./')
```

Upload `./YourRun.tsv` or `./YourRun.xml` to http://www.mobileclick.org/ for evaluation!

## License
MIT License (see LICENSE file).
