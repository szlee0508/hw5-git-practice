##### Name:Szu-Pei Lee
########## Uniqname:szlee
##############################################




import unittest
import hw5_cards
import random

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q1 = hw5_cards.Card(2, 12)
        
        self.assertEqual(q1.rank_name, 'Queen')
        self.assertNotEqual(q1.rank_name, 'King')
        self.assertIsInstance(q1.rank_name, str)
        self.assertTrue(q1.rank_name == 'Queen')
        self.assertFalse(q1.rank_name != 'Queen')
        self.assertIs(q1.rank_name, 'Queen')
        self.assertIsNot(q1.rank_name, 'Jack')
        self.assertIsNot(q1.rank_name, 10)
        
        return q1.rank_name, 'Queen'
    
    def test_q2(self):
        '''
        1. fill in your test method for question 2:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q2 = hw5_cards.Card(1, 10)
        
        self.assertEqual(q2.suit, 1)
        self.assertEqual(q2.suit_name, 'Clubs')
        self.assertNotEqual(q2.suit, 12)
        self.assertTrue(q2.suit == 1)
        self.assertIsInstance(q2.suit, int)
        self.assertIsInstance(q2.suit_name, str)
        self.assertIs(q2.suit, 1)
        self.assertIs(q2.suit_name,'Clubs')
        self.assertIsNot(q2.suit, 4)
            
        
        return q2.suit_name, 'Clubs'    
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q3 = hw5_cards.Card(3, 13)
        q3_word = q3.__str__()
        
        self.assertEqual(q3_word, 'King of Spades')
        self.assertNotEqual(q3_word, 'King of Clubs')
        self.assertIsNot(q3_word, int)
        self.assertIsInstance(q3_word, str)
        self.assertTrue(q3_word == 'King of Spades')
        self.assertIsNot(q3_word, 1)
        self.assertFalse(q3_word != 'King of Spades')
        self.assertTrue(q3_word != 'Queen of Diamonds')
        
        return q3_word, 'King of Spades' 

    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q4 = hw5_cards.Deck()
        q4_cards = q4.cards
        
        self.assertEqual(len(q4_cards), 52)
        self.assertNotEqual(len(q4_cards), 50)
        self.assertIsInstance(len(q4_cards), int)
        self.assertIsNot(len(q4_cards), list)
        self.assertNotEqual(len(q4_cards), 53)
        self.assertTrue(len(q4_cards) == 52)
        self.assertTrue(len(q4_cards) != 50)
        self.assertFalse(len(q4_cards) == 48)
        
        return len(q4_cards), 52  

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q5 = hw5_cards.Deck()
        q5_pop = q5.deal_card()
        type(q5_pop)
        
        self.assertIsInstance(q5_pop, hw5_cards.Card )
        #self.assertNotEqual(q5_pop, hw5_cards.Card)
        #self.assertTrue(q5_pop == hw5_cards.Card)
        
        return q5_pop, hw5_cards.Card
   
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q6 = hw5_cards.Deck()
        q6_cards = q6.cards.copy() #list可以算len
        q6.deal_card()
        nq6_cards = q6.cards
        
        self.assertEqual(len(q6_cards)-1,len(nq6_cards))
        self.assertNotEqual(len(q6_cards), len(nq6_cards))
        self.assertTrue(len(q6_cards) != len(nq6_cards))
        self.assertFalse(len(q6_cards) == len(nq6_cards))
        self.assertEqual(len(q6_cards)-1 , len(nq6_cards))
        self.assertNotEqual(len(q6_cards), len(nq6_cards))
        
        return len(q6_cards)-1, len(nq6_cards)   


    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q7 = hw5_cards.Deck()
        temp1 = q7.cards.copy()
        q7_pop = q7.deal_card()
        temp2 = q7.cards.copy()
        q7.replace_card(q7_pop)
        #print("pop cards : " + str(q7_pop))
        #print("now cards : " + str(len(q7.cards)))
        #print("per cards : " + str(len(temp)))
        self.assertEqual(len(q7.cards), len(temp1), len(temp2))
        return 52, 52, 52
        #return len(q7.cards), len(temp1), len(temp2)
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        q8 = hw5_cards.Deck()
        randomNumber = random.randint(1,len(q8.cards))
        new_card = q8.cards[randomNumber]
        temp = q8.cards.copy()
        q8.replace_card(new_card)
        #print("pop cards : " + str(new_card))
        #print("pre cards : " + str(len(temp)))
        #print("now cards : " + str(len(q8.cards)))
        
        self.assertEqual(len(q8.cards), len(temp))
        
        return len(q8.cards), len(temp)
        #return X, Y  



if __name__=="__main__":
    unittest.main()