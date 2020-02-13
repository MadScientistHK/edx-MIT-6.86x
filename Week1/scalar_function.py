def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if(x<=y):
        return np.dot(x,y)
    else:
        return x/y
    raise NotImplementedError