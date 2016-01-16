import sys

import authHandler
import twitterHandler
import apiHandler
import googleHandler
import redditHandler

api = AuthHandler.login()
fileName = twitterHandler.getTweets(api, sys.argv[1])
responseList = apiHandler.getData(fileName)
# recommendationList = googleHandler.getRec(responseList)

# get the username and password somehow, probably from http request or commandline args

# changesList = redditHandler(recommendationList, user, pass)
# if(!twitterHandler.sendResult(changesList, user, pass, profile)) print("not able to send DM")
# else print("success")



