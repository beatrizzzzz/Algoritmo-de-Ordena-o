import time

def insertion_sort(x):
    start_time = time.time()
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key
    end_time = time.time()
    print("O tempo de execução do Insertion Sort foi de:", end_time - start_time, "segundos")
    return x

for y in (1000, 10000, 100000):
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
      lista_ordenada = insertion_sort(data)
      end_time = time.time()
    
      str3 = 'num.' + x + '.' + z + '.out'
      str4 = str3
      print(str4)
    
      with open(str4, 'w') as f:
          f.write(str(n)+'\n')
          for num in lista_ordenada:
              f.write(str(num)+'\n')
            
      print("\nO tempo de execução do InsertionSort foi de:", end_time - start_time, "segundos")