import numpy as np

from meshless.interpolate import interpolate_lagrange_2D, interpolate_lagrange_3D

def test_interpolate_lagrange_2D():
    a = 1
    b = 0.5
    xs = np.linspace(0, a, 12)
    ys = np.linspace(0, b, 12)
    xs, ys = np.meshgrid(xs, ys)
    x_nodes = [0, a/2, a]
    y_nodes = [0, b/2, b]
    theta_nodes = np.array([[0,   0, 0],
                            [45, 45, 45],
                            [0,   0, 0]])

    thetas = interpolate_lagrange_2D(xs.flatten(), ys.flatten(),
            x_nodes, y_nodes, theta_nodes)

    ans = np.array([ 0.        , 14.87603306, 26.7768595 , 35.70247934, 41.65289256,
       44.62809917, 44.62809917, 41.65289256, 35.70247934, 26.7768595 ,
       14.87603306,  0.        ,  0.        , 14.87603306, 26.7768595 ,
       35.70247934, 41.65289256, 44.62809917, 44.62809917, 41.65289256,
       35.70247934, 26.7768595 , 14.87603306,  0.        ,  0.        ,
       14.87603306, 26.7768595 , 35.70247934, 41.65289256, 44.62809917,
       44.62809917, 41.65289256, 35.70247934, 26.7768595 , 14.87603306,
        0.        ,  0.        , 14.87603306, 26.7768595 , 35.70247934,
       41.65289256, 44.62809917, 44.62809917, 41.65289256, 35.70247934,
       26.7768595 , 14.87603306,  0.        ,  0.        , 14.87603306,
       26.7768595 , 35.70247934, 41.65289256, 44.62809917, 44.62809917,
       41.65289256, 35.70247934, 26.7768595 , 14.87603306,  0.        ,
        0.        , 14.87603306, 26.7768595 , 35.70247934, 41.65289256,
       44.62809917, 44.62809917, 41.65289256, 35.70247934, 26.7768595 ,
       14.87603306,  0.        ,  0.        , 14.87603306, 26.7768595 ,
       35.70247934, 41.65289256, 44.62809917, 44.62809917, 41.65289256,
       35.70247934, 26.7768595 , 14.87603306,  0.        ,  0.        ,
       14.87603306, 26.7768595 , 35.70247934, 41.65289256, 44.62809917,
       44.62809917, 41.65289256, 35.70247934, 26.7768595 , 14.87603306,
        0.        ,  0.        , 14.87603306, 26.7768595 , 35.70247934,
       41.65289256, 44.62809917, 44.62809917, 41.65289256, 35.70247934,
       26.7768595 , 14.87603306,  0.        ,  0.        , 14.87603306,
       26.7768595 , 35.70247934, 41.65289256, 44.62809917, 44.62809917,
       41.65289256, 35.70247934, 26.7768595 , 14.87603306,  0.        ,
        0.        , 14.87603306, 26.7768595 , 35.70247934, 41.65289256,
       44.62809917, 44.62809917, 41.65289256, 35.70247934, 26.7768595 ,
       14.87603306,  0.        ,  0.        , 14.87603306, 26.7768595 ,
       35.70247934, 41.65289256, 44.62809917, 44.62809917, 41.65289256,
       35.70247934, 26.7768595 , 14.87603306,  0.        ])

    assert np.allclose(thetas, ans)


def test_interpolate_lagrange_3D():
    a = 1
    b = 2
    c = 3
    xs = np.linspace(0, a, 4)
    ys = np.linspace(0, b, 4)
    zs = np.linspace(0, c, 3)
    x = np.array(np.meshgrid(xs, ys, zs)).swapaxes(0, -1).reshape(-1, 3)

    x_nodes = [0, a/3, 2*a/3, a]
    y_nodes = [0, b/2, b]
    z_nodes = [0, c/2, c]
    theta_ref = np.array([
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        [[45, 0, 0],
         [45, 0, 0],
         [45, 0, 0]],
        [[45, 0, 0],
         [45, 0, 0],
         [45, 0, 0]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        ])

    thetas = interpolate_lagrange_3D(x[:, 0], x[:, 1], x[:, 2], x_nodes, y_nodes,
            z_nodes, theta_ref)

    ans = np.array([ 0.   , 45.   , 45.   ,  0.   ,  0.   , 45.   , 45.   ,  0.   ,
        0.   , 45.   , 45.   ,  0.   ,  0.   , 45.   , 45.   ,  0.   ,
        0.   , -5.625, -5.625,  0.   ,  0.   , -5.625, -5.625,  0.   ,
        0.   , -5.625, -5.625,  0.   ,  0.   , -5.625, -5.625,  0.   ,
        0.   , 45.   , 45.   ,  0.   ,  0.   , 45.   , 45.   ,  0.   ,
        0.   , 45.   , 45.   ,  0.   ,  0.   , 45.   , 45.   ,  0.   ])

    assert np.allclose(thetas, ans)

