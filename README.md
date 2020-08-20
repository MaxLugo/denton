# Denton proportional procedure

The package provide a function to make an interpolation using the denton proportional procedure. It uses 2 arrays: the first one is the indicator array (high frequency data) and the second one is the aggregate array (low frequency data). Notice that the first array must have multiple number of elements of the second one. In this case, it is consider that the second array as means of a subsets elements of the first array. Boths array must be order ascending in time.

An example is included in the repository

The methodology was taken from: https://www.imf.org/external/pubs/ft/qna/pdf/2017/chapter6.pdf

The package use the FCO of minimization problem to get the optimal solution. 





