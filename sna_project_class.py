import praw
import matplotlib.pyplot as plt
import networkx as nx
import pickle
from prawcore.exceptions import Forbidden
from datetime import datetime
import time

TOP_SUBREDDITS = 3


r = praw.Reddit(user_agent='sna_project_acc',
					client_id='N0yT2MUgrlY2bg', 
					client_secret='l2lkbw5xrjyHqUhHH3-U8JbxFDlwuA',
					)

class TopLevelSubreddits:
	def __init__(self, size, praw):
		print("here")


def main():
	r = praw.Reddit(user_agent='sna_project_acc',
					client_id='N0yT2MUgrlY2bg', 
					client_secret='l2lkbw5xrjyHqUhHH3-U8JbxFDlwuA',
					)
	topLevelSubreddits = TopLevelSubreddits(TOP_SUBREDDITS, r)


if __name__ == '__main__':
	main()