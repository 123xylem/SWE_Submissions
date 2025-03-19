class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Read only first num of each row.
        #Read previous row once Row is > target
        #Binary search that row for target
        for i in range(len(matrix)):  
            if matrix[i][0] == target:
                return True
            if target < matrix[0][0]:
                return False

            if target < matrix[i][0]:
                search_row = matrix[i - 1]
                if len(search_row) == 1:
                    return search_row[0] == target
                l, r = 0, len(search_row) -1
                while l <= r:
                    mid = l + (r - l) // 2
                    if search_row[mid] < target:
                        l = mid + 1
                    elif search_row[mid] > target:
                        r = mid - 1
                    else:
                        return True

                return False
                                        

        return target in matrix[-1]              

