from Apriory import Apriori
from RandomizedApriori import RandomizedApriori
from time import time

def simulation():

	f = open("LshResult.csv",'w');
	f.write("support"+","+"hashfunctions"+","+"time"+","+"keys");
	f.write("\n");
	f.flush();


	# for support in range(30,5,-5):

	# 	# print "i am inside loop";
		# tolerance=0.1
		# error=0.1;
	# 	r = RandomizedApriori("soybeandata.txt",float(support)/100,tolerance,error);

	# 	start = time();
	# 	list = r.randomizedApriori();
	# 	end = time();
	# 	totalkeys =0;

	# 	for key in list:

	# 		totalkeys +=len(list[key]);


	# 	f.write(str(support)+","+str(round(end-start,2))+","+str(totalkeys));
	# 	f.write("\n");
	# 	f.flush();

	for support in [1,0.8,0.6,0.4,0.2,0.1]:

		for numberofhashfunctions in [10,15,25,50,75,100,150,200]:

			tolerance=0.1
			error=0.1;
			r = RandomizedApriori("soybeandata.txt",float(support)/100,numberofhashfunctions,tolerance,error);

			start = time();
			list = r.randomizedApriori();
			end = time();
			totalkeys =0;

			for key in list:

				totalkeys +=len(list[key]);


			f.write(str(support)+","+str(numberofhashfunctions)+","+str(round(end-start,2))+","+str(totalkeys));
			f.write("\n");
			f.flush();


simulation();
