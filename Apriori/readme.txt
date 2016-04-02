# DataMining

This folder contains the following files:

			1.Apriory.py
			
Apiory Alogrithm:

		1.Contains the implementation of standard Apriori Algorithm.
		2.First it generate all frequent items(whose support is greater than given threshold) of size one(k=1) using C1List() and 			     itemWithMinimumSupport().
		3.From next level onwards it follows below two steps:
			
				1.Generate candidates of size (k+1) from itemsets of size k using candidateGenerator() function.
				2.For every item in candidates check its support and if its support is greater than the threshold add this element using 					  itemWithMinimumSupport() function.
				
		4.Stop this procedure if the itemset is empty set.
	


	

