#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: create.py
# Description: Generate images latex for all images defined by 'files' below
# Run: python create.py > images.tex
# Date: January 2016
# Author: Richard Hill http://retu.be

import glob
import os,sys
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Get all images (.JPG and .jpg in this example)
files = glob.glob("photos.cmyk/*.JPG")
files.extend(glob.glob("photos.cmyk/*.jpg"))

#files = files[0:22]

# Returns value of specified exif field.
def get_exif_value(exif, field) :
	for (k,v) in exif.iteritems():
		if TAGS.get(k) == field:
        		return v

def get_comparator(filepath):
	return filepath

def get_exif_data(filepath):
	return Image.open(filepath)._getexif();

def get_timestamp(exif):
	dt = get_exif_value(exif,"DateTimeOriginal")	
	return datetime.strptime(dt, '%Y:%m:%d %H:%M:%S')

# Gets name of image from full path. Escapes underscores for latex. 
def get_filename(filepath):
	return (os.path.basename(filepath)).replace("_","\_");

def get_name(filepath):
	return (os.path.basename(filepath)).split(" - ")[1].replace(".jpg", "").replace(".JPG", "").replace("_","\_");

# Prints the latex for each image. Images have a black border and caption
# detailing the file name and date taken (as determined by exif data)
def get_latex(filepath):

#	exif = get_exif_data(filepath)
#	do = get_timestamp(exif)
	print '\\vspace*{\stretch{1}}\n'
	print '\\begin{figure}[ht!]'
	print '\\centering'
	print "{\n"
	print "\\setlength{\\fboxsep}{0pt}%"
	print "\\setlength{\\fboxrule}{2pt}%"
	print "\\fbox{\\includegraphics[height=16cm,width=16cm,keepaspectratio]{" + filepath + "}}\n"
	print "}%"	
#	print '\\caption{' + '\\texttt{[' + get_filename(filepath) + ']}' + ' ' + do.strftime('%d') + ' ' + do.strftime('%B') + ' ' + do.strftime('%Y') + '}'
	print '\\caption{' + get_name(filepath) + '}'
	print '\\end{figure}\n'
#	print get_name(filepath) + '\n'
	print '\\vspace{\stretch{1}}\n'

def old_get_latex(filepath):
#	print '\\vskip 3cm'
	print '\\begin{figure}[ht!]'
	print '\\centering'
	print "{%"
	print "\\setlength{\\fboxsep}{0pt}%"
	print "\\setlength{\\fboxrule}{2pt}%"
	print "\\fbox{\\includegraphics[height=17.5cm,width=17.5cm,keepaspectratio]{" + filepath + "}}%"
	print "}%"	
#	print '\\caption{' + '\\texttt{[' + get_filename(filepath) + ']}' + ' ' + do.strftime('%d') + ' ' + do.strftime('%B') + ' ' + do.strftime('%Y') + '}'
	print '\\caption{' + get_name(filepath) + '}'
	print '\\end{figure}\n'
	return;

# Sort the images chronologically
files = sorted(files, key=get_comparator)

# Loop over images and print latex for each
count = 0
for filepath in files:
	count = count + 1
	get_latex(filepath)
	print "\\newpage\n"
