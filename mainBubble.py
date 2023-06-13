#BUBBLE SORT

import time
def bubble_sort(x):
    start_time = time.time()
    n = len(x)
    # Executa o loop n vezes
    for i in range(n):
        # Últimos i elementos já estão ordenados
        for j in range(0, n-i-1):
            # Se o elemento atual for maior que o próximo, troque-os
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    end_time = time.time()
    print("O tempo de execução do BubbleSort foi de:", end_time - start_time, "segundos")
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
      
      sorted_data = bubble_sort(data)

      str3 = 'num.' + x + '.' + z + '.out'
      str4 = str3
      print(str4)
      
      with open(str4, 'w') as f:
          f.write(str(n)+'\n')
          for num in sorted_data:
              f.write(str(num)+'\n')