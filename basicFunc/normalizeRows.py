def normalizeRows(x):
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    
    x = x / x_norm

    return x
