import praw
import csv


class AnalyzeSubreddit:
    def __init__(self, subreddit_name):
        self.subreddit_name = subreddit_name
        self.reddit = praw.Reddit(user_agent='Comment Extraction (by /u/RaresMM)',
                                  client_id='n8CURaWqBCFT1g', client_secret="Uxet3ed-ryfpKm3uVfidZbU5nMs")
        self.subreddit = self.reddit.subreddit(subreddit_name)

    def get_array_of_submission(self):
        """
        Creates an array of submissions
        :return: 
        """
        self.submissions_array = [submission for submission in self.subreddit.top()]

    """
    Input:reddit submission
    Output:an array with all the main comments of the submission
    """

    def get_array_of_comments(self, submission):
        submission.comments.replace_more(limit=0)
        # flat_comments = praw.helpers.flatten_tree(submission.comments)
        comments_array = [comment for comment in submission.comments]
        return comments_array

    """
    Iterates thourgh the submission and starts iterating through
    each submission's list of comments
    """

    def iterate_through_submission_array(self):
        self.submission_values = []
        for submission in self.submissions_array:
            comments_array = self.get_array_of_comments(submission)

            time_of_submission = (submission.created)
            self.submission_values.append(self.iterate_through_comments_array(comments_array, time_of_submission))
        self.save_data()

    """
    Iterates though the comments array and calculates the averege time of the comments
    """

    def iterate_through_comments_array(self, comments_array, time_of_submission):
        vars_dict = {'number_of_comments': 0, 'number_of_points': 0, 'time_of_submission': time_of_submission,
                     'time_took_to_comment': 0}
        self.checkComments(comments_array, vars_dict)
        if vars_dict['number_of_comments'] != 0:
            vars_dict['time_took_to_comment'] = ((vars_dict['time_took_to_comment'] / vars_dict['number_of_comments']))
        return vars_dict

    """
    Input parent comment
    Output childrens comments of the parent
    """

    def checkComments(self, comments, vars):
        for comment in comments:
            vars['number_of_comments'] += 1
            vars['number_of_points'] += comment.score
            vars['time_took_to_comment'] += comment.created - vars['time_of_submission']
            self.checkComments(comment.replies, vars)

    """
    Saves the data from the submission to a json
    """

    # def save_data(self):
    #     with open('test.json', 'a')as file_appender:
    #         json.dump(self.submission_values, file_appender,sort_keys=True,indent=4,separators=(',',':'))
    def save_data(self):
        with open(self.subreddit_name + '.txt', 'a') as file_appender:
            appender = csv.writer(file_appender)
            for i in self.submission_values:
                list = []
                for j in i.values():
                    print j
                    list.append(j)
                appender.writerow(list)


def main():
    obj = AnalyzeSubreddit('learnpython')
    obj.get_array_of_submission()
    obj.iterate_through_submission_array()
    # obj2 = AnalyzeSubreddit('python')
    # obj2.get_array_of_submission()
    # obj2.iterate_through_submission_array()


if __name__ == '__main__':
    main()

