# Quick Sort

Quick sort also known as **Partition-exchange sort** is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

Two best partition methods are:
* Hoare Partition Scheme
* Lomuto Partition Scheme

## Steps to perform:
* Pick an element (mostly first or last) and name as Pivot.
* Partitioning- the array elements are positioned that all the elements smaller than the pivot will be on the left side of the pivot and all the elements greater than the pivot will be on the right side of it.
* And the pivot element will be at its final sorted position.
* The elements to the left and right, may not be sorted.
* Then we pick subarrays, elements on the left of pivot and elements on the right of pivot, and we perform partitioning on them by choosing a pivot in the subarrays.

<p align ="center" >
<img src="https://user-images.githubusercontent.com/74424757/124618372-5acfe700-de95-11eb-8d62-5936f9fdf943.gif" width="500px" height="200px">
</p>

## Complexity

* Time Complexity
 
   * ```Worst Case(Big-O) - O(n^2)``` *when the list is already sorted*
   * ```Average Case(Big-Theta) - O(n logn)```

   
* Space Complexity - ``` O(logn) ```
