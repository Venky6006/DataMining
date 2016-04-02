import copy;
from Apriory import Apriori;
from Utility import Utility;
import numpy as np;
from time import time;
from math import log;

class RandomizedApriori(object):

	def __init__(self,transactionFile,minimumSupport,numberOfHashFunctions,tolerance,error):

		self.transactionFile = transactionFile;
		self.numberOfHashFunctions = numberOfHashFunctions;
		self.minimumSupport = minimumSupport;
		self.tolerance = tolerance;
		self.error = error;

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
	def random(self,low,high,length):

		a =[];
		b =[];

		a  = (np.random.randint(low,high,length));
		b  = (np.random.randint(low,high,length));

		return a,b;

# ------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

	def randomizedApriori(self):

		apriori = Apriori(self.transactionFile,self.minimumSupport);
		utility = Utility(self.transactionFile,self.minimumSupport);

		candidates,T = apriori.C1List();
		
		frequentItemSet = {};
		k=1;

		list = apriori.itemsetWithMinimumSupport(candidates);
		
		if list:
			frequentItemSet[k] = list;

		onezero = {};
		indexes = {};

		d=0;
		
		while list:

			if k==1:
				
				onezero,d = utility.convert(list,apriori);
				
			else:

				onezero = utility.combineConvert(onezero,indexes);
				
			k = k+1;			
			m = utility.mValue(onezero);			
						
			pqonezero = utility.pqTrasform(onezero,m,d);			
			qponezero = utility.qpTransform(onezero,m,d);

			# print "old support : ",self.minimumSupport;
			alpha = float(m)/T ;	
			omega = ( (1-self.tolerance)*self.minimumSupport )/(2*alpha-(1-self.tolerance)*self.minimumSupport);
			# print "omega value : ",omega;
			epsolon = ( (alpha)*self.tolerance ) /( alpha +(alpha -self.minimumSupport)*(1-self.tolerance) );
			# print "epsolon value :",epsolon;
			deltaInverse = int(1/self.error);
			# print "delta inverse is : ",deltaInverse;

			# numberOfHashFunctions = int( (2/(omega*epsolon*epsolon))*log(deltaInverse) );
			support = ( ( 1-epsolon )*self.minimumSupport)/(2*alpha - self.minimumSupport);			
			
			# print "new support is :",support;			
			# print "number of hashfunctions : ",numberOfHashFunctions;

			prime = 9887;
			a,b = self.random(0,prime,self.numberOfHashFunctions);			
			# if m < self.numberOfHashFunctions:
			# 	self.numberOfHashFunctions =m;

			pSignature = utility.minHashSignature(list,pqonezero,a,b,prime,m,d,self.numberOfHashFunctions);
			qSignature = utility.minHashSignature(list,qponezero,a,b,prime,m,d,self.numberOfHashFunctions);
						

			candidates,indexes = utility.generate(pSignature,qSignature,k,support);
				
			del pSignature,qSignature;
			
			list,indexes = utility.itemsetWithMinimumSupport(candidates,indexes,apriori);
			
			frequentItemSet[k] = list;			
			

		
		return frequentItemSet;


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

