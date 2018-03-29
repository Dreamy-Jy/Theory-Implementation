import java.util.Arrays;

class InsertionSort {
  /*old insertion sort implementation start*/
    public static void oldInsertionSort(int[] array) {
      for(int currentValueIndex = 0; currentValueIndex < array.length; currentValueIndex++) {
        int lessThanValueIndex = -1;

        int searchIndex = currentValueIndex - 1;

        while( lessThanValueIndex < 0 && searchIndex >= 0 ) {
          if(array[searchIndex] < array[currentValueIndex]) {
            lessThanValueIndex = searchIndex;
          }
          searchIndex--;
        }

        if (lessThanValueIndex < 0) {
          shiftAndInsert(array, currentValueIndex, 0);
        } else {
          shiftAndInsert(array, currentValueIndex, lessThanValueIndex + 1);
        }
      }
    }

    public static void shiftAndInsert(int[] array, int valueIndex, int insertToIndex ) {
      int value = array[valueIndex];
      for(int index = valueIndex; index > insertToIndex; index--) {
        array[index] = array[index - 1];
      }
      array[insertToIndex] = value;
    }
/*old insertion sort implementation end*/

    public static void insertionSort(int[] array) {
      for(int selectedIndex = 0; selectedIndex < array.length; selectedIndex++) {
        int selectedValue = array[selectedIndex];
        
        int shiftIndex = selectedIndex;
        while(shiftIndex > 0 && !(array[shiftIndex - 1] < selectedValue)) {
          array[shiftIndex] = array[shiftIndex - 1];
          shiftIndex--;
        }

        array[shiftIndex] = selectedValue;
      }
    }

    public static void main(String[] args) {
      int[] array = generateRandomIntArray(100);
      System.out.println(Arrays.toString(array));
      insertionSort(array);

      System.out.println("Array after insert:\n"+Arrays.toString(array));
    }

    public static int[] generateRandomIntArray(int largestSize) {
      int [] array = new int[(int) (Math.random()*largestSize + 1)];

      for (int i = 0; i < array.length; i++)
        array[i] = (int) (Math.random()*(largestSize*10));

      return array;
    }
}
