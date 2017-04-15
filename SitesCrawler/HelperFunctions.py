from collections import OrderedDict


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


if __name__ == '__main__':
    test = {'python': 2, 'flask': 4, 'a': 1, 'b': 3, 'c': 2}
    print 'Started'
    print HelperFunctions.ASC
    print (HelperFunctions.KEY)
    new_test = HelperFunctions.get_ordered_dict(test, HelperFunctions.ASC,HelperFunctions.KEY)
    print new_test
