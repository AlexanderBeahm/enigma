import sys
import base64
import cli_processor

def main(args):
    result_string = args.string
    for x in range(args.iterations):
         result_string = base64.b64decode(result_string)
    print(result_string.decode('utf-8'))

args = sys.argv
instructions = cli_processor.process_cli_args(args)
main(instructions)