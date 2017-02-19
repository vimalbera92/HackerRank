import sys
import operator

words = input().strip().split(" ")
n = int(input().strip())
sortedhotel = {}
while n > 0:
    hotelId = int(input().strip())
    reviewsCount = sortedhotel.get(hotelId)
    if reviewsCount == None:
        reviewsCount = 0
    review = input()
    for word in words:
        reviewsCount += review.count(word)
    sortedhotel[hotelId] = reviewsCount
    n -= 1
sortedList = sorted(sortedhotel.items(), key=operator.itemgetter(1), reverse=True)
for record in sortedList:
    sys.stdout.write(str(record[0]) + " ")
