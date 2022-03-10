def insertion_sort_yt(data):
    outer_loop = 0
    for i in range (1, len(data)):
        inner_loop = 0
        outer_loop = outer_loop + 1
        j = i
        while data[j-1] > data[j] and j > 0:
            data [j-1], data[j] = data[j], data[j-1]
            j = j - 1
            inner_loop = inner_loop + 1
    return data, outer_loop, inner_loop

def bubble_sort(data):
    flag = True
    while flag == True:
        flag = False
        for i in range(0, len(data)-1):
            if data[i] > data[i] + 1:
                flag = True
                data[i], data[i+1], = data[i+1], data[i]
    return data

def selection_sort(data):
    for i in data:
        smallest = i

        for j in range(i+1, len(data)):
            if data[j] < data[smallest]:
                smallest = j

        if smallest != data[i]:
            data[i], data[smallest] = data[smallest], data[i]
            
    return data 
            

list = [9,2,6,1,4,7,4,8,9,1]

print("yt")
data_yt, outer_yt, inner_yt = insertion_sort_yt(list)
print(data_yt, outer_yt, inner_yt)

print("bubble: ", bubble_sort(list))
print("selection: ", selection_sort(list))