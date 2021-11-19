#!/usr/bin/python3

import sys
import requests
import time

def main():

    host = sys.argv[1]
    file_list = sys.argv[2]
    
    f = open(file_list, "r")
    lines = f.readlines()
   
    intro()


    for line in lines:
        res = requests.get('http://' + host + '/' + line.rstrip())
        #print(res.headers)
        #print(res.text)

        if res.status_code == 200:
            for line2 in lines:
                res2 = requests.get('http://' + host + '/' + line.rstrip() + '/' + line2.rstrip())

                print('Path: /' + line.rstrip() + '/' + line2.rstrip() + '         Status Code: ' + str(res.status_code))
        
        print('Path: /' + line.rstrip() + '         Status Code: ' + str(res.status_code))

def intro():
    print('############### DIRECTORY DISCOVERY ###############')
    print('Host: ' + sys.argv[1])
    print('Wordlist: ' + sys.argv[2])
    print('###################################################')
    time.sleep(2)


if __name__ == "__main__":
    main()

