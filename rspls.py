#!/usr/bin/env python3
import argparse, random, sys

# Global settings
__version__ = '1.0'
__build__ = '20200630'
RSPLS = ['rock', 'Spock', 'paper', 'lizard', 'scissors']

def name_to_number(input1):
    return RSPLS.index(input1)

def number_to_name(input1):
    return RSPLS[input1]

def rspls(p1_trw, cpu, debug):
    result = (cpu - name_to_number(p1_trw)) % 5
    jout = dict([('cpu', number_to_name(cpu)), ('player1', p1_trw), ('result', str(result))])
    if debug:
        print('[+] ', end = '')
        print(jout)
    if (result == 3) or (result == 4):
        print('[+] Player1 wins!')
    elif (result == 1) or (result == 2):
        print('[+] Computer wins!')
    else:
        print('[+] Tie!')

def main():
    parser = argparse.ArgumentParser(description='RSPLS: Rock, Spock, Paper, Lizard, Scissors! Version ' + __version__ + ', build ' + __build__ + '.')
    parser.add_argument('-D', '--debug', action='store_true', help='Debug/verbose mode')
    parser.add_argument('-i', '--input', metavar='<User\'s input>', type=str, help='Player1\'s input, must be one of \'rock\', \'Spock\', \'paper\', \'lizard\', or \'scissors\'')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))
    args = parser.parse_args() # parse command line

    # In case of no arguments shows information from the main list
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Player1's input is stored in a string variable
    # validation consists of checking whether the input is present in RSPLS (list)
    player1_throw = args.input
    DEBUG = args.debug

    try:
        name_to_number(player1_throw)
        if DEBUG: print('[+] Valid input...')
    except ValueError:
        if DEBUG: print('[-] Input is invalid!')
        sys.exit(10)

    # Computer's input is a random number between 0 and 4 
    cpu_throw = random.randrange(5)

    rspls(player1_throw, cpu_throw, DEBUG)

if __name__ == '__main__':
    main()

