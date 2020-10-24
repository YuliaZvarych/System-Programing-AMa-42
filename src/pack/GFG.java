package pack;

class GFG {

  static int minimumSquare(int a, int b) {
    int result = 0, rem = 0;

    if (a < b){
      int temp = a;
      a = b;
      b = temp;
    }

    while (b > 0) {
      result += a / b;
      rem = a % b;
      a = b;
      b = rem;
    }

    return result;
  }
}
