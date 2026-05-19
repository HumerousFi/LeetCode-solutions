use std::collections::HashMap;
impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        
        let mut seen : HashMap<i32, i32> = HashMap::new();
        let mut max_elem: i32 = nums.iter().max().unwrap().clone();
        let mut ans: i32 = 0;
        for num in nums.into_iter() {
            if num > 0 && ! seen.contains_key(&num) {
                ans += num;
            }
            seen.insert(num, 1);
        }
        if ans > 0 {ans} else {max_elem} 
    }
}