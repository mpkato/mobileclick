from mobileclick.methods import BaseSummarizationMethod
from mobileclick import Summary

class YourSummarizationMethod(BaseSummarizationMethod):
    def init(self, tasks):
        '''
        Initialization

        `tasks` is a list of Task instances.
        Task.query: Query
        Task.iunits: a list of Iunit instances
        Task.intents: a list of Intent instances
        Task.indices: a list of Index instances

        Query:
        Query.qid: Query ID
        Query.body: string of the query

        Iunit:
        Iunit.qid: Query ID
        Iunit.uid: iUnit ID
        Iunit.body: string of the iUnit

        Intent:
        Intent.qid: Query ID
        Intent.iid: Intent ID
        Intent.body: string of the intent

        Index (index information of a webpage in the provided document collection):
        Index.qid: Query ID
        Index.filepath: filepath of an HTML file
        Index.rank: rank in a search engine result page
        Index.title: webpage title
        Index.url: webpage url
        Index.body: summary of the webpage
        '''

    def summarize(self, task):
        '''
        Output Summary that consists of the first layer
        and second layers.

        How to create Summary:
        (qid: Query ID, iunit*: Iunit instance, intent*: Intent instance)

        summary = Summary.new(qid,
            # first layer
            [iunit1, iunit2, intent1, intent2],
            # second layer
            {
                intent1.iid: [iunit3, iunit4],
                intent2.iid: [iunit3, iunit5]
            }
        )
        summary.add(iunit6) # added to the first layer
        summary.add(iunit7, intent1.iid) # added to the second layer
        summary.add(intent3) # added to the first layer
        summary.add(iunit8, intent3.iid) # added to the second layer

        The resultant summary is
            First layer:
                iunit1, iunit2, intent1, intent2, iunit6, intent3
            Second layer:
                intent1: iunit3, iunit4, iunit7
                intent2: iunit3, iunit5
                intent3: iunit8

        e.g. Random summarization method
        return Summary(task.query.qid, task.iunits)
        '''
        return Summary(task.query.qid, task.iunits)

if __name__ == '__main__':
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

