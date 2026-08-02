class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for el in strs:
            result += f"{len(el)}#{el}"
        return result

    def decode(self, s: str) -> List[str]:
        inx = 0
        result = []
        n = len(s)
        while inx < n:
            count_str = ""
            while s[inx] != "#":
                count_str += s[inx]
                inx += 1

            count = int(count_str)
            # Move index past the delimiter
            inx += 1
            
            next_str = s[inx : inx + count]
            inx += count

            result.append(next_str)

        return result