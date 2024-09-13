class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort Nums & use 3 pointers with i as the anchor
        # Basically we just go through all combos with 2 pointers (range minus i position) 
        # Pointers move up or down pending on differential to 0 (because its sorted)
        # Used an inneficient hashmap to exclude duplicates Switched to efficient check:
        # that i and l dont equal their past values
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            if i>0 and v == nums[i-1]:
                continue
            l,r = i+1, len(nums) -1
            while i < l < r:
                curr_val = v + nums[l] + nums[r]
                if curr_val < 0:
                    l += 1
                elif curr_val > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res        

    #innefficient hashmap remove duplicates:
            # hmap = {}

        #  key = str(str(v)+str(nums[l])+str(nums[r]))
        #             if key not in hmap:
        #                 hmap[key] = 1
        #                 res.append([v, nums[l], nums[r]])
        #             else:
        #                 pass
        #                 # print(f'repeated {key}')
