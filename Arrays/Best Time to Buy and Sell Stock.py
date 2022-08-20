# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:23:24 2022

@author: ADARSH
"""
#the buy and sell of stock only once
def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        maxprofit=0
        left=0
        right=1
        
        while right<n :
            cprofit=prices[right]-prices[left]
            if(prices[left]<=prices[right]):
                
                maxprofit=max(maxprofit,cprofit)
                
            else:
                
                left=right
            right+=1
                    
                    
        return maxprofit   
    
    
    