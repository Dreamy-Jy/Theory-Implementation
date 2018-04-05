#include <iostream>
#include <vector>

using namespace std;

bool binarySearch(const vector<int>& array, const int& findInArray) {
  vector<int> output;
  int highSearchIndex = array.size()-1, lowSearchIndex = 0;
  int midSearchIndex;

  while(highSearchIndex >= lowSearchIndex) {
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
