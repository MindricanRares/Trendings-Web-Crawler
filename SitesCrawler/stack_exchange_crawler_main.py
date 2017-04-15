# -*- coding: utf-8 -*-
import sys
from stackauth import StackAuth
from stackexchange import Site, StackOverflow, Sort, ASC, DESC
import datetime
import json
import py
import matplotlib.pyplot
import numpy as np
import sklearn.cluster
import distance

sys.path.append('.')
sys.path.append('..')

so = Site(StackOverflow, impose_throttling=True)


# take all the data from the last week split it by days search
# for specific tags(python java javascript etc) and create
# multiple pie diagrams of the procnet of each tag and then create a gif
# group the tags with clustering and/or levensthein distance

# maybe upload to a flask server the gif
def write_to_dict():
    print('The highest voted question on StackOverflow is:')

    date_limit = datetime.datetime(2017, 04, 06, 6, 30, 0)

    tags_dictionary = dict()

    questions = so.questions(sort=Sort.Creation, order=DESC)
    for question in questions:
        if question.creation_date > date_limit:
            print question.title
            print question.tags
            for tag in question.tags:
                if tag not in tags_dictionary.keys():
                    tags_dictionary[tag] = 0
                tags_dictionary[tag] += 1
            print question.creation_date

            continue
        break

    with open('tags.json', 'w') as file_writer:
        json.dump('ceva', file_writer)
        print tags_dictionary
        json.dump(tags_dictionary, file_writer, sort_keys=True, indent=4, separators=(',', ':'))




def main():
    with open('tags.json', 'r') as file_reader:
        tag_dict = json.load(file_reader)

        # real_list_of_tags(tag_dict)
        from collections import OrderedDict
        d = OrderedDict(sorted(tag_dict.items(),
                               key=lambda kv: kv[1], reverse=True))
        import csv
        my_file = open('tag2.csv', 'wb')
        wr = csv.writer(my_file, quoting=csv.QUOTE_ALL)
        for val in d.keys():
            wr.writerow([val])
        my_file.close()
        # affinity_propagation(d.keys())


if __name__ == '__main__':
    # main()
    tag_dict = {}
    tag_def = {}
    with open('tags.json', 'r') as file_reader:
        tag_dict = json.load(file_reader)

    # real_list_of_tags(tag_dict)
    from collections import OrderedDict

    ordered_tags = OrderedDict(sorted(tag_dict.items(),
                                      key=lambda kv: kv[1], reverse=True))
    tags = ordered_tags.keys()

    for first_tag in tags:
        similar_tags = [first_tag]
        for second_tag in tags:
            if first_tag in second_tag:
                similar_tags.append(second_tag)
                tags.remove(second_tag)
        from teeest import search_for_tag

        if len(similar_tags) == 2:
            print similar_tags[0]
            print search_for_tag(similar_tags[0])['snippet']
            tag_def[similar_tags] = search_for_tag(similar_tags[0])['snippet']
            # print similar_tags
    with open('tags_def.json', 'w') as file_writer:
        json.dump(tag_def, file_writer)
    for key, value in tag_def.iteritems():
        print key, value
