def count_negative(sequence):
    count = 0
    index = 0
    for index in sequence:
        if index < 0:
            count = count + 1
    return count




print(count_negative([-1, 0, -2, 1, -3, 2]))
print(count_negative([ 2.,  1.,  0., -1., -2.]))
print(count_negative([-3, -2, -1,  0,  1]))
print(count_negative([
        0.00000000e+00,  2.53654584e-01,  4.90717552e-01,  6.95682551e-01,
        8.55142763e-01,  9.58667853e-01,  9.99486216e-01,  9.74927912e-01,
        8.86599306e-01,  7.40277997e-01,  5.45534901e-01,  3.15108218e-01,
        6.40702200e-02, -1.91158629e-01, -4.33883739e-01, -6.48228395e-01,
       -8.20172255e-01, -9.38468422e-01, -9.95379113e-01, -9.87181783e-01,
       -9.14412623e-01, -7.81831482e-01, -5.98110530e-01, -3.75267005e-01,
       -1.27877162e-01,  1.27877162e-01,  3.75267005e-01,  5.98110530e-01,
        7.81831482e-01,  9.14412623e-01,  9.87181783e-01,  9.95379113e-01,
        9.38468422e-01,  8.20172255e-01,  6.48228395e-01,  4.33883739e-01,
        1.91158629e-01, -6.40702200e-02, -3.15108218e-01, -5.45534901e-01,
       -7.40277997e-01, -8.86599306e-01, -9.74927912e-01, -9.99486216e-01,
       -9.58667853e-01, -8.55142763e-01, -6.95682551e-01, -4.90717552e-01,
       -2.53654584e-01, -4.89858720e-16]))
print(count_negative([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))