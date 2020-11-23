#! /usr/bin/python2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-u', metavar='unit', type=str, required=True, help='Systemd unit to display')
parser.add_argument('-f', default=False, action='store_true', help='Follows the log')
parser.add_argument('-n', metavar='num', type=int, help='Num of lines to display')
args = parser.parse_args()

log_path = '/var/log/journal/{}.service.log'.format(args.u)
if args.f:
    os.system('tail -n 10 -F {}'.format(log_path))
elif args.n:
    os.system('tail -n {} {}'.format(args.n, log_path))
else:
    os.system('less {}'.format(log_path))
