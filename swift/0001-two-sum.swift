// ! Day 1 // 9.28


class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var map: [Int:Int] = [:]
        for (i, num) in nums.enumerated() {
            if let mapped = map[target - nums[i]] {
                return [mapped, i]
            }
            map[nums[i]] = i 
        }
        return []
    }
}
