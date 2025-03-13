// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// Implement the MinStack class:

// MinStack() initializes the stack object.
// void push(int val) pushes the element val onto the stack.
// void pop() removes the element on the top of the stack.
// int top() gets the top element of the stack.
// int getMin() retrieves the minimum element in the stack.
// You must implement a solution with O(1) time complexity for each function.

class MinStack {
    stack: number[][]
    constructor() {
        this.stack = [];
    }
    //[10,5]
    push(val: number): void {
      if (this.stack.length === 0){
        this.stack[this.stack.length] = [val, val];
      } else{
        if (val < this.stack[this.stack.length-1][1]) {
          this.stack[this.stack.length] = [val, val]
        } else {
          this.stack[this.stack.length] = [val, this.stack[this.stack.length-1][1]]
        }
      }
    }
  
    pop(): void {
        if (this.stack.length > 0) {
            this.stack.pop();
        }
    }
  
    top(): number {
      return this.stack[this.stack.length-1][0]  
    }
  
    getMin(): number {
      return this.stack[this.stack.length-1][1]
    }
  }
  
  /**
  * Your MinStack object will be instantiated and called as such:
  * var obj = new MinStack()
  * obj.push(val)
  * obj.pop()
  * var param_3 = obj.top()
  * var param_4 = obj.getMin()
  */
  
  const obj = new MinStack()
  obj.push(5);
  obj.push(6);
  obj.push(2);
  console.log(obj.getMin()); // 2
  obj.pop();
  console.log(obj.getMin()); // 5
  