## RSPLS: Rock, Spock, Paper, Lizard, Scissors!
### Version: 1.0

### Usage:
```
usage: rspls.py [-h] [-D] [-i <User's input>] [-v]

RSPLS: Rock, Spock, Paper, Lizard, Scissors! Version 1.0, build 20200630.

optional arguments:
  -h, --help            show this help message and exit
  -D, --debug           Debug/verbose mode
  -i <User's input>, --input <User's input>
                        Player1's input, must be one of 'rock', 'Spock',
                        'paper', 'lizard', or 'scissors'
  -v, --version         show program's version number and exit
```

### Examples:
- Valid inputs
```
$ ./rspls.py -i rock 
[+] Computer wins!

$ ./rspls.py -i Spock
[+] Player1 wins!

$ ./rspls.py -i paper
[+] Computer wins!

$ ./rspls.py -i lizard
[+] Computer wins!

$ ./rspls.py -i scissors
[+] Tie!

$ echo $?               
0
```

- Wrong input
```
$ ./rspls.py -i test    

$ echo $?
10
```

- With Debug option
```
$ ./rspls.py -Di test
[-] Input is invalid!

$ ./rspls.py -Di Spock
[+] Valid input...
[+] {'cpu': 'rock', 'player1': 'Spock', 'result': '4'}
[+] Player1 wins!
```

