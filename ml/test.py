# input command
#
# choices commands under device in command
#
# wordslist
# all words have a value
# verb and nouns
#
################################
# verbs with similiar processes are grouped
# k means
# words and their meanings
#
# however having a one to many relationship would be counterproductive
# so how?
# words and their meaning value
# 1
# phrases and words relationship to the value
# ex. (turnon),(on),(power on)
# (playfull),("energetic")
# this allows us to use pattern rec along with clustering methods moving forward


####### mongodb  ########
# id
# synonyms []
#
# what we hope to get from clustering these are their euclydian values
# with these values will be a feature for decsion tree
# most likley will have the highest correlation




#########
# decision tree regression
# prediction action(command)
#
# features
#     verb ord
#     verbs k value




def WordToOrd(word):
    word_ord = []
    for letter in word:
        word_ord.append(ord(letter))
    return word_ord



#############################################################

# data collection

# verb ord
# action
# state





