#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 08:37:25 2020

@author: mac
"""

import unittest
import hw5_card_ec1.py


class TestCard(unittest.TestCase):

    def test_init_card(self):
        c1 = hw5_card_ec1.Card(2,10)
        c2 = hw5_card_ec1.Card(0,13)
        init_cards=[]
        init_cards = init_cards.append(c1)
        init_cards = init_cards.append(c2)
    
        self.assertIsInstance(init_cards, list)
        
    def testAddAndRemove(self):
        c1 = hw5_card_ec1.Card(2,10)
        c2 = hw5_card_ec1.Card(0,13)
        c3 = hw5_card_ec1.Card(1,5)
        init_cards=[]
        init_cards = init_cards.append(c1)
        init_cards = init_cards.append(c2)
        
        t1 = hw5_card_ec1.Hand(init_cards)
        t1_add = t1.add_card(c3)
        t1_remove = t1_add.remove_card(c3)
        
        self.assertNotEqual(len(t1_add), len(t1_remove))
        
    def testDraw(self):
        deck1 = hw5_card_ec1.Deck()
        deck_card = deck1.cards
        deck_copy = deck_card.copy()
        c1 = hw5_card_ec1.Card(2,10)
        c2 = hw5_card_ec1.Card(0,13)
        init_cards=[]
        init_cards = init_cards.append(c1)
        init_cards = init_cards.append(c2)
        
        init_card_draw = init_cards.draw(deck_copy)
        
        self.assertEqual(len(init_cards), len(init_card_draw))
        self.assertEqual(len(deck_card), len(deck_copy))
        
        
        
        
        
