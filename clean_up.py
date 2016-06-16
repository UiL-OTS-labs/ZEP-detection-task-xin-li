#!/usr/bin/python
# Cleans up the experiment data from a previous version where missed trials in one block are 
#faultely replayed in subsequent blocks.

import csv,os,sys

 
# Get the total number of args passed to the demo.py
total = len(sys.argv)
if total <= 1:
	print "Usage: %s <FILENAME>"%(sys.argv[0])
	exit()

filename = sys.argv[1]
new_filename = 'corrected_'+filename

def __main__():
	headers = []
	print "Reading: ",filename
	with open(filename,'rU') as csvfile:
		reader = csv.reader(csvfile)
		headers = reader.next()

	print "Writing: ",new_filename
	with open(new_filename,'w') as outputfile:
		writer = csv.DictWriter(outputfile,headers)
		with open(filename,'rU') as csvfile:
			writer.writeheader()
			previous_rows = []
			reader = csv.DictReader(csvfile)
			for row in reader:
				if allowed(row, previous_rows):
					previous_rows.append(row)
					writer.writerow(row)

def allowed(current_row, previous_rows):
	if len(previous_rows) == 0:
		return True
	for previous_row in reversed(previous_rows):
		if rows_are_comparable(current_row, previous_row):
			if is_a_repeat(previous_row, previous_rows):
				return False
			if is_missing_response(previous_row):
				return True
	return True

def rows_are_comparable(row1, row2):
	result = \
	row1['ppid'] == row2['ppid'] \
	and row1['block'] == row2['block'] \
	and row1['id'] == row2['id'] \
	and row1['sesid'] == row2['sesid']
	return result

def is_missing_response(row):
	return row['correctness'] == '0'

def is_a_repeat(row, previous_rows):
	for previous_row in reversed(previous_rows):
		if rows_are_comparable(row, previous_row) and is_missing_response(row):
			return False
	return True

print 'STARTING'
__main__()
print 'FINISHED'