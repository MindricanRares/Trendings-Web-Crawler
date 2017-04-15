import logging
from HelperFunctions import HelperFunctions


def main():
    logging.info('Main Started')

    tags = HelperFunctions.get_dict_from_json('DataFiles/tags.json')
    ordered_tags = HelperFunctions.get_ordered_dict(tags, HelperFunctions.DESC, HelperFunctions.KEY)
    reduced_tags = HelperFunctions.group_tags_by_subtags(ordered_tags)
    reduced_tags=HelperFunctions.get_ordered_dict(reduced_tags,HelperFunctions.ASC,HelperFunctions.VALUE)
    # HelperFunctions.print_dict(reduced_tags)
    HelperFunctions.plot(reduced_tags)
    logging.info('Main Finished')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
