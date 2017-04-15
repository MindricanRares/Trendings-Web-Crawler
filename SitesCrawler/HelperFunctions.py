from collections import OrderedDict
import json
import os
import matplotlib.pyplot
import matplotlib.pyplot
import numpy as np
import sklearn.cluster
import distance
from nltk.stem.wordnet import WordNetLemmatizer


class HelperFunctions(object):
    ASC = 1
    DESC = 0

    KEY = 0
    VALUE = 1

    @staticmethod
    def get_ordered_dict(original_dict, order, element):
        '''
        Orders a dictionary by the key elements.
        :param original_dict: 
        :param order , must be set to ASC or DESC:
        :parameter element,must be set to KEY or VALUE 
        :returns an order dictionary: 
        '''
        ordered_tags = OrderedDict(sorted(original_dict.items(),
                                          key=lambda kv: kv[element], reverse=order))
        return ordered_tags

    @staticmethod
    def get_dict_from_json(file_name):
        '''
        :param file_name: 
        :return a dictionary: 
        '''
        current_path = os.path.dirname(__file__)
        with open(file_name, 'r') as file_reader:
            dict_tag = json.load(file_reader)
        return dict_tag

    @staticmethod
    def print_dict(dict_to_be_printed):
        '''
        Prints a dictionary to the console
        :param dict_to_be_printed:  
        '''
        for key, value in dict_to_be_printed.iteritems():
            print key, value

    @staticmethod
    def group_tags_by_subtags(original_tags):
        tags = original_tags.keys()
        list = []
        for first_tag in tags:
            similar_tags = [first_tag]
            for second_tag in tags:
                if first_tag in second_tag and first_tag != second_tag:
                    similar_tags.append(second_tag)
                    # tags.remove(second_tag)
            # print similar_tags
            list.append(similar_tags)

        grouped_tags = []
        exceptions = ['c', 'int', 'r']
        for el in list:
            if len(el) > 2 and el[0] not in exceptions:
                grouped_tags.append(el)

        for grouped_tag in grouped_tags:
            for index in xrange(1, len(grouped_tag)):
                original_tags[grouped_tag[0]] += original_tags[grouped_tag[index]]
        for grouped_tag in grouped_tags:
            for index in xrange(1, len(grouped_tag)):
                if grouped_tag[index] in original_tags.keys():
                    del original_tags[grouped_tag[index]]
        return original_tags

    @staticmethod
    def plot(tags):
        new_dict = {'others': 0}
        i = 0
        for elem, key in tags.iteritems():
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



if __name__ == '__main__':
    test = {'python': 2, 'flask': 4, 'a': 1, 'b': 3, 'c': 2}
    print 'Started'
    print HelperFunctions.ASC
    print (HelperFunctions.KEY)
    new_test = HelperFunctions.get_ordered_dict(test, HelperFunctions.ASC, HelperFunctions.KEY)
    print new_test
    print HelperFunctions.get_dict_from_json('DataFiles/tags.json')
