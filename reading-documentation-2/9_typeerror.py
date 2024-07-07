tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)    # TypeError was because tweet is string where 5 is int and 
                                    # they cannot be concatenated
                # len(tweet) + 5
