class Solution:
    def trap(self, height):
        if not height:
            return 0
        f = 0
        cur = 0
        ret = 0
        for idx, h in enumerate(height):
            if h >= height[f]:
                cur = idx
                if height[f] == 0:
                    f = cur

                    continue
                else:
                    ret += min(height[f], height[cur]) * (cur - f) - sum(height[f: cur])
                    for i in range(f, cur):
                        height[i] = height[f]
                f = idx

        dheight = height[::-1]
        dcur = 0
        df = 0
        for idx, h in enumerate(dheight):
            if h >= dheight[df]:
                dcur = idx
                if dheight[df] == 0:
                    df = dcur

                    continue
                else:
                    ret += min(dheight[df], dheight[dcur]) * (dcur - df) - sum(dheight[df: dcur])
                df = idx

        return ret
