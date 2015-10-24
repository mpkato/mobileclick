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

Replicate the random iUnit ranking baseline:
```
$ mobileclick_random_ranking_method --runname random_ranking_method \
--query data/MC2-training/en/1C2-E-queries.tsv \
--iunit data/MC2-training/en/1C2-E-iunits.tsv \
--indexdir data/MC2-training-documents/1C2-E.INDX \
--pagedir data/MC2-training-documents/1C2-E.HTML
```

Replicate the LM-based iUnit ranking baseline:
```
$ mobileclick_lang_model_ranking_method --runname lang_model_ranking_method \
--query data/MC2-training/en/1C2-E-queries.tsv \
--iunit data/MC2-training/en/1C2-E-iunits.tsv \
--indexdir data/MC2-training-documents/1C2-E.INDX \
--pagedir data/MC2-training-documents/1C2-E.HTML \
--language english
```

## Generate your runs
The current version can only deal with the iUnit ranking subtask.

### 1. Create a subclass of BaseRankingMethod

```python
from .base_ranking_method import BaseRankingMethod

class YourRankingMethod(BaseRankingMethod):
    def init(self, tasks):
	    '''
    	Initialization
    	
		`tasks` is a list of Task instances.
		Task.query: Query
		Task.iunits: a list of Iunit instances
		Task.indices: a list of Index instances
		
		Query:
		Query.qid: Query ID
		Query.body: string of the query
		
		Iunit:
		Iunit.qid: Query ID
		Iunit.uid: iUnit ID
		Iunit.body: string of the iUnit
		
		Index (index information of a webpage in the provided document collection):
		Index.qid: Query ID
		Index.filepath: filepath of an HTML file
		Index.rank: rank in a search engine result page
		Index.title: webpage title
		Index.url: webpage url
		Index.body: summary of the webpage
    	'''

    def rank(self, task):
        '''
        Output ranked pairs of an iUnits and a score
        
        e.g. Random ranking method
        return [(i, 0) for i in task.iunits]
        '''
```

### 2. Generate a run
```python
tasks = Task.read(
	"data/MC2-training/en/1C2-E-queries.tsv",
	"data/MC2-training/en/1C2-E-iunits.tsv",
	"data/MC2-training-documents/1C2-E.INDX",
	"data/MC2-training-documents/1C2-E.HTML")
method = YourRankingMethod()
run = method.generate_run("YourRun", "This is your run", tasks)
run.save('./')
```

Upload "./YourRun.tsv" to http://www.mobileclick.org/ for evaluation!

## License
MIT License (see LICENSE file).
