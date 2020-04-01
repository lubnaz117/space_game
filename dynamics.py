import numpy as np
import math

from    space_game_helpers import *

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
        
    # Gravity lol
    g = 0.0001
    
    # Attitude control gains
    if u[2] == 0:
        kp = 5E-6
        kd = 5E-3
    else: # Turn off control when there is input
        kp = 0
        kd = 0

    # Force from thrusters
    th = x[4]    
    cth = math.cos(th * math.pi / 180)
    sth = math.sin(th * math.pi / 180)    
    F_thrust = np.array([cth * u[0] + sth * u[1], -sth * u[0] + cth * u[1]])
    
    # Force from gravity
    F_grav = np.array([0, g])
    
    # Torque from input
    T_input = u[2]
    
    # Torque from control
    T_control = - x[4] * kp - x[5] * kd
    
    dxdt = np.empty_like(x)
    dxdt[0] = x[2]
    dxdt[1] = x[3]
    dxdt[2] = F_thrust[0] + F_grav[0]
    dxdt[3] = F_thrust[1] + F_grav[1]
    dxdt[4] = x[5]
    dxdt[5] = T_input + T_control
    return dxdt

def bounce(x):
    """
    x = [x, y, vx, vy, theta, omega]
    """
    
    # Velocity lost after a bounce
    Cx = 0.8
    Cy = 0.7
    
    # Flip x and y velocity
    if x[3] > 0:
        x[2] = -x[2] * Cx
        x[3] = - x[3] * Cy
