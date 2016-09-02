from Bio import SeqIO # Biopython is great for parsing sequence files. Import the part we need (SeqIO).

input = open('original subsample extraction for E1 Gene.fasta copy', 'r') # Open your sequence file in read mode ('r'). Put the script.py and the input.fasta in the same directory.
output = open('extraction E1 fixed year.fasta', 'w') # Open a file in write mode ('w') to put the output.

seq_list = []
for entry in SeqIO.parse(input, 'fasta'): # Parse each sequence in the input file; tell biopython to expect fasta format.
	seqlist.append(entry) # Add this sequence object to our list

for entry in seqlist: # Each sequence object has some attributes stored that we want to access. 	
	header = entry.description  # This is an instance of `object.attribute` syntax; it will pull the sequence object, and look for the header attached to it
	sequence = str(entry.seq) # Pull the sequence information; another instance of `object.attribute` 
	header = header.split('|') # accessionNumber|blah|blah|...|country|year --> [ accessionNumber, blah, blah, ..., country, year]
	year = data[-1] # need to look just for year, not month or day 
	if year != "NA": # isolate the year from year_month_day format given
		new_year = year.split('_')
		year = int(new_year[0])
	for metadata in header:
		header = metadata + "|"
    #new_header = header + "|" + year         
	output.write('>'+header+'\n'+sequence+'\n') # '\n' inserts a new line 

for entry in seq_list:
    SeqIO.write(entry, output, 'fasta')