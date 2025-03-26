import numpy as np
def is_string_of_ones(mat):
  break_ = False
  first_index = [0,0]
  for x in range(mat.shape[0]):
    for y in range(mat.shape[1]):
      if mat[x,y] == 1:
        first_index = [x,y]
        break_ = True
        break
    if break_:
      break

  nbrs = [(0, 1), (0,-1), (1,0), (-1, 0)]
  cands = [first_index]
  for idx in cands:
    if mat[idx[0],idx[1]] == 1:
      mat[idx[0],idx[1]] = 0
      for nbr in nbrs:
        nbr_idx = (nbr[0] + idx[0], nbr[1] + idx[1])
        if 0 <= nbr_idx[0] < mat.shape[0] and 0 <= nbr_idx[1] < mat.shape[1]: 
          cands.append(nbr_idx)
  return not (1 in mat)

mat1 = np.array([
[1,1,0,0,1],
[1,0,0,0,1],
[1,1,0,0,1],
[0,1,1,1,1]]
)

mat2 = np.array([
[1,1,0,0,1],
[1,0,0,0,1],
[0,1,0,0,1],
[0,0,0,0,0]]
)

print(is_string_of_ones(mat1) )
print(is_string_of_ones(mat2) )