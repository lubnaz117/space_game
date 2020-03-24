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
    
def gravity2DAttitude(t, x, u):
    """
    Rigid body in 2D gravity equations of motion
    x = [x, y, vx, vy, theta, omega]
    u = [Fx, Fy, T]
    """
    g = 0.0001
    
    dxdt = np.empty_like(x)
    dxdt[0] = x[2]
    dxdt[1] = x[3]
    dxdt[2] = u[0]
    dxdt[3] = g + u[1]
    dxdt[4] = x[5]
    dxdt[5] = u[2] - x[5] * 0.0005
    return dxdt

def bounce(x):
    """
    x = [x, y, vx, vy, theta, omega]
    """
    
    # Velocity lost
    Cx = 0.8
    Cy = 0.7
    
    # Flip y velocity
    if x[3] > 0:
        x[2] = x[2] * Cx
        x[3] = - x[3] * Cy
