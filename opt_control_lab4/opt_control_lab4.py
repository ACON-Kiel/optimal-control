from optlab_library import plot_cart_pole_graphs, \
    animate_cart_pole, parse_arguments
from scipy.integrate import ode, solve_bvp
import numpy as np
from numpy import sin, cos


def cart_pole_ode(t, x):
    x0 = x[0]
    x1 = x[1]
    x2 = x[2]
    x3 = x[3]
    lam0 = x[4]
    lam1 = x[5]
    lam2 = x[6]
    lam3 = x[7]

    # Pole length
    l = 0.5
    # Gravitational acceleration
    g = 9.81
    # Preallocate \dot{x}
    xd = np.zeros((8, x.shape[1]))

    # @TODO Compute the input u

    # @TODO Assign the equations of motion _and_ adjoint states
    # xd[0] = ...
    # ...
    # xd[7] = ...

    return xd


def boundary_fun(ya, yb):
    # @TODO Fill in the correct boundary conditions
    bcs = np.array([ya[0],
                    yb[0],
                    ya[1],
                    yb[1],
                    ya[2],
                    yb[2],
                    ya[3],
                    yb[3]])
    return bcs


if __name__ == '__main__':
    options = parse_arguments()

    t0 = 0.0
    T = 3.0
    dt = 0.001

    # Define collocation points
    t = np.linspace(t0, T, int(1.0 / dt))
    y0 = np.zeros((8, t.shape[0]))
    res = solve_bvp(cart_pole_ode, boundary_fun, t, y0,
                    max_nodes=10000,
                    verbose=2)

    y = np.array([res.sol(t)]).T

    # @TODO Compute the input u with the final state

    if options.graph:
        plot_cart_pole_graphs(t, y, u)
    if options.animate:
        animation = animate_cart_pole(t, y)
