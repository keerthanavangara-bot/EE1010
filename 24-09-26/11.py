import numpy as np

P = np.array([
        [1, 0, 1],
            [0, 1, 0],
                [1, 0, 1]
                ])

print("Matrix P:")
print(P)
print("-" * 40)

# trace equals sum of eigenvalues
trace_P = np.trace(P)
eigenvalues = np.linalg.eigvals(P)
sum_eigen = np.sum(eigenvalues)

print(f"Trace of P: {trace_P}")
print(f"Sum of Eigenvalues: {np.real_if_close(sum_eigen)}")
print(f"Equal? {np.isclose(trace_P, sum_eigen)}")
print("-" * 40)

# check if P^T P is identity
PTP = np.dot(P.T, P)

print("P^T P =")
print(PTP)
print(f"Identity? {np.allclose(PTP, np.eye(3))}")
print("-" * 40)

# check if P is skew-symmetric
print("P^T =")
print(P.T)
print(f"Skew-symmetric? {np.allclose(P.T, -P)}")
print("-" * 40)

# check magnitudes of eigenvalues
magnitudes = np.abs(eigenvalues)

print("Eigenvalues of P:")
print(np.real_if_close(eigenvalues))
print("Magnitudes:")
print(np.real_if_close(magnitudes))
print(f"All |eigenvalue| = 1? {np.allclose(magnitudes, 1.0)}")
print("-" * 40)
