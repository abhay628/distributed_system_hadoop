#!/usr/bin/env python
# coding=utf-8
from mrjob.job import MRJob
from mrjob.step import MRStep
 
class RecommendationFile(MRJob):
    """ 
    The is to aggregate all data of a single job_post
    """
    def steps(self):
        return [
            MRStep(mapper=self.groupJobPost,
                reducer=self.countCourseByJob),
        ]

    def groupJobPost(self, _, line):
        """
        Grouping by job post and course title
        """
        jobPost ,courseTitle, courseRating = line.split('\t')
        yield jobPost, (courseTitle, float(courseRating))
 
    def countCourseByJob(self, jobPost, valueOfTitleRating):
        """
        Create a list of courses by Job post
        """
        count = 0
        ratings = []
        for courseTitle, courseRating in valueOfTitleRating:
            count += 1
            ratings.append((courseTitle, courseRating))
        yield jobPost, (count, ratings) 

if __name__ =='__main__':
    RecommendationFile.run()                      