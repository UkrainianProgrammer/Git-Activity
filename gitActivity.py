# libs
import requests
import sys

import constants

# Use the following URLs:
# https://api.github.com/users/<username>/events - events for user
# https://api.github.com/users/{username} - checks for user info
# https://docs.github.com/en/rest/using-the-rest-api/github-event-types?apiVersion=2022-11-28#event-object-common-properties
# Example: https://api.github.com/users/kamranahmedse/events

# example output of the events
'''
[
  {
    "id": "40012584399",
    "type": "PushEvent",
    "actor": {
      "id": 15058374,
      "login": "UkrainianProgrammer",
      "display_login": "UkrainianProgrammer",
      "gravatar_id": "",
      "url": "https://api.github.com/users/UkrainianProgrammer",
      "avatar_url": "https://avatars.githubusercontent.com/u/15058374?"
    },
    "repo": {
      "id": 759505103,
      "name": "UkrainianProgrammer/WritingReact",
      "url": "https://api.github.com/repos/UkrainianProgrammer/WritingReact"
    },
    "payload": {
      "repository_id": 759505103,
      "push_id": 19248874864,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "ee5b4cf67a2d028d190da3b0d37c2a490b875486",
      "before": "3ab09a32f5fcbff7fad49c46eecd4db5b307fb33",
      "commits": [
        {
          "sha": "ee5b4cf67a2d028d190da3b0d37c2a490b875486",
          "author": {
            "email": "insten490@gmail.com",
            "name": "Alex S"
          },
          "message": "minor styles updates and new header",
          "distinct": true,
          "url": "https://api.github.com/repos/UkrainianProgrammer/WritingReact/commits/ee5b4cf67a2d028d190da3b0d37c2a490b875486"
        }
      ]
    },
    "public": true,
    "created_at": "2024-07-10T04:34:21Z"
  }
]
'''

# example CLI output:
# - Pushed 3 commits to kamranahmedse/developer-roadmap
# - Opened a new issue in kamranahmedse/developer-roadmap
# - Starred kamranahmedse/developer-roadmap
# - ...

# TODOs:
# Handle API error codes

# Handle multiple event types
def fetchData(username):
   # https://api.github.com/users/<username>/events
   # happens after validation
   eventsUrl = f"https://api.github.com/users/{username}/events"
   request = requests.get(eventsUrl.format(username))

   if request.status_code == constants.STATUS_SUCCESS:
    pass
   

# Validate user
def validateGitUser(username: str) -> bool:
    url = f"https://api.github.com/users/{username}"
    request = requests.get(url.format(username))

    if request.status_code == constants.STATUS_SUCCESS:
      userInfo = request.json()
      print(userInfo)
      return True
    elif request.status_code == constants.STATUS_NOT_FOUND:
        raise Exception(f"User {username} does not exist.")
    else:
       return False

# functions
def main(username):
   validateGitUser(username)

#main
if __name__ == '__main__':
  try:
    args = sys.argv[1:]
  except:
    raise ValueError("Missing arguments. Exiting...")
  
  if len(args) > 1 and args[0] != "-h":
      # invalid args
      raise ValueError("Invalid arguments. Exiting...")
  elif args[0] == "-h" and len(args) == 1:
      # help info
      print ('gitActivity.py <username>')
      sys.exit()
  elif len(args) == 1:
      main(sys.argv[1])
  else:
      # TODO: maybe implement activity for multiple users?
      # invalid args
      raise ValueError("Invalid arguments. Exiting...")
