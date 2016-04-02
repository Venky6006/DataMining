
class Apriori(object):


	def __init__(self,trasactionFile,minimumSupport):

		self.trasactionFile = trasactionFile;
		self.minimumSupport = minimumSupport;

# --------------------------------------------------------------------------------------
# Reads transactional data from the file and returns the transactions as set of integers
# --------------------------------------------------------------------------------------

	def readData(self):

		data = open(self.trasactionFile,'r');
		transactions = [];

		for line in data:

			temp = set(map(int,line.split()));
			transactions.append(temp);

		return transactions;


# -----------------------------------------------------------------------------------------
# It returns list of items that present in the store (all items from the transactional file 
# -----------------------------------------------------------------------------------------


	def C1List(self):

		transactions = self.readData();
		listOfOneItemset = [];

		for eachTransaction in transactions:

			for item in eachTransaction:

				temp = set([item]);

				if temp not in listOfOneItemset:
					listOfOneItemset.append(temp);

		print "c1 list is generated----with length ",len(listOfOneItemset);
		return (listOfOneItemset);

# -----------------------------------------------------------------------------------------------
# For given itemset it calculates the support by checking whether the itemset is part of the
# transaction ,reading whole trascations one by one from the file. 
# 
# -----------------------------------------------------------------------------------------------

	def itemsetWithMinimumSupport(self,itemSet):

		transactions = self.readData();
		size = len(transactions);

		supportDictionary ={};

		for eachTransaction in transactions:

			for item in itemSet:
				if item.issubset(eachTransaction):

					temp = frozenset(item);
					if temp in supportDictionary:
						supportDictionary[temp] += 1;
					else:
						supportDictionary[temp] = 0;
						supportDictionary[temp] += 1;
		prunedItemSet = [];
	
		for key in supportDictionary:

			itemSupport = float(supportDictionary[key])/size;
			# print "key value  :" ,key,"support value---: ",itemSupport;
			if itemSupport >= self.minimumSupport:
				prunedItemSet.append(set(key));
	# print "Pruned Itemset is ---";
	# print prunedItemSet;
		return prunedItemSet;

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


	def candidateGenerator(self,items,length):

		track = len(items);
		# print "size of the of the join is ---",(track*track);
		candidates = [];
		#print "items size is : ",len(items);

		for left in items:
			for right in items:

				temp = left.union(right);
				if((len(temp) == length )and (temp not in candidates)):

					candidates.append(temp);
		#print "Candidate list size : ", len(candidates);
		# print "Generated itemset of length----",length;
		return candidates;

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

	def apriori(self):

		one_ItemSet = self.C1List();
		frequentItemset = {};
		k = 1;
		list = self.itemsetWithMinimumSupport(one_ItemSet);
		
		# print "added item sets of legth ",k," to dictionary";
	
		while  k <=4 and list:

			frequentItemset[k] = list;
			k = k+1;
			candidates = self.candidateGenerator(list,k);
			list = self.itemsetWithMinimumSupport(candidates);
			
		return frequentItemset;
