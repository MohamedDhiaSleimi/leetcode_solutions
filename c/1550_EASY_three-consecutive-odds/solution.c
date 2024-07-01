
bool threeConsecutiveOdds(int *arr, int arrSize) {
  for (int i = 1; i < arrSize - 1; i++) {
    if ((arr[i - 1] % 2) + (arr[i] % 2) + (arr[i + 1] % 2) == 3) {
      return true;
    }
  }
  return false;
}
