# parsing command line args
import argparse

parser = argparse.ArgumentParser(
    description="A simple argument parser",
    epilog="-h help text",
)

parser.print_help()
parser.add_argument("echo", help="echo the string you use here",
                    type=str, default="Hello World")
args = parser.parse_args()
print(args.echo)
