import traceback 
import sys 
import random 
from termcolor import colored 
from bluto_logging import info, INFO_LOG_FILE
def get_user_agents(useragent_f):
    info('Gathering UserAgents')
    uas = []
    with open(useragent_f, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    info('Completed gathering UserAgents')
    return uas 
def get_subs(filename, domain):
    info('Gathering subdomains')
    full_list = []
    try:
        subs = [line.rstrip('\n') for line in open (filename)]
        for sub in subs:
            full_list.append(str(sub.lower() + "." + domain))
    except Exception:
        info('An unhandled exception has occured, please check the log for details' + INFO_LOG_FILE)
        sys.exit()
    info('Completed gathering sundomains')
    return full_list
def get_sub_interest(filename, domain):
    info('Sorting subdomains of required interests')
    full_list = []
    try:
        subs = [line.rstrip('\n') for line in open(filename)]
        for sub in subs:
            full_list.append(str(sub.lower() + "." + domain))
    except Exception:
        info('An unexpected error has occured, please check the log for more details' + INFO_LOG_FILE)
        sys.exit()
    info('Completed gathering subdomains of interest')
    return full_list
def get_line_count(filename):
    info('Gathering subdomains count.')
    lines = 0
    for lines in open(filename):
        lines += 1
    info('Compiled gathering subdomains count')
    return lines