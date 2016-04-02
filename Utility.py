
class Utility(object):

	
	def __init__(self,transactionFile,minimumSupport):

		self.transactionFile = transactionFile;
		# self.numberOfHashFunctions = numberOfHashFunctions;
		self.minimumSupport = minimumSupport;

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

	def mValue(self,matrix):

		m=0;

		for key in matrix:

			length = len(matrix[key]);
			if(m < length):

				m = length;

		return m;

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

	def convert(self,list,apriori):

		
		transactions = apriori.readData();

		onezero = {};
		transactionid =0;
		
		for eachtrasaction in transactions:

				
			for item in list:

				if item.issubset(eachtrasaction):

					temp = frozenset(item);
					if temp in onezero:

						onezero[temp].append(transactionid);
					else:
						onezero[temp] = [];
						onezero[temp].append(transactionid);

			transactionid = transactionid +1;
			
		return onezero,(transactionid);


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

	def pqTrasform(self,onezero,m,d):

		# print "i am in pqTrasform";
		for key in onezero:

			length = len(onezero[key]);
			onepadding = m-length;

			for i in range(length):

				yield onezero[key][i];

			for j in range(onepadding):

				yield (d+j);

			yield -1;

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

	def qpTransform(self,onezero,m,d):

		
		for key in onezero:

			length = len(onezero[key]);

			onepadding = m-length;
			dimension = d+m;

			for i in range(length):

				yield onezero[key][i];

			for j in range(onepadding):

				yield (dimension+j);

			yield -1;

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

	def minHashSignature(self,list,generator,a,b,prime,m,d,numberOfHashFunctions):

		# print "i am minHashSignature";

		signature ={};

		size = (d+2*m);
		count =0;
		flag =0;

		if list:
			key = frozenset(list[count]);
		length=len(list);

		# print (key);
		while True:

			try:

				id = next(generator);
				
				if (id != -1):
					# print (id);
					if flag ==0:

						flag =1;
						for j in range(numberOfHashFunctions):

							hash = ((a[j]* id + b[j])%prime)%size;

							if key in signature:

								signature[key].append(hash);

							else:

								signature[key] = [];
								signature[key].append(hash);
					else:

						for j in range(numberOfHashFunctions):

							hash = ((a[j]* id + b[j])%prime)%size;

							if signature[key][j] > hash:

								signature[key][j] = hash;


				else:

					count =count + 1;
					flag =0;
					if count < length:
						key = frozenset(list[count]);
						# print (key);

			except StopIteration:

				return signature;

# ----------------------------------------------------------------------------------
# shuffle all non zeros using some hash function .while suffling pick some random 
# float value from (0,1) if it is greater than 0.5 and the signature size is less than
# required insert this value else pass. 
# -----------------------------------------------------------------------------------

	# def minHashSignature(self,list,generator,a,b,prime,m,d,numberOfHashFunctions):

	# 	signature ={};

	# 	size = (d+2*m);
	# 	count =0;
	# 	flag =0;

	# 	if list:
	# 		key = frozenset(list[count]);
	# 	length=len(list);

	# 	while  True:

	# 		try:

	# 			id = next(generator);

	# 			if (id != -1):

	# 				if flag ==0:

	# 					flag=1;

	# 					signature[key] = [];
	# 					hash = ((a[0]* id + b[0])%prime)%size;
						
	# 					signature[key].append(hash);




	# 			else:

	# 				count =count + 1;
	# 				flag =0;
	# 				if count < length:
	# 					key = frozenset(list[count]);
	# 					# print (key);

	# 		except StopIteration:
	# 			return signature;
			

