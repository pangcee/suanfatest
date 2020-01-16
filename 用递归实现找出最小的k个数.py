
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k>len(tinput) or k ==0:
            return []
        heap = tinput[:k]
        self.build_max_heap(heap)
        for i in range(k,len(tinput)):
            if tinput[i]<heap[0]:
                heap[0] = tinput[i]
                self.max_heapify(heap,k,0)
        return self.heapsort(heap)
    def build_max_heap(self,heap):
        length = len(heap)
        for i in range(int(length/2-1),-1,-1):
            self.max_heapify(heap,length,i)
    #堆调整
    def max_heapify(self,heap,length,root):
        left = 2*root + 1
        right = 2*root + 2
        biger = root
        if left<length and heap[left]>heap[biger]:
            biger = left
        if right<length and heap[right]>heap[biger]:
            biger = right
        if biger!=root:
            heap[biger],heap[root] = heap[root],heap[biger]
            self.max_heapify(heap,length,biger)
    def heapsort(self,heap):
        length = len(heap)
        for i in range(length-1,-1,-1):
            heap[0],heap[i] = heap[i],heap[0]
            self.max_heapify(heap,i,0)
        return heap
s = Solution()
print(s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],6))
