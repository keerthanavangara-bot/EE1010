import numpy as np

P = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])

# trace equals sum of eigenvalues
trace_P = np.trace(P)
eigenvalues = np.linalg.eigvals(P)
sum_eigen = np.sum(eigenvalues)
print(np.isclose(trace_P, sum_eigen))

# P^T P is identity
PTP = np.dot(P.T, P)
print(PTP)
print(np.allclose(PTP, np.eye(3)))

# P is skew-symmetric
print(np.allclose(P.T, -P))

# all eigenvalue magnitudes are 1
magnitudes = np.abs(eigenvalues)
print(np.allclose(magnitudes, 1.0))
