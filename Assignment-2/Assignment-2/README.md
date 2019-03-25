# Write-Up for Assignment 2
## Prologue
If you want to run my notebook, be aware of a few things first.
This notebook SHOULD run everything if you just press "run all" in jupyter notebook.
Getting it to do that took a lot of work, however. I think there were a few data points in the B set that were unique
compared to the A dataset and vice versa, specifically in the categorigal variables. This meant that when I use get_dummies,
that I would get columns unique to the A set and B set, and that they would have a different number of columns, which
made using the models trained on the A set a pain to use on the B set (dimensionality errors or something). 
I ended up going with the naive approach of deleting any columns in the A set that were not in the B set and vice 
versa due to time constraints. Both columns still had well over 150 columns in the end though. In order to make this 
work, I had to resplit and retrain all of the models (on the A data still) to take in the new shape of data. 
I originally did this by scrolling up and down and running different blocks as I needed to out of order, but that 
quickly began to confuse even me, and I wrote the entire notebook! So a lot of time had to be sunk into making the 
entire notebook run in sequence with (hopefully) no errors. Now with that out of the way, let's begin.

## Part 1: Data Preparation
I looked at the dtypes of the dataset as well as checking for missing values, and there were a lot of missing values.
I decided to make two datasets, one where I deleted columns with missing values, (which was around a fourth of the data)
and one where I filled in the missing data points. For the missing data points, I looked at columns where there were NaN
values, and checked the data type. I chose a few variables at my own discretion that had the data type float 
(such as Garage Area) and filled them in with the constant 0, and the rest of the floats with the mean of the column.
I chose the mean because it seemed like the 'safer' and more statistically standard option. For all of the categorical
variables I filled in missing values with the mode. I also deleted the PID column, because it looked like an ID column
which we know has no bearing on price. I also reordered the dataframe and put the target in the first column for easy
access. After that was all done, I used the cat_features function we made in class to identify all of the categorical
features and one-hot encode them with get_dummies. I looked at the categorical features and didn't see any features that 
I thought would benefit from label encoding. 

## Part 2: Exploratory Analysis and Hypotheses
As far as exploratory analysis goes, I didn't really do a lot to be honest. I did an initial linear regression using
all of the features, which is more or a part 3 thing, but I just wanted to see what kind of r2 I would get. I ended up
getting over .8, which I thought was pretty good for a baseline. If 80% of the variability in price could be explained
by a linear regression, I figured that a polynomial regression was kind of out of the question. Scatter matrices really
didn't want to load, even if I only did 5 features at a time or so, and having 2000 data points on tiny little scatter
plots would make it nigh unreadable even if I tediously did scatter matrices five features at a time. So I didn't use 
scatter matrices at all. 

## Part 3: Making Models
I started with two baselines: one with NaNs simply deleted, another with them filled in. Since I was using linear
regression, my error metric of choice was going to be r2, since its the most human-readable metric of performance
for a linear regression, so to speak. The deletion set got an r2 of .8586, and the filled set got .9014. Because I 
was filling in the means for a lot of variables, that 5% increase might be a false positive from the inpution 
strategy I chose. Going further with the filled set, I used RFECV to try and find the optimal feature set... and my 
performance TANKED. The r2 was .6221. Not sure why. I decided to move on to regularization, I used a loop to try and 
find the optimal alphas for the deletion set and the filled set, using the LASSO model. The best alpha was around 2.5 
for both, and for the deletion set the r2 increased to .8641. The filled set barely increased to .9058. I also tried 
regularization on the feature selected set of filled data, and the performance dropped again, down to .6215. Based on 
these metrics, the best performing model was the regularized baseline for the filled dataset, with an r2 of .9058.

## Part 4: Predicting and Validation, or how all my models failed to generalize.
As I mentioned before, simply getting all my models to run on the B dataset was a trial in and of itself, but I managed
to get things working. I followed my previous approach, one deletion set, and one filled set. I performed all the same
tranforms as part 1 here as well, deleting PID and using the same inpution strategies on the same columns. Testing the 
original base model on the B deletion set yielded a r2 of .9090. Somehow, the baseline performed even better on the B 
set than the A set. I then used the baseline model trained on the filled in data from set A on the filled set B and
the r2 was... -26.7929. Something is off. And I couldn't figure out what. Moving on to feature selection, I used my 
selector, trained on the A set to select variables from the B set, then test them with the same model that was used on
the A set for this test. The r2 was again, -26.7929. Great. Moving on to my LASSO models, the deletion baseline got a
.9187, the best r2 any model had gotten to that point. The LASSO baseline for the filled set got a negative, -24.6011 
this time to be exact. Bringing LASSO to look at the feature selected set B got the same result, -24.6011. I think the 
inpution strategies I used really really REALLY caused my models to overfit. My 'best' model was the LASSO deletion baseline. 