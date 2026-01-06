class Linearsearching:
    def solution(self,arr,element):
        is_present=False
        i = 0
        while i<len(arr):
            if arr[i] == element:
                is_present=True
                break
            i += 1
        print(is_present)
lst=[12,3,24,5,6,21,54]
element=24
linear_instance=Linearsearching()
linear_instance.solution(lst,element)
