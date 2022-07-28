from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """

        :param pushed:
        :param popped:
        :return:
        """
        st = []
        for i in  pushed:
            st.append(i)
            while len(popped) > 0 and len(st) > 0 and st[-1] == popped[0]:
            #if st[-1] == popped[0]:
                popped.pop(0)
                st.pop()
            else:
                continue
        # while len(popped) > 0 and len(st) > 0 and st[-1] == popped[0]:
        #     # if st[-1] == popped[0]:
        #     popped.pop(0)
        if len(popped) == 0:
            return True
        return False

a = Solution(
             )
print(a.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))