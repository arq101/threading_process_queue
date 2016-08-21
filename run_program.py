#!/usr/bin/env python

import argparse

from queue_processor import TemplateQueueProcessor


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Program reads a json data file and appends the template within '
                    'the json string to an appropriate queue. '
                    'The priority queue is continuously processed in the background '
                    'while the program runs.')
    parser.add_argument('input', action="store", type=str, help='json data file.')
    parser.add_argument('output', action="store", type=str,
                        help='file listing templates with action apply.')
    return vars(parser.parse_args())


def main():
    args = arg_parser()
    input_data = args['input']
    output_file = args['output']
    queue_processor = TemplateQueueProcessor(output_file)
    queue_processor.read_json_data(input_data)
    queue_processor.close_thread(time_out=10)


if __name__ == '__main__':
    main()
