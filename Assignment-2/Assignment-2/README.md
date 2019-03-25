# Write-Up for Assignment 2
## Prologue
I'm going to put most of my outputs in this document, but if you want to run my notebook, be aware of a few things first.
This notebook SHOULD run everything if you just press "run all" in jupyter notebook.
Getting it to do that took a lot of work, however. I think there were a few data points in the B set that were unique
compared to the A dataset and vice versa, specifically in the categorigal variables. This meant that when I use get_dummies,
that I would get columns unique to the A set and B set, and that they would have a different number of columns, which
made using the models trained on the A set a pain to use on the B set (dimensionality errors or something). 
I ended up going with the naive approach of deleting any columns in the A set that were not in the B set and vice 
versa due to time constraints. In order to make this work, I had to resplit and retrain all of the models 
(on the A data still) to take in the new shape of data. I originally did this by scrolling up and down and running 
different blocks as I needed to out of order, but that quickly began to confuse even me, and I wrote this! So a lot 
of time had to be sunk into making the entire notebook run in sequence with (hopefully) no errors. Now with that out
of the way, let's begin.

## Part 1: Data Preparation
I looked at the dtypes of the dataset as well as checking for missing values, and there were a lot of missing values.
I decided to make two datasets, one where I deleted columns with missing values, (which was around a fourth of the data)
and one where I filled in the missing data points. For the missing data points, I put in