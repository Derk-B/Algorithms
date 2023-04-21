def search(target, left, right, data):
    while(left <= right):
        mid = (left + right) // 2

        if(data[mid] == target):
            return mid
        
        if(data[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    return None

def main(target, data):
    end_index = len(data) - 1
    print(search(target, 0, end_index, data))