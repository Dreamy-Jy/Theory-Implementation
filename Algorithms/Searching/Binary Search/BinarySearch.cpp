#include<iostream>
#include<vector>

bool binarySearch(const std::vector<int> array, int findInArray) {
  vector<int> output;
  int stepCount = 0;
  int highSearchIndex = array.size()-1, lowSearchIndex = 0;
  int midSearchIndex;

  while(highSearchIndex >= lowSearchIndex) {
    stepCount++;
    midSearchIndex = lowSearchIndex + (highSearchIndex - lowSearchIndex)/2;

    if(array[midSearchIndex] == findInArray) return true;

    if(array[midSearchIndex] > findInArray) {
      highSearchIndex = midSearchIndex - 1;
    } else if (array[midSearchIndex] < findInArray) {
      lowSearchIndex = midSearchIndex + 1;
    } else {
       cout << "error" << endl;
    }
  }

  return false;
}

int main(int argc, char const *argv[]) {
  /* code */
  return 0;
}
