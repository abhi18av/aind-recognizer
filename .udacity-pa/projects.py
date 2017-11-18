import argparse
import os
import shutil

from udacity_pa import udacity

nanodegree = 'nd889'
projects = ['recognizer']
filenames_all = ['asl_recognizer.ipynb', 'asl_recognizer.html',
                 'my_model_selectors.py', 'my_recognizer.py']


def submit(args):
    filenames = []
    for filename in filenames_all:
        if os.path.isfile(filename):
            filenames.append(filename)

    udacity.submit(
        nanodegree,
        projects[0],
        filenames,
        environment=args.environment,
        jwt_path=args.jwt_path)
