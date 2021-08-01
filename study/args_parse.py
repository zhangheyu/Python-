import sys
import argparse
import os


parser = argparse.ArgumentParser()

parser.add_argument('--send_dir', '-d',
                    help='Send logs in the specified directory')
parser.add_argument('--bta', default=False,
                    help='Send log with bta use single process', action='store_true')
parser.add_argument('--local_time', default=False,
                    help='Change timestamp to now', action='store_true')
parser.add_argument('--manual_server', '-m', default=False,
                    help='Send log to specified server')
parser.add_argument('--max_speed_line_per_second', default=0,
                    help='Max speend lines/second')
parser.add_argument('--threat_log', '-t', default=False,
                    help='Send Threat log manually', action='store_true')

print('argv:', sys.argv)
for idx in range(len(sys.argv)):
    arg = sys.argv[idx]
    print(arg)
    if arg.endswith('args_pars.py'):
        sys.argv = sys.argv[idx:]
    break

args = parser.parse_args()

print('parsed args:', args)

if args.send_dir:
    if not os.path.exists(args.send_dir):
        print('File not exist: %s' % (args.send_dir,))
    
    print(os.path.splitext(args.send_dir))
