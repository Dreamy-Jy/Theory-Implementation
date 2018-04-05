public class LinkedList {
  public static class Node {
    private int data;
    private Node next;

    public Node(int data) {
      this.data = data;
    }

    public Node(int data, Node next) {
      this.data = data;
      this.next = next;
    }

    public void setData(int newData) {
      this.data = newData;
    }

    public int getData() {
      return this.data;
    }

    public void setNext(Node newNext) {
      this.next = newNext;
    }

    public Node getNext() {
      return this.next;
    }

    public void deleteNext() {
      this.next = null;
    }

    @Override
    public String toString() {
      return "("+this.data+")>";
    }
  }

  private Node head;
  //private int length; we'll start with a naive implementation

  public LinkedList(int headData) {
    head = new Node(headData);
  }

  // public LinkedList(int[] data) {
  //   head = new Node(data[0]);
  //   for() {}

  // }

  public void add(int data) {
    if(head != null) {
      Node current = head;

      while(current.next != null) {
        current = current.next;
      }

      current.next = new Node(data);
      return;
    }

    head = new Node(data);
  }

  public void reverse() {
    Node prev = null, current = head, next;

    while(current != null) {
      next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }

    head = prev;

  }

  @Override
  public String toString() {
    String output = "";
    Node current = this.head;
    while (current != null) {
      output = output + current;
      current =  current.next;
    }
    return output+"null";
  }
}
