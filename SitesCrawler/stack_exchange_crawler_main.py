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


# def levenshtein(s1, s2):
#     if len(s1) < len(s2):
#         return levenshtein(s2, s1)
#
#     # len(s1) >= len(s2)
#     if len(s2) == 0:
#         return len(s1)
#
#     previous_row = range(len(s2) + 1)
#     for i, c1 in enumerate(s1):
#         current_row = [i + 1]
#         for j, c2 in enumerate(s2):
#             insertions = previous_row[
#                              j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
#             deletions = current_row[j] + 1  # than s2
#             substitutions = previous_row[j] + (c1 != c2)
#             current_row.append(min(insertions, deletions, substitutions))
#         previous_row = current_row
#
#     return previous_row[-1]


def real_list_of_tags(tags_dict):
    data2 = []
    from collections import OrderedDict
    d = OrderedDict(sorted(tags_dict.items(),
                           key=lambda kv: kv[1], reverse=True))
    data = d.keys()

    for i in data:
        for index, j in enumerate(data):
            s = distance.levenshtein(i, j)
            if s < 5:
                del data[index]
                tags_dict[i] += tags_dict[j]

        data2.append(i)
    print 'started printing'
    from collections import OrderedDict
    from operator import itemgetter
    d = OrderedDict(sorted(tags_dict.items(),
                           key=lambda kv: kv[1], reverse=True))
    i = 0
    new_dict = {'others': 0}
    for elem, key in d.iteritems():
        if i < 19:
            new_dict[elem] = key
        else:
            new_dict['others'] += key
        i += 1
    new_d = OrderedDict(sorted(new_dict.items(),
                               key=lambda kv: kv[1], reverse=True))

    total_sum = 0
    for elem, key in new_d.iteritems():
        total_sum += key
        # print elem, key
    for elem, key in new_d.iteritems():
        # print elem,key,total_sum
        new_d[elem] = float(key) / total_sum * 100

    for elem, key in new_d.iteritems():
        print elem, key
    matplotlib.pyplot.pie([float(v) for v in new_d.values()], labels=[(k) for k in new_d.keys()],
                          autopct=None)
    matplotlib.pyplot.savefig('initial_pie_chart.jpg')
    matplotlib.pyplot.show()

    print 'finished printing'


# def affinity_propagation(words):
#     words = np.asarray(words)  # So that indexing with a list will work
#     lev_similarity = -1 * np.array([[distance.nlevenshtein(w1, w2) for w1 in words] for w2 in words])
#     affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.9)
#     affprop.fit(lev_similarity)
#     for cluster_id in np.unique(affprop.labels_):
#         exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
#         cluster = np.unique(words[np.nonzero(affprop.labels_ == cluster_id)])
#         cluster_str = ", ".join(cluster)
#         print(" - *%s:* %s" % (exemplar, cluster_str))


def main():
    with open('tags.json', 'r') as file_reader:
        tag_dict = json.load(file_reader)

        # real_list_of_tags(tag_dict)
        from collections import OrderedDict
zt
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