# ---------------------------------------------------------------------------------------
# ---------------minHash- signature using one permutation and rotation--------------------
# ---------------------------------------------------------------------------------------

	# def minHashSignature(self,list,generator,a,b,prime,m,d,numberOfHashFunctions):

	# 	size = (2*m+d);
	# 	binsize = size/numberOfHashFunctions+1;
	# 	signature ={};

	# 	count =0;
	# 	flag =0;

	# 	if list:

	# 		key = frozenset(list[count]);

	# 	length=len(list);

	# 	while True:

	# 		try:

	# 			id = next(generator);

	# 			if(id != -1):

	# 				if flag ==0:

	# 					# k = key[count];
	# 					signature[key] = [];

	# 					for j in range(numberOfHashFunctions):

	# 						signature[key].append(-1);

	# 					flag =1;

	# 					hash = ((a[0]* id + b[0]))%size;

	# 					binid = hash/binsize;
	# 					positionInsideBin = hash%binsize;



	# 					if signature[key][binid] == -1:

	# 						signature[key][binid] =positionInsideBin;

	# 					else :

	# 						signature[key][binid] =positionInsideBin;

	# 				else:

						

	# 					hash = ((a[0]* id + b[0])%prime)%size;
	# 					binid = hash/binsize;
	# 					positionInsideBin = hash%binsize;

						
	# 					if signature[key][binid] == -1:

	# 						signature[key][binid] =positionInsideBin;

	# 					elif signature[key][binid] > positionInsideBin:

	# 						signature[key][binid] =positionInsideBin;
							

	# 			else:
	# 				count =count + 1;
	# 				flag =0;
	# 				if count < length:
	# 					key = frozenset(list[count]);
	# 					# print (key);

	# 		except StopIteration:

	# 			c = binsize+1;

	# 			for key in signature:

	# 				temp = signature[key];
	# 				nonzeros = [];
	# 				zeros=[];

	# 				for i in range(len(temp)):

	# 					if temp[i] == -1:

	# 						zeros.append(i);
	# 					else:
	# 						nonzeros.append(i);

	# 				if zeros:

	# 					for i in zeros:

	# 						flag =0;

	# 						for j in nonzeros:

	# 							if  i < j:

	# 								temp[i] = temp[j] + (j-i)*c;
	# 								flag =1;
	# 								break;

	# 						if flag ==0:

	# 							for j in nonzeros:

	# 								if j < i :

	# 									temp[i] = temp[j] + (numberOfHashFunctions-i+j)*c;
	# 									break;

	# 			return signature;


# -------------------------------------------------------------------------------------------------
# ------------------------Conditional Random Sampling(take top k min hash values as signature )------
# very bad results .it is losing almost 1/3rd of keys at every level.The results are fluctuating
# some times it is running for small number of levels and other times it is running higher levels
# by losing more number of keys more than 1/3rd.
# ------------------------------------------------------------------------------------------

	# def minHashSignature(self,list,generator,a,b,prime,m,d,numberOfHashFunctions):

	# 	signature ={};

	# 	size = (d+2*m);
	# 	count =0;
	# 	flag =0;
	# 	sort =0;

	# 	if list:
	# 		key = frozenset(list[count]);
	# 	length=len(list);

	# 	while True:

	# 		try:

	# 			id = next(generator);

	# 			if(id != -1):

	# 				if flag ==0:

	# 					flag =1;

	# 					hash = ((a[0]* id + b[0])%prime)%size;

	# 					signature[key] = [];
	# 					signature[key].append(hash);

	# 				else:

	# 					hash = ((a[0]* id + b[0])%prime)%size;

	# 					if len(signature[key]) <self.numberOfHashFunctions:

	# 						signature[key].append(hash);

	# 					elif  sort ==0:

	# 						signature[key].sort();
	# 						sort =1;

	# 						temp =[];
	# 						index =0;

	# 						for j in signature[key]:

	# 							if j <=hash:

	# 								index +=1;
	# 							else:
	# 								break;

	# 						if index < self.numberOfHashFunctions:
								
	# 							for j in range(0,index):

	# 								temp.append(signature[key][j]);
	# 							temp.append(hash);

	# 							for j in range(index,self.numberOfHashFunctions-1):
	# 								temp.append(signature[key][j]);

	# 							signature[key] = temp;

	# 					else:

	# 						temp =[];
	# 						index =0;

	# 						for j in signature[key]:

	# 							if j <=hash:

	# 								index +=1;
	# 							else:
	# 								break;

	# 						if index < self.numberOfHashFunctions:
								
	# 							for j in range(0,index):

	# 								temp.append(signature[key][j]);
	# 							temp.append(hash);

	# 							for j in range(index,self.numberOfHashFunctions-1):

	# 								temp.append(signature[key][j]);

	# 							signature[key] = temp;


	# 			else:

	# 				count =count + 1;
	# 				flag =0;
	# 				sort =0;
	# 				# sort = False;
	# 				if count < length:
	# 					key = frozenset(list[count]);
						

	# 		except StopIteration:

	# 			return signature;



# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

	def generate(self,psignature,qsignature,k,support):

		# print "i am in generate function";
		list=[];
		indexes = {};
		# length = p
		# length = self.numberOfHashFunctions;

		qkeys = qsignature.keys();
		pkeys = psignature.keys();
		size = len(qkeys);

		for q in range(size):		

			qtemp = qsignature[qkeys[q]];
			length = len(qtemp);

			for p in range(q+1,size):

				count =0;
				ptemp = psignature[pkeys[p]];				

				for j in range(length):

					if ptemp[j] == qtemp[j]:

						count +=1;

				itemSupport = float(count) / length;

				if (itemSupport >= support ):

					union = qkeys[q].union(pkeys[p]);
					if len(union) == k and union not in list:

						list.append(union);
						indexes[union] = [qkeys[q],pkeys[p]];

		return list,indexes;
# -------------------------------------------------------------------------
# --------------------------------------Using banding----------------------
# -------------------------------------------------------------------------
	
	# def generate(self,psignature,qsignature,k):

	# 	candidateList =[];
	# 	indexes = {};
	# 	length = self.numberOfHashFunctions;

	# 	bandsize = int(self.minimumSupport*length);		
	# 	if bandsize != 0:
	# 		bands = int(length/bandsize);
	# 	else:
	# 		bandsize = 1;
	# 		bands = int(length/bandsize);

	# 	qkeys = qsignature.keys();
	# 	pkeys = psignature.keys();

	# 	listOfDic=[];

	# 	for band in range(bands):

	# 		dic ={};

	# 		for index in range(len(pkeys)):

	# 			temp = psignature[pkeys[index]];
	# 			sum =0;
	# 			for i in range(bandsize):

	# 				sum += temp[band*bandsize+i];

	# 			if sum in dic:
	# 				dic[sum].append(index);
	# 			else:
	# 				dic[sum] =[];
	# 				dic[sum].append(index);

	# 		listOfDic.append(dic);

	# 	for index in range(len(qkeys)):

	# 		for band in range(bands):

	# 			temp = qsignature[qkeys[index]];
	# 			sum = 0

	# 			for i in range(bandsize):

	# 				sum += temp[(band*bandsize) +i];

	# 			if sum in listOfDic[band]:

	# 				list = listOfDic[band][sum];

	# 				for item in list:

	# 					union = qkeys[index].union(pkeys[item]);
	# 					if len(union) ==k and union not in candidateList:
	# 						candidateList.append(union);
	# 						indexes[union] = [qkeys[index],pkeys[item]];

	# 	return candidateList,indexes;

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

	# def itemsetWithMinimumSupport(self,candidates,indexes,apriori):

	# 	# print "I am in itemsetWithMinimumSupport";

	# 	transactions = apriori.readData();

	# 	supportDictionary ={};
	# 	size = len(transactions);

	# 	for eachtrasaction in transactions:

	# 		for item in candidates:

	# 			if item.issubset(eachtrasaction):

	# 				temp = frozenset(item);
	# 				if temp in supportDictionary:
	# 					supportDictionary[temp] += 1;
	# 				else:
	# 					supportDictionary[temp] = 1;

	# 	prunedItemSet = [];
	# 	prunedIndex = {};

	# 	for key in supportDictionary:

	# 		itemSupport = float(supportDictionary[key])/size;
			
	# 		if itemSupport >= self.minimumSupport:
	# 			prunedItemSet.append(set(key));
	# 			prunedIndex[key] = indexes[key];
	
	# 	return prunedItemSet,prunedIndex;

# ----------------------------------------------------------------------------------
# do this for every item set in the candidate pair:read whole transactions and
# check the number of transactions support this itemset.
# ----------------------------------------------------------------------------------

	def itemsetWithMinimumSupport(self,candidates,indexes,apriori):

		prunedItemSet = [];
		prunedIndex = {};

		for item in candidates:

			transactions = apriori.readData();

			T  = len(transactions);
			count =0;

			for transaction in transactions:

				if item.issubset(transaction):
					count +=1;

			itemSupport = float(count)/T;

			if itemSupport >=self.minimumSupport:

				prunedItemSet.append(set(item));
				prunedIndex[frozenset(item)] = indexes[frozenset(item)];

		return prunedItemSet,prunedIndex;
				


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

	def combineConvert(self,onezero,indexes):
				
		newonezero = {};

		for itemset in indexes:

			list = indexes[itemset];
			temp =set();

			for index in list:

				if not temp:

					temp = set(onezero[index]);
				else:

					temp = temp.intersection(set(onezero[index]));

			newonezero[itemset] = [item for item in temp];

		return newonezero;

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------