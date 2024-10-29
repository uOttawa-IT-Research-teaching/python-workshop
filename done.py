import requests
import sys

SERVER="https://play.jarno.ca:12080"

def imdone(chapter, exercise):
    try:
        r = requests.get(f'{SERVER}/done_chap{chapter}ex{exercise}')
        if r.status_code < 200 or r.status_code >= 300:
            print(f"Failed to connect to server ({r.status_code})", file=sys.stderr)
        else:
            print("Success")
    except:
        print("Failed to connect to server", file=sys.stderr)

def quizanswer(chapter, quiz, answer):
    try:
        r = requests.get(f'{SERVER}/quiz_chap{chapter}q{quiz}', params={"answer": answer})
        if r.status_code < 200 or r.status_code >= 300:
            print(f"Failed to connect to server ({r.status_code})", file=sys.stderr)
        else:
            print("Success")
    except:
        print("Failed to connect to server", file=sys.stderr)
