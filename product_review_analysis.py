#task12



def tally_words(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    positive_tally = 0
    negative_tally = 0
    
    for review in reviews:
        review = review.lower()
        positive_tally += sum(review.count(word)for word in positive_words)
        negative_tally += sum(review.count(word)for word in negative_words)
    return positive_tally, negative_tally
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
]
keywords = ["excellent", "good", "average", "poor", "bad"]

    
    
for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())
    print(review)

positive_tally, negative_tally = tally_words(reviews)

print(f"This is the amount of positive words in the reviews: {positive_tally} and this is the amount of negative words in the reviews: {negative_tally}")
#task3
def summarize(review, length=30):
    if len(review) <= length:
        return review
    
    words = review.split()
    summary = []
    char_count = 0
    
    for word in words:
        if char_count + len(word) + len(summary) > length:
            break
        summary.append(word)
        char_count += len(word)
    
    return " ".join(summary) + "…"

for review in reviews:
    print(summarize(review))

 




    

    