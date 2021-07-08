# Insertion Sort

Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration. Insertion sort works similarly as we sort cards in our hand in a card game.

## Steps to Perform

* The array spilled virtually in the two parts in the insertion sort - An unsorted part and sorted part.
* The sorted part contains the first element of the array and other unsorted subpart contains the rest of the array. The first element in the unsorted array is compared to the sorted array so that we can place it into a proper sub-array.
* It focuses on inserting the elements by moving all elements if the right-side value is smaller than the left side.
* It will repeatedly happen until the all element is inserted at correct place.

<p align ="center" >
<img src="https://user-images.githubusercontent.com/74424757/124907039-56c2d700-e005-11eb-8b30-703adb1cf221.gif" width="500px" height="200px">
</p>

## Complexity

* Time Complexity
 
   * ```Worst Case(Big-O) - О(n^2) comparisons and swaps)``` *when whole array is unsorted
   * ```Best Case(Big-Omega) - O(n) comparisons, O(1) swaps``` *When array is sorted

* Space Complexity - ``` O(1) ```
