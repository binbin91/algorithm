# -*- coding: utf-8 -*-

def InversePairs(data):
    if len(data) > 1:
        print data
        mid = len(data) / 2
        left_half = data[:mid]
        print 'left half:', left_half
        right_half = data[mid:]
        print 'right half:', right_half
        left_count = InversePairs(left_half)%1000000007
        right_count = InversePairs(right_half)%1000000007
        i,j,k,count = len(left_half)-1,len(right_half)-1,len(data)-1,0
        print i,j,k,count
        while i >= 0 and j >= 0:
            if left_half[i] < right_half[j]:
                data[k] = right_half[j] 
                j = j - 1
                k = k - 1
            else:
                data[k] = left_half[i]
                count += (j+1)
                print count
                i = i - 1
                k = k - 1
            print 'while 1, data:', data
        while i >= 0:
            data[k] = left_half[i]
            k = k - 1
            i = i - 1
            print 'while 2, data:', data
        while j>=0:
            data[k] = right_half[j]
            k = k - 1
            j = j - 1
            print 'while 3, data:', data
        print 'data:', data
        print 'count:', count
        print 'left_count:', left_count
        print 'right_count:', right_count
        return (count + left_count + right_count)%1000000007
    else:
        return 0


if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,0] 
    print InversePairs(array)
