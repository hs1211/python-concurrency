import argparse
import multiprocessing
import os


def handle_commandline():
    parser = argparse.ArgumentParser()
    # optional argument
    parser.add_argument('-c', '--concurrency', type=int, default=multiprocessing.cpu_count(), help='specify the concurrency')
    parser.add_argument('-s', '--size', default=400, type=int, help='make a scaled image that fits the given dimension')
    parser.add_argument('-S', '--smooth', action='store_true', help='use smooth scaling')
    # positional argument
    parser.add_argument('source', help='the director containing the original images')
    parser.add_argument('target', help='the directory for scaled images')
    args = parser.parse_args()
    source=os.path.abspath(args.source)
    target=os.path.abspath(args.target)
    if source == target:
        args.error('source and target must be different')

    if not os.path.exists(args.target):
        os.makedirs(target)
    return args

if __name__ == '__main__':
    args = handle_commandline()
    print(args)