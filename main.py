from scholar import ScholarDriver
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-an", "--author-name", dest="author_name", help="search for name of author")
    group.add_argument("-u", "--url", dest="url", help="url of author")
    parser.add_argument("-o", "--output", dest="output", help="output file name", default="output.csv")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    driver = ScholarDriver()
    if args.author_name:
        driver.search_author(args.author_name)
        data = driver.get_all_publications()
    elif args.url:
        data = driver.get_all_publications(args.url)
    else:
        print("please enter a valid argument")

    if args.output:
        driver.save_data(args.output)

    print("done")


