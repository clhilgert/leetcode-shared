// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

// Example 1:
// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]

// Input: temperatures = [73,73,73,500]
// Output: [3,2,1,0]

// Example 2:
// Input: temperatures = [30,40,50,60]
// Output: [1,1,1,0]

// Example 3:
// Input: temperatures = [30,60,90]
// Output: [1,1,0]

function dailyTemperatures(temperatures: number[]): number[] {
    const stack:number[][] = [];
    const output: number[] = Array.from({length: temperatures.length}).fill(0) as number[];
  
    for (let i = 0; i < temperatures.length; i += 1){
      const currTemp = temperatures[i];
      if (stack.length === 0) {
        stack[0] = [currTemp, 0]
      };
      while (stack.length > 0 && currTemp > stack[stack.length - 1][0]) {
        output[i] = i - stack.pop()![1]
      } 
      stack.push([currTemp, i])
    }
    return output;
  };
  
  const temps = [73,73,73,500]
  console.log(dailyTemperatures(temps))