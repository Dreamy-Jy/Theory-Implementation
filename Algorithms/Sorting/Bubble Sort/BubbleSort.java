import java.util.Arrays;

class BubbleSort {

  public static void bubbleSort(int[] array) {
    for(int run = 0; run < array.length; run++)
      for(int currentIndex = 0; currentIndex < array.length-1; currentIndex++ )
        if(array[currentIndex] > array[currentIndex + 1]) { swap(array, currentIndex + 1 , currentIndex); }
  }

  public static void swap(int[] array, int valueOneIndex, int valueTwoIndex) {
    int val = array[valueOneIndex];
    array[valueOneIndex] = array[valueTwoIndex];
    array[valueTwoIndex] = val;
  }

  public static void main(String[] args) {
    int[] array = generateIntArray_randomValues(10, 10, -10);
    //System.out.println( Arrays.toString(array) );
    bubbleSort(array);
    System.out.println( Arrays.toString(array) );
  }

  public static int[] generateIntArray_randomValues(int arrayLength, int upperLimit, int lowerLimit) {
    int [] array = new int[arrayLength];

    for (int i = 0; i < array.length; i++)
      array[i] = lowerLimit + (int)(Math.random() * (upperLimit - lowerLimit) + 1);

    return array;
  }
}
