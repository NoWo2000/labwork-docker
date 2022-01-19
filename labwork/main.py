#!/usr/bin/python3
#
# License: CC-0

import sys
import json
import requests

from labwork01 import handle_caesar_cipher, handle_strcat, handle_histogram 

if len(sys.argv) != 4:
    print("syntax: %s [API endpoint URI] [client ID] [assignment_name]" % (
        sys.argv[0]))
    sys.exit(1)

api_endpoint = sys.argv[1]
client_id = sys.argv[2]
assignment_name = sys.argv[3]

session = requests.Session()

result = session.get(api_endpoint + "/assignment/" +
                     client_id + "/" + assignment_name)
assert(result.status_code == 200)


assignment = result.json()
known_assignment_count = 0
unknown_assignment_count = 0
pass_count = 0

for testcase in assignment["testcases"]:
    # labwork01 
    if testcase["type"] == "strcat":
        known_assignment_count += 1
        response = handle_strcat(testcase["assignment"])
    
    elif testcase["type"] == "histogram":
        known_assignment_count += 1
        response = handle_histogram(testcase["assignment"])
    
    elif testcase["type"] == "caesar_cipher":
        known_assignment_count += 1
        response = handle_caesar_cipher(testcase["assignment"])
    
    # labwork[02-10]
           
    else:
        unknown_assignment_count += 1
        print("Do not know how to handle type: %s" % (testcase["type"]))
        continue
    
        
    result = session.post(api_endpoint + "/submission/" + testcase["tcid"], headers={
        "Content-Type": "application/json",
    }, data=json.dumps(response))
    assert(result.status_code == 200)
    submission_result = result.json()
    if submission_result["status"] == "pass":
        pass_count += 1
    else:
        print(submission_result)

print("%d known assignments, %d unknown." %
      (known_assignment_count, unknown_assignment_count))
print("Passed: %d. Failed: %d" %
      (pass_count, known_assignment_count - pass_count))
