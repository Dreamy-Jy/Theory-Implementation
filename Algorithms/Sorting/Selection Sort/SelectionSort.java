import java.util.Arrays;

class SelectionSort {
  // sorts array into assenting order
  public static void selectionSort(int[] array) {

    for(int pointerIndex = 0; pointerIndex < array.length; pointerIndex++) {
      int minValueIndex = pointerIndex;

      for(int lookerIndex = pointerIndex + 1; lookerIndex < array.length; lookerIndex++)
        if (array[lookerIndex] < array[minValueIndex]) {minValueIndex = lookerIndex;}

      if(minValueIndex != pointerIndex) {swap(array, minValueIndex, pointerIndex);}
    }
  }

  public static void swap(int[] array, int lowerValueIndex, int highValueIndex) {
    int val = array[lowerValueIndex];
    array[lowerValueIndex] = array[highValueIndex];
    array[highValueIndex] = val;
  }

  public static void main(String[] args) {
    int[] array = generateRandomIntArray(100);
    selectionSort(array);
  }
/*helper methods for testing*/
  public static int[] generateRandomIntArray(int largestSize) {
    int [] array = new int[(int) (Math.random()*largestSize + 1)];

    for (int i = 0; i < array.length; i++)
      array[i] = (int) (Math.random()*(largestSize*10));

    return array;
  }
}
