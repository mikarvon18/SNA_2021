import praw
import matplotlib.pyplot as plt
import networkx as nx
import pickle
from prawcore.exceptions import Forbidden
from datetime import datetime
import time

NUM_OF_SUBREDDITS = 5
NUM_OF_USERS_PER_SUBREDDIT_TOP = 5
NUM_OF_SUBREDDITS_PER_USER_TOP = 3
NUM_OF_USERS_PER_SUBREDDIT_INNER = 5
NUM_OF_SUBREDDITS_PER_USER_INNER = 5
COUNTER = 0
result_list = []



#secret = l2lkbw5xrjyHqUhHH3-U8JbxFDlwuA
#client_id = N0yT2MUgrlY2bg

def findRelatedUsers(amount, r, subreddit, list_of_subreddits):
	#print("**********TOP LEVEL***************")
	#print(f"Finding related users of {subreddit}")
	users = []
	submissions_user = r.subreddit(subreddit).new(limit=None)
	for submission in submissions_user:
		try:
			author = submission.author
		except:
			print("Error getting author")
		if len(users) >= amount:
			break
		elif author not in users:
			users.append(author)
			#i += 1
		#print(submission.author)
		#print(i)
	#print(users)
	for j in users:
		try:
			findRelatedSubreddits(NUM_OF_SUBREDDITS_PER_USER_TOP, r, str(j), list_of_subreddits, users, subreddit)
		except:
			print("ERROR")
			continue
	#findRelatedSubreddits(NUM_OF_SUBREDDITS_PER_USER_TOP, r, "hemuli")


def findRelatedSubreddits(amount, r, user, list_of_subreddits, users, original_subreddit):
	global COUNTER

	#print(f"Finding related subreddits of {user}")
	subreddits = []
	submissions = r.redditor(user).submissions.new(limit=None)
	for submission in submissions:

		try:
			subreddit = submission.subreddit
		except:
			print("Error getting subreddit")
		if (str(subreddit)[0] == 'u') and (str(subreddit)[1] == '_'):
			continue
		elif len(subreddits) >= amount:
			break
		elif subreddit not in list_of_subreddits and subreddit not in subreddits:
			subreddits.append(subreddit)
			#print(submission.subreddit)
	#print(subreddits)
	for num, i in enumerate(subreddits):
		try:
			findRelatedUsersSecond(NUM_OF_USERS_PER_SUBREDDIT_INNER, r, str(i), subreddits, users, original_subreddit)
		except:
			print("ERROR")
			continue


def findRelatedUsersSecond(amount, r, subreddit, list_of_subreddits, top_level_users, original_subreddit):
	#print("**********INNER LEVEL***************")
	#print(f"Finding related users of {subreddit}")
	users = []
	submissions_user = r.subreddit(subreddit).new(limit=None)
	for submission in submissions_user:
		try:
			author = submission.author
		except:
			print("Error getting author")
		if (str(subreddit)[0] == 'u') and (str(subreddit)[1] == '_'):
			continue
		if len(users) >= amount:
			break
		elif author not in users and author not in top_level_users:
			users.append(author)
			#i += 1
		#print(submission.author)
		#print(i)

	#print(users)

	for j in users:
		try:
			findRelatedSubredditsSecond(NUM_OF_SUBREDDITS_PER_USER_INNER, r, str(j), list_of_subreddits, subreddit, original_subreddit)
		except:
			print("ERROR")
			continue
	#findRelatedSubreddits(NUM_OF_SUBREDDITS_PER_USER_TOP, r, "hemuli")

def findRelatedSubredditsSecond(amount, r, user, list_of_subreddits, level_2_subreddit, original_subreddit):
	#print(f"Finding related subreddits of {user}")
	subreddits = []
	submissions = r.redditor(user).submissions.new(limit=None)
	for submission in submissions:
		try:
			subreddit = submission.subreddit
		except:
			print("Error getting subreddit")
		if len(subreddits) >= amount:
			break
		elif subreddit not in list_of_subreddits and subreddit not in subreddits:
			
			subreddits.append(subreddit)
			#print(submission.subreddit)

	#print(subreddits)
	for num, i in enumerate(subreddits):
		if str(i) != original_subreddit:
			result_list.append([original_subreddit, level_2_subreddit, str(i)])
	#print("*******")
	#print(list_of_subreddits)
	#print("*******")
	#for i in subreddits:
	#	findRelatedUsersSecond(NUM_OF_USERS_PER_SUBREDDIT_INNER, r, str(i), subreddits)

def run():
	global COUNTER
	print("running script")
	r = praw.Reddit(user_agent='sna_project_acc',
					client_id='N0yT2MUgrlY2bg', 
					client_secret='l2lkbw5xrjyHqUhHH3-U8JbxFDlwuA',
					)
	r.read_only = True

	top_subreddits = []


	submissions = r.subreddit('all').hot(limit=None)
	for submission in submissions:
		subreddit = submission.subreddit
		if len(top_subreddits) >= NUM_OF_SUBREDDITS:
			break
		elif subreddit not in top_subreddits:
			top_subreddits.append(subreddit)
	#print("*******TOP LEVEL SUBREDDITS*************")
	#print(top_subreddits)
	for num, k in enumerate(top_subreddits):
		print(f"Loop: {num} / {len(top_subreddits)}")
		findRelatedUsers(NUM_OF_USERS_PER_SUBREDDIT_TOP, r, str(k), top_subreddits)
	#print("RESULS:")
	#print(top_subreddits)
	#for i in result_list:
	#	print(i)
def main():
	start = time.time()
	now = datetime.now()
	try:
		run()
	except:
		print("Crashed :(")
	print(f"Total run time: {(time.time() - start):2f}")
	with open(f'data-{now.strftime("%b-%d-%Y--%H-%M")}__{str(NUM_OF_SUBREDDITS)}-{str(NUM_OF_USERS_PER_SUBREDDIT_TOP)}-{str(NUM_OF_SUBREDDITS_PER_USER_TOP)}-{str(NUM_OF_USERS_PER_SUBREDDIT_INNER)}-{str(NUM_OF_SUBREDDITS_PER_USER_INNER)}.txt', 'wb') as fp:
	    pickle.dump(result_list, fp)

if __name__ == '__main__':
	main()
