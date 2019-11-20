import numpy as np

import everest

mpi = everest.mpi

local_node_data = [
    (np.array([mpi.rank,]), np.array([mpi.rank ** 2,])),
    (np.array([mpi.rank * 2,]), np.array([mpi.rank ** 3,]))
    ]

gathered = mpi.comm.allgather(local_node_data)

global_data = np.sort(np.vstack(gathered), axis = 0).T[0][1]

if mpi.rank == 0:
    print(global_data.shape)

# from uw
#[[(array([0], dtype=int32), array([ 1.])), (array([1], dtype=int32), array([ 0.37102193]))
# from here
#[[(array(0), array(1.0)), (array(0), array(1.0))], [(array(1), array(0.0)),
