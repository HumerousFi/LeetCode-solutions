impl Solution {
    pub fn xor_operation(n: i32, start: i32) -> i32 {
        let mut result = 0;
        let mut val = start;
        for _ in 0..n {
            result ^= val;
            val += 2;
        }
        result
    }
}