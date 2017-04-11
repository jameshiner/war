#!/usr/bin/python3

import os
import sys
import random
import time

class Deck:

	def __init__(self, x):
		self.rankShort = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
		self.rankLong = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
		self.suitShort = ["♦", "♥", "♠", "♣"]
		self.suitLong = ["Diamonds", "Hearts", "Spades", "Clubs"]
		self.deck = []
		for i in range(x):
			for q in range(len(self.suitShort)):
				for w in range(len(self.rankShort)):
					card = Card(self.suitShort[q], self.suitLong[q], self.rankShort[w], self.rankLong[w], w)
					self.deck.append(card);

	def __str__(self):
		res = []
		for x in self.deck:
			res.append(str(x))
		return ', '.join(res)
	def getDeck(self):
		return self.deck
	def getDeckLength(self):
		return len(self.deck)
	def shuffle(self):
		random.shuffle(self.deck)
	def deal(self):
		return self.deck.pop()



class Card:
	def __init__ (self, suitShort, suitLong, rankShort, rankLong, value):
		self.suitShort = suitShort
		self.suitLong = suitLong
		self.rankShort = rankShort
		self.rankLong = rankLong
		self.value = value

	def getSuitShort(self):
		return self.suitShort
	def getSuitLong(self):
		return self.suitLong
	def getRankShort(self):
		return self.rankShort
	def getRankLong(self):
		return self.rankLong
	def getValue(self):
		return self.value
	def toString(self):
		return str(self.rankLong + ' of ' + self.suitLong)
	def __str__(self):
		return str(self.rankShort + self.suitShort)

class Player:
	def __init__(self, name, bank=500):
		self.name = name
		self.bank = bank
		self.hand = []

	def getName(self):
		return self.name
	def getBank(self):
		return self.bank
	def getHand(self):
		return self.hand
	def getHandLength(self):
		return len(self.hand)
	def getHandString(self):
		res = []
		for x in self.hand:
			res.append(str(x))
		return ', '.join(res)
	def deal(self, x):
		self.hand.append(x)



def simpleWar():
	startTime = time.time()
	round = 1
	p1w = 0
	p2w = 0
	wars = 0
	players = []
	players.append(Player("X"))
	players.append(Player("Y"))
	p1 = players[0]
	p2 = players[1]
	p1_s = []
	p2_s = []
	deck = Deck(1);
	deck.shuffle()
	while deck.getDeckLength() > 0:
		for player in players:
			player.deal(deck.deal())
	while p1.getHandLength() > 0 and p2.getHandLength() > 0:
		card1 = p1.getHand().pop(0)
		card2 = p2.getHand().pop(0)

		print("Round: %d - P1 Wins: %d - P2 Wins: %d - Wars: %d" % (round,p1w,p2w,wars))
		print('Player 1 - Card: ' + str(card1) + ' - Value: ' + str(card1.value))
		print('Player 2 - Card: ' + str(card2) + ' - Value: ' + str(card2.value))
		if (card1.value > card2.value):
			p1.hand.append(card1)
			p1.hand.append(card2)
			p1.hand.extend(p1_s+p2_s)
			p1_s = []
			p2_s = []
			print('Player 1 wins')
			p1w+=1
		elif (card1.value < card2.value):
			p2.hand.append(card1)
			p2.hand.append(card2)
			p2.hand.extend(p1_s+p2_s)
			p1_s = []
			p2_s = []
			print('Player 2 wins')
			p2w+=1
		else:
			p1_s.append(card1)
			p1_s.extend(p1.getHand()[:3])
			p1.hand = p1.getHand()[3:]
			p1.hand.insert(0,p1_s.pop())
			p2_s.append(card2)
			p2_s.extend(p2.getHand()[:3])
			p2.hand = p2.getHand()[3:]
			p2.hand.insert(0,p2_s.pop())
			wars+=1


		round+=1
		print('P1: %d --- P2: %d' % (p1.getHandLength(), p2.getHandLength()))
		p1_s1 = []
		p2_s1 = []
		for x in p1_s:
			p1_s1.append(str(x))
		for x in p2_s:
			p2_s1.append(str(x))
		print('P1_s: ' + str(p1_s1))
		print(p1.getHandString())
		print('P2_s: ' + str(p2_s1))
		print(p2.getHandString())
		# input()
	gameTime = time.time() - startTime
	print('PLAYER 2 WINS') if p1.getHandLength() == 0 else print('PLAYER 1 WINS')
	print('Time Elapsed: ' + str(gameTime))

simpleWar()