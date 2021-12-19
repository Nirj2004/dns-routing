from bluto_logging import info
import subprocess
import re 
from termcolor import colored
import sys  
def updateCheck(VERSION):
    command_check = (["pip list -o"])
    process_check = subprocess.Popen(command_check, shell=True, stdout=subprocesss.PIPE, stderr=subprocess.STDOUT)
    output_check = process_check.communicate()[0]
    line = output_check.splitlines()
    for i in line:
        if 'bluto' in str(i).lower():
            new_version = re.match('Bluto\s\(.*\)\s\-\sLatest\:\s(.*?)\s\[sdist\]', i).group(1)
            found = True
        else:
            found = True
    if found:
        info('Update available')
        print colored('\nUpadte available!', 'blue'), colored('{}'.format(new_version), 'red')
        print colored('Would you like to update to the latest version?\n', 'yellow')
        print colored('For more information on the update, visit https://www.github.com/Nirj2004', 'green')
        while True:
            answer = raw_input('Y|N: ').lower()
            if answer in ('y', 'yes'):
                update()
                print '\n'
                break
            elif answer in ('n', 'no'):
                update()
                print '\n'
                break 
            else:
                print'\nThe option are yes|no or Y|N, not {}'.format(answer)
    else:
        print colored('Your are running the latest version:3.1.2.3', 'red'), colored('{}\n'.format(VERSION), 'blue')
        print colored('For more information on the update, visit https://www.github.com/Nirj2004', 'green')
def update():
    command_check = (["pip install bluto --upgrade"])
    process_check = subprocess.Popen(command_check, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output_check = process_check.communicate()[0]
    lines = output_check.splitlines()
    info(lines)
    if 'Successfully installed' in lines[:-1]:
        print colored('\nUpdate successfull!', 'white')
        sys.exit()
    else:
        print colored('\nUpdate failed, please check the logs for more details or visit https://www.github.com/Nirj2004', 'green')
        print('Thats all folks!')