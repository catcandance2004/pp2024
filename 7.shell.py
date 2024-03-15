import os
import sys
import subprocess
from shlex import split

class Shell:
    def __init__(self):
        self.input_file = None
        self.output_file = None

    def execute_command(self, command):
        if self.input_file:
            with open(self.input_file, 'r') as f:
                command = f'{command} < {self.input_file}'
                self.input_file = None
        if self.output_file:
            with open(self.output_file, 'w') as f:
                command = f'{command} > {self.output_file}'
                self.output_file = None
        process = subprocess.Popen(split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if error:
            print(f'Error: {error.decode()}')
        else:
            print(output.decode())

    def input_redirect(self, filename):
        self.input_file = filename

    def output_redirect(self, filename):
        self.output_file = filename

if __name__ == '__main__':
    shell = Shell()
    while True:
        command = input('> ')
        if command.lower() == 'exit':
            break
        elif '|' in command:
            left, right = command.split('|')
            output = subprocess.check_output(split(left), universal_newlines=True, stderr=subprocess.PIPE, shell=True)
            if output:
                command = right.strip()
                command = command.replace('$', output)
                shell.execute_command(command)
            else:
                print(f'Error: {output}')
        else:
            shell.execute_command(command)