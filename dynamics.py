import numpy as np

def propagate(fun, t0, x0, dt, u):
    """
    Propagate state by timestep using RK4
    """
    # Step 1
    k0 = fun(t0, x0, u)
    
    # Step 2
    t1 = t0 + dt / 2
    x1 = x0 + k0 * dt / 2
    k1 = fun(t1, x1, u)
    
    # Step 3
    t2 = t0 + dt / 2
    x2 = x0 + k1 * dt / 2
    k2 = fun(t2, x2, u)
    
    # Step 4
    t3 = t0 + dt
    x3 = x0 + k2 * dt
    k3 = fun(t3, x3, u)
    
    # New state at t + dt
    xnew = x0 + (k0 + 2 * k1 + 2 * k2 + k3) * dt / 6
    return xnew
    
   
def gravity2D(t, x, u):
    """
    Dynamics function
    """
    g = 0.0001
    
    dxdt = np.empty_like(x)
    dxdt[0] = x[2]
    dxdt[1] = x[3]
    dxdt[2] = u[0]
    dxdt[3] = g + u[1]
    return dxdt


if __name__ == "__main__":
    fun = double_integrator
    t = 0
    x = np.array([0, 1])
    dt = 1
    

    for ii in range(5):
        x = propagate(fun, t, x, dt)
        t += dt
        print(t, x)