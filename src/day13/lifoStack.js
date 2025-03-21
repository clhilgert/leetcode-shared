// Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

// Implement the MyStack class:

// void push(int x) Pushes element x to the top of the stack.
// int pop() Removes the element on the top of the stack and returns it.
// int top() Returns the element on the top of the stack.
// boolean empty() Returns true if the stack is empty, false otherwise.
// Notes:

// You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
// Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

// Example 1:

// Explanation
// MyStack myStack = new MyStack();
// myStack.push(1);
// myStack.push(2);
// myStack.top(); // return 2
// myStack.pop(); // return 2
// myStack.empty(); // return False

class Stack {
  // pop from front, push to the back, view the front

  constructor() {
    this.firstQ = [];
    this.secondQ = [];
  }
  //return nothing
  push(val) {
    this.firstQ.push(val);
  }

  //returns value
  top() {
    let value;
    for (let i = 0; i < this.firstQ.length; i++) {
      //record first item
      value = this.firstQ[0];
      //pop
      this.secondQ.push(this.firstQ.shift());
    }
    for (let i = 0; i < this.secondQ.length; i++) {
      this.firstQ.push(this.secondQ.shift());
    }
    return value;
  }

  //returns value
  pop() {
    let value;
    for (let i = 0; i < this.firstQ.length - 1; i++) {
      //record first item
      //pop
      this.secondQ.push(this.firstQ.shift());
    }
    value = this.firstQ.shift();
    for (let i = 0; i < this.secondQ.length; i++) {
      this.firstQ.push(this.secondQ.shift());
    }

    return value;
  }

  //return boolean
  empty() {
    if (this.firstQ.length === 0) return true;
    return false;
  }
}
