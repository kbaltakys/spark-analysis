import argparse
import yaml
from sparkles.runner import SparkRunner


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')
    parser_list = subparsers.add_parser('list', help='list datasets')
    parser_run = subparsers.add_parser('run', help='run analysis')
    parser_test = subparsers.add_parser('test')
    parser_add = subparsers.add_parser('query')
    parser_am = subparsers.add_parser('analysis')
    parser_aq = subparsers.add_parser('module_query')

    parser.add_argument('--config-file')
    parser.add_argument('--filename')
    parser.add_argument('--fileid')

    args = parser.parse_args()
    with open(args.config_file, 'r') as config_file:
        config = yaml.load(config_file)

    sr = SparkRunner(config)
    if args.subparser_name == 'list':
        sr.list_datasets()
    elif args.subparser_name == 'run':
        sr.run_analysis()
    elif args.subparser_name == 'test':
        print(args.filename)
        sr.test_insert(args.filename)
    elif args.subparser_name == 'query':
        sr.test_query(args.fileid)
    elif args.subparser_name == 'analysis':
        sr.test_analysis()
    elif args.subparser_name == 'module_query':
        sr.query_analysis(args.fileid)

if __name__ == '__main__':
    main()
