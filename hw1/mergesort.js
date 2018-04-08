/*
* This module invokes the sort function that takes care of I/O and invoking the given sorting algorithm on input data.
* See merge-sort-func.js file for the implementation of the merge sort.
* See sort.js file for the I/O and merge-sort-func invocation.
*/
let sort = require('./sort');
sort('data.txt', 'merge.out', 'merge');