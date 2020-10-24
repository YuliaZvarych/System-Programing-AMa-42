package pack;

import java.util.Scanner;

public class Application {

  private static Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    runMenu();
  }

  private static void runSort() {
    int[] arr = {12, 11, 13, 5, 6, 7};

    System.out.print("\nInput array: ");
    printArray(arr);

    QuickSort ob = new QuickSort();
    ob.sort(arr, 0, arr.length - 1);

    System.out.print("Sorted array: ");
    printArray(arr);
  }

  private static void runSearch() {
    int[] arr = {2, 3, 4, 10, 40};
    int x = 10;
    int result = BinarySearch.binarySearch(arr, 0, arr.length - 1, x);
    System.out.print("\nOur array: ");
    printArray(arr);
    System.out.println("Input: " + x);
    if (result == -1) {
      System.out.println("Element not present");
    } else {
      System.out.println("Element found at index " + result);
    }
  }

  private static void printArray(int[] arr) {
    for (int value : arr) System.out.print(value + " ");
    System.out.println();
  }

  private static void runPaper() {
    int n = 13, m = 29;
    System.out.println("\nInput: " + n + " x " + m);
    System.out.println("Output: " + GFG.minimumSquare(n, m));
  }

  private static void runInterestingRow() {
    int n = 5;
    System.out.println("\nInput: " + n);
    int result = InterestingRow.interestingRow(n);
    System.out.println("Output: " + result);
  }

  private static void runMenu() {
    System.out.println("Welcome :)");
    boolean exit = true;
    while (exit) {
      printMenu();
      switch (sc.next()) {
        case "1": {
          runSort();
          break;
        }
        case "2": {
          runSearch();
          break;
        }
        case "3": {
          runInterestingRow();
          break;
        }
        case "5": {
          runPaper();
          break;
        }
        case "e": {
          System.out.println("\nSee you soon.");
          exit = false;
          break;
        }
        default: {
          break;
        }
      }
    }
  }

  private static void printMenu() {
    System.out.println("\nMenu:\n");
    System.out.println("'1' - if you want run sorting");
    System.out.println("'2' - if you want run searching");
    System.out.println("'3' - if you want run dynamic algorithm");
    System.out.println("'5' - if you want run greedy algorithm");
    System.out.println("'e' - if you want exit");
    System.out.print("Make your choice -> ");
  }
}
