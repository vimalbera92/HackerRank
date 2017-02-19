'''
Created on Feb 8, 2017

@author: vbera
'''
def maxProfit(priceList, maxPriceIndex):
    profit = 0
    for i in range(0, maxPriceIndex):
        profit += priceList[maxPriceIndex] - priceList[i]
    return profit

def getMaxIndex(priceList):
    maxPrice = 0
    maxPriceIndex = 0
    i = 0
    for price in priceList:
        prices[i] = int(price)
        if maxPrice < prices[i]:
            maxPrice = prices[i]
            maxPriceIndex = i
        i += 1
    return maxPriceIndex

testcases = int(input().strip())
while testcases > 0:
    days = int(input().strip())
    prices = [int(price) for price in input().strip().split(" ")]
    profit = 0
    while len(prices) > 0:
        maxPriceIndex = getMaxIndex(prices)
        profit += maxProfit(prices[0:maxPriceIndex + 1], maxPriceIndex)
        prices = prices[maxPriceIndex + 1:]
    print(profit)
    testcases -= 1
