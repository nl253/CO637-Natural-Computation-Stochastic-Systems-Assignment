#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard Library
from argparse import ArgumentParser, Namespace
from os.path import basename

parser: ArgumentParser = ArgumentParser(
    prog=basename(__file__).replace('.py', ''),
    description='solutions to stochastic systems assessment')

parser.add_argument(
    'exercise',
    help='the exercise number',
    choices=[1, 2, 3, 4],
    type=int)

parser.add_argument(
    '--debug',
    help='turn on very verbose logging',
    action='store_true',
    default=False)

parser.add_argument(
    '--test',
    help='run tests for the exercise instead of running it',
    action='store_true',
    default=False)

args: Namespace = parser.parse_args()

if args.debug:
    import logging
    from logging import DEBUG
    logging.basicConfig(level=DEBUG, format='[%(levelname)s] %(message)s')

if args.exercise < 0 or args.exercise > 4:
    raise NotImplementedError(
        f'exercise number "{args.exercise}" is invalid, try 1-4')

if args.test:
    if args.exercise == 1:
        from tests import test_exercise_1
        test_exercise_1()
    elif args.exercise == 2:
        from tests import test_exercise_2
        test_exercise_2()
    elif args.exercise == 3:
        from tests import test_exercise_3
        test_exercise_3()
    elif args.exercise == 4:
        from tests import test_exercise_4
        test_exercise_4()
else:
    from utils import print_matrix
    #  print_heading(f'Solution to exercise {args.exercise}')

    if args.exercise == 1:
        from markov import exercise_1
        _, trans_table = exercise_1()
        print_matrix(trans_table)

    elif args.exercise == 2:
        from markov import exercise_2
        _, trans_table = exercise_2()
        print_matrix(trans_table)

    elif args.exercise == 3 or args.exercise == 4:
        from markov import exercise_3, exercise_4
        ((p1, std1), (p3, std3), (p9, std9)) = exercise_3() if args.exercise == 3 else exercise_4()

        for s, p, std in [(1, p1, std1), (3, p3, std3), (9, p9, std9)]:
            print(f'p(state = {s}) = {p}+-{std}')
