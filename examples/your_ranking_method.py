from mobileclick.methods import BaseRankingMethod

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
        return [(i, 0) for i in task.iunits]

if __name__ == '__main__':
    from mobileclick import Task
    tasks = Task.read(
        "data/MC2-training/en/1C2-E-queries.tsv",
        "data/MC2-training/en/1C2-E-iunits.tsv",
        "data/MC2-training-documents/1C2-E.INDX",
        "data/MC2-training-documents/1C2-E.HTML")
    method = YourRankingMethod()
    run = method.generate_run("YourRun", "This is your run", tasks)
    run.save('./')
