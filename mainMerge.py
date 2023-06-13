import time

def merge_sort(x):
    if len(x) > 1:
        mid = len(x) // 2
        left_half = x[:mid]
        right_half = x[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                x[k] = left_half[i]
                i += 1
            else:
                x[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            x[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            x[k] = right_half[j]
            j += 1
            k += 1
    return x
  

for y in(1000, 10000, 100000):
  for i in range(1,5,1):
      x = str(y)
      z = str(i)
      str1 = 'num.' + x + '.' + z + '.in'
      str2 = str1
  
      with open(str2, 'r') as f:
          n = int(f.readline().strip())
          data = []
          for i in range(n):
            data.append(int(f.readline().strip()))
            
      start_time = time.time()
      lista_ordenada = merge_sort(data)
      end_time = time.time()

      str3 = 'num.' + x + '.' + z + '.out'
      str4 = str3
      print(str4)
    
      with open(str4, 'w') as f:
          f.write(str(n)+'\n')
          for num in lista_ordenada:
              f.write(str(num)+'\n')
            
      print("O tempo de execução do MergeSort foi de:", end_time - start_time, "segundos")