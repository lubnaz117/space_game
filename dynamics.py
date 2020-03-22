import numpy as np

def propagate(t0, x0, dt):
    """
    Propagate state by timestep
    """
    # First step
    t1 = t0
    x1 = x0
    k1 = f(t0, x1)
    
    xnew = np.empty_like(x0)
    xnew = x0 + k1 * dt

    return xnew
    

def f(t, x):
    """
    Dynamics function
    """
    dxdt = np.empty_like(x)
    
    dxdt[0] = x[1]
    dxdt[1] = 0
    
    return dxdt

if __name__ == "__main__":

    t = 0
    x = np.array([0, 1])
    dt = 1

    for ii in range(5):
        x = propagate(t, x, dt)
        t += dt
        print(t, x)