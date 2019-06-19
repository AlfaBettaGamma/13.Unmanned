def wait_to_time(time,red_time,green_time):
  cycle = red_time + green_time
  if (time % cycle) < red_time :
    return red_time -  (time % cycle)
  else:
    return 0

def Unmanned(L, N, track):
  result = 0
  for i in range(L):
    svet = 0
    for j in range(N):
      if track[j][0] == i:
        result = result + wait_to_time(result,track[j][1],track[j][2])
        svet = 1
    result = result + 1
  return result