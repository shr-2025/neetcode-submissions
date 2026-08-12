class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        down, up = 0, len(matrix) - 1
        while down <= up:
            m_y = (up + down) // 2
            if matrix[m_y][0] <= target <= matrix[m_y][-1]: 
                left, right = 0, len(matrix[m_y]) - 1
                while left <= right:
                    m_x = (left + right) // 2
                    if target == matrix[m_y][m_x]:
                        return True
                    elif target < matrix[m_y][m_x]:
                        right = m_x - 1
                    else:
                        left = m_x + 1
                return False
            elif target < matrix[m_y][0]:
                up = m_y - 1
            else:
                down = m_y +1
        return False