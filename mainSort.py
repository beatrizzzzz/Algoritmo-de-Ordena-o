import time

def quick_sort(V, ini, fim):
  if ini < fim:
    p = partition(V, ini, fim)
    quick_sort(V, ini, p-1)
    quick_sort(V, p+1, fim)

  return V
    
def partition(V, ini, fim):
    a = ini - 1
    p = V[fim]
    b = ini
  
    while True:
        if b == fim:
            break
          
        if V[b] < p:
            a += 1
            (V[a], V[b]) = (V[b], V[a])
          
        b += 1
    (V[a + 1], V[fim]) = (V[fim], V[a + 1])
    return a + 1



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
      sorted_data = quick_sort(data,0,y-1)
      end_time = time.time()
  
      str3 = 'num.' + x + '.' + z + '.out'
      str4 = str3
      print(str4)
    
      with open(str4, 'w') as f:
          f.write(str(n)+'\n')
          for num in sorted_data:
              f.write(str(num)+'\n')
      
      
      print("O tempo de execução do QuickSort foi de:", str2, " - ", end_time - start_time, "segundos")
  