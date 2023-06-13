import time

def selection_sort(x):
    start_time = time.time()
    for i in range(len(x)-1):
        min_idx = i
        for j in range(i+1, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
    end_time = time.time()
    print("O tempo de execução do SelectionSort foi de:", end_time - start_time, "segundos")
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
      lista_ordenada = selection_sort(data)
      end_time = time.time()
    
      str3 = 'num.' + x + '.' + z + '.out'
      str4 = str3
      print(str4)
    
      with open(str4, 'w') as f:
          f.write(str(n)+'\n')
          for num in lista_ordenada:
              f.write(str(num)+'\n')
            
    