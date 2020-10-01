import sys
import base64
import cli_processor

def main(args):
    encoded_string = args[1]
    iterations = int(args[2])
    print(encoded_string)
    print(iterations)
    result_string = encoded_string
    for x in range(iterations):
         result_string = base64.b64decode(result_string)
    print(result_string.decode('utf-8'))

args = sys.argv
main(args)