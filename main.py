import sys
import base64
import cli_processor
import re

def main(args):
    result_string = args.string
    for x in range(args.iterations):
        if(args.mode == 'decode'):
            result_string = re.sub('\(.*\)', '', base64.b64decode(result_string).decode('utf-8'))
        else:
            result_string = base64.b64encode(result_string.encode('utf-8')).decode('utf-8')
    print(result_string)

args = sys.argv
instructions = cli_processor.process_cli_args(args)
main(instructions)