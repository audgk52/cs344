'''
This program takes in the sample text and test if it is a spam or not based on the data from
hash tables of words from spam corpus and non-spam corpus & calculated probability for each word being spam
'''


def Hash(spam_corpus, ham_corpus):
    spam = {}  # key as token; value as the number of occurence
    not_spam = {}
    token = []
    ngood = 0
    nbad = 0

    # 1st hash table for spam
    for msg in spam_corpus:
        nbad += 1
        for wd in msg:
            if wd in spam:
                spam[wd] += 1
            else:
                spam[wd] = 1
            if wd not in token:
                token.append(wd)

    # 2nd hash table for not_spam
    for msg in ham_corpus:
        ngood += 1
        for wd in msg:
            if wd in not_spam:
                not_spam[wd] += 1
            else:
                not_spam[wd] = 1
            if wd not in token:
                token.append(wd)

    # 3rd hash table - probability
    prob = {}
    for wd in token:
        if wd in not_spam:
            g = 2 * not_spam[wd]
        else:
            g = 0
        if wd in spam:
            b = spam[wd]
        else:
            b = 0
        if g + b > 1:
            prob[wd] = max(0.01, min(0.99, min(1.0, b/nbad) / (min(1.0, g/ngood) + min(1.0, b/nbad))))
        else:
            prob[wd] = 0
    return prob

def SpamCheck(text, filt):
    product = 1
    comp_product = 1

    for wd in text:
        if wd in filt:
            product *= filt[wd]
            comp_product *= 1 - filt[wd]
        elif wd not in filt:
            filt[wd] = 0.4
    marginal = product + comp_product
    Bayes = product / marginal
    if Bayes > 0.9:
        return True
    else:
        return False

# Hard-coded SPAM/HAM corpus

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

sample_text = ["I", "am", "spam", "yes", "i", "am"]

spam_filter = Hash(spam_corpus, ham_corpus)
if SpamCheck(sample_text, spam_filter):
    print("Spam")
else:
    print("Not spam")
























