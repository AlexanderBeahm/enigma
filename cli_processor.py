import argparse
from instructions import Instructions

def process_cli_args(args):
    currentIndex = 0
    skipIndex = 0
    instructions = None
    for item in args:
        if(skipIndex == currentIndex):
            currentIndex = currentIndex + 1
            continue
        if(item == 'decode'):
            if(instructions is None):
                instructions = Instructions("decode")
            else:
                print("Not allowed to have multiple methods.")
                raise Exception()
        elif(item == 'encode'):
            if(instructions is None):
                instructions = Instructions("encode")
            else:
                print("Not allowed to have multiple methods.")
                raise Exception()
        elif(item == 'main.py'):
            print("found main method")
        elif(item == '-i'):
            iterations = int(args[currentIndex+1])
            instructions.iterations = iterations
            skipIndex = currentIndex + 1
        else:
            instructions.string = item
        currentIndex = currentIndex + 1
    return instructions
