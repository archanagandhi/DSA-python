# Searching Algorithms

* Linear Search
* Binary Search

## Linear Search

Linear search also known as **Sequential search** is a very simple search algorithm. A sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.

### Big O Complexity

* Time Complexity
   * ```Best Case - O(1)```  *element is found at the first index*
   * ```Worst Case - O(n)``` _element is found at the last index or element_
* Space Complexity - ``` O(1) ```

## Binary Search

Binary search  also known as half-interval search, logarithmic search, or binary chop is a fast search algorithm. This search algorithm works on the principle of **divide and conquer**.
Binary search looks for a item by comparing the middle most item of the collection. If a match occurs, then the index of item is returned. If the middle item is greater than the item, then the item is searched in the sub-array to the left of the middle item. Otherwise, the item is searched for in the sub-array to the right of the middle item. This process continues on the sub-array as well until the size of the subarray reduces to zero.

### Big O Complexity

* Time Complexity
   * ```Best Case - O(1)```  *element is found at the middle index*
   * ```Worst Case - O(logn)```
* Space Complexity - ``` O(1) ```

## Linear Vs Binary
<p align="center">
<img src="https://user-images.githubusercontent.com/74424757/124422656-439fd500-dd81-11eb-87f3-c539eff6c6b4.gif"></p>


