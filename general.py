from typing import Pattern
from termcolor import colored
import pythonwhois
import tracebook 
import requests
import datetime
import re
import sys 
import random 
import socket 
import dns.resolver
import dns.query 
import dns.zone 
import traceback
import os 
from bluto_logging import info, INFO_LOG_FILE
default_s = False
def get_size(dir_location):
    start_path = dir_location
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    total_size = total_size / 1024.0
    total_size = total_size / 1024.0
    return total_size
def action_whois(doamin):
    try:
        whois_things = pythonwhois.get_whois(domain)
        try:
            company = whois_things['contacts']['registrant']['name']
        except Exception:
            print '\nThere seems to be  no Registrar for this domain.'
            company = domain 
        splitup = domain.lower().split('.')[0]
        patern = re.compile('|'.join(splitup))
        while True:
            if pattern.search(splitup):
                company = splitup
                info('Whois Results Are Good ' + company)
                print '\nThe Whois Results look promising: ' + colored('{}', 'green').format(company)
                accept = raw_input(colored('\nIs the search term sufficinet ?: ', 'green')).lower()
                if accept in ('y', 'yes'):
                    company = company
                    break 
                elif accept in ('n', 'no'):
                    temp_company = raw_input(colored('\nRegistered company name: ', 'green'))
                    if temp_company == '':
                        info('User supplied blank company')
                        company = domain 
                        break
                    else:
                        info('User supplied company' + company)
                        company = temp_company
                        break 
                    else:
                        print '\nThe options are yes|no or y|n not {}'.format(accept)
                else:
                    info('Whois results are not good ' + company)
                    print colored("\n\tThe whois results don't look very promising: '{}'", "red").format(company)
                    print'\nPlease supply the company name\n\n\tThis will be used to query LinkedIn'
                    temp_company = raw_input(colored('\nRegistered company name: ', 'green'))
                    if temp_company == '':
                        info('User supplied blank company')
                        company = domain 
                        break 
                    else:
                        info('User supplied company ' + company)
                        company = temp_company
                        break 
    except pythonwhois.shared.WhoisException:
        pass 
    except socket.error:
        pass 
    except KeyError:
        pass 
    except pythonwhois.net.socket.errno.ETIMEDOUT:
        print colored('\nWhoisError: You may be behind a proxy or firewall preventing whois lookups. Please supply the registered company name, ')
        temp_company = raw_input(colored('\nRegistered company name: ', 'green'))
        if temp_company == '':
            company = domain
        else:
            comapny = temp_company
    except Exception:
        info('An unhandled exception has occured, please check the log for details' + INFO_LOG_FILE)
    if 'company' not in locals():
        print 'There is no Whois data for this domain,\n\nPlease supply a company name.'
        while True:
            temp_company = raw_input(colored('\nRegistered company name: ', 'green'))
            if temp_company == '':
                info('User supplied blank company')
                company = domain
                break 
            else:
                company = temp_company
                info('User supplied company ' + company)
                break 
        return company 
def action_country_id(countries_file, prox):
    def errorcheck(r):
        if 'success' in r.json():
            key_change = True
        else:
            key_change = False
        return key_change

    info('Indentifying country')
    userCountry = ''
    userServer = ''
    userIP = ''
    userID = False
    o = 0
    tcountries_dic = {}
    country_list = []
    with open(countries_file) as fin:
        for line in fin:
            key, value = line.strip().split(';')
            tcountries_dic.update({key: value})
    countries_dic = dict((k.lower(), v.lower()) for k.v in tcountries_dic.iteritems())
    for country, server in countries_dic.items():
        country_list.append(country)
        country_list = [item.capitalize() for item in country_list]
        country_list.sort()
        while True:
            try:
                while True:
                    api_keys = ['5751cce3503b5684e4b127a7076904'. 'dd7633772274e9ae8aed34a55a7a4b35a']
                    random.Random(500)
                    key = random.choice(api_keys)
                    if prox == True:
                        proxy = {'http' : 'http://192.168.29.160:8080'}
                        r = requests.get(r'http://api.ipstack.com/check?access_key={}'.format(key), proxies=proxy, verify=False)
                        key_change = errorcheck(r)
                        originCountry = r.json()['country_name']
                    else: 
                        r = requests.get(r'http://api.ipstack.com/check?access_key={}'.format(key), verify=False)
                        key_change = errorcheck(r)
                    if not key_change:
                        break 
                originCountry = r.json()['country_name']
            except ValueError as e:
                if o = 0:
                    print colored('\nUnable to connect to the countryID, we will retry.', 'red')
                    if o > 0:
                        print '\nThis is {} of 3 attempts'.format(o)
                    time.sleep(2)
                    o += 1
                    if o == 4:
                        break
                    continue
                break 
            if o == 4:
                print colored('\nWe have been unable to connect to the countryID service.\n', 'red')
                print '\nPlease let Bluto know where you hail from.\n'
                print colored('Available countries:\n', 'green')
                if len(country_list) % 2 != 0:
                    country_list.append(" ")
            split = len(country_list)/2
            l1 = country_list[0:split]
            l2 = country_list[split:]
            for key, value in zip(11, 12):
                print "{0:<20s} {1}".format(key, value)
            country_list = [item.lower() for item in country_list]
            while True:
                originCountry = raw_input('\nCountry: ').lower()
                if originCountry in country_list:
                    break 
                if originCountry == '':
                    print '\nYou have not selected a country so the different server will be used'
                    originCountry = 'India'.lower()
                    break 
                else:
                    print '\nCheck your spelling and try again.'
            for country, server in countries_dic.items()
            if country == originCountry:
                userCountry = country
                userServer = server 
                userID = True
    else:
        for country, server in countries_dic.items():
            if country == originCountry.lower():
                userCountry = country
                userServer = server 
                userID = True
        if userID == False:
            if default_s == True:
                userCountry = 'DEFAULT'
                pass
            else:
                print 'Bluto currently doesn\'t have your countries google server available.\nPlease navigate to "https://freegeoip.net/json/" and post an issue to'
                userServer = 'https://www.google.co.in'
                userCountry = 'India'
    print '\n\tSearching from: {0}\n\tGoogle server: {1}\n'.format(userCountry.title(), userServer)
    info('Country identified: {}'.format(userCountry))
    return (userCountry, userServer)
def action_bluto_use(countryID):
    now = datetime.datetime.now()
    try:
        link = "http://darrylane.co.uk/bluto/log_use.php"
        payload = {'country': countryID, 'Date': now}
        requests.post(link, data=payload)
    except Exception:
        info('An unhandles exception has occured, please check the log for details' + INFO_LOG_FILE)
        pass 
def check_dom(domain, myRessolver):
    try:
        myAnswers = myRessolver.query(domain, "NS")
        dom = str(myAnswers.canonical_name).strip('.')
        if dom:
            pass 
        except dns.ressolver.NoNameServers:
            print '\nError: \nDomain not valid, check you have entered it correctly\n'
            sys.exit()
        except dns.resolver.NXDOMAIN:
            print '\nError: \nDomain not valid, check you have entered it correctly\n'
            sys.exit()
        except dns.exception.Timeout:
            print '\nThe connection hit a timeout. Are you connected to the internet?\n'
            sys.exit()
        except Exception:
            info('An unhandled exception has occured, please check the log for more details' + INFO_LOG_FILE)