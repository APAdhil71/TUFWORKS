class BinarySearch:
    def solution(self,arr,element):
        arr.sort()
        low = 0
        upp = len(arr)-1
        is_present = False
        while(low<=upp):
            mid=(low+upp)//2
            if element==arr[mid]:
                is_present=True
                break
            elif element< arr[mid]:
                upp = mid-1
            elif element>arr[mid]:
                low = mid+1
        print(is_present)
arr=[1,2,3,4,5,6,7,8,9]
element=12
binary_instance=BinarySearch()
binary_instance.solution(arr,element)

