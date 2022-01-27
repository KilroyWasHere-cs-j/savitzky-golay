import numpy as np
import random
import matplotlib.pyplot as plt


class KalmanFilter(object):
    def __init__(self, dt, u, std_acc, std_meas):
        self.dt = dt
        self.u = u
        self.std_acc = std_acc
        self.A = np.matrix([[1, self.dt],
                            [0, 1]])
        self.B = np.matrix([[(self.dt ** 2) / 2], [self.dt]])
        self.H = np.matrix([[1, 0]])
        self.Q = np.matrix([[(self.dt ** 4) / 4, (self.dt ** 3) / 2],
                            [(self.dt ** 3) / 2, self.dt ** 2]]) * self.std_acc ** 2
        self.R = std_meas ** 2
        self.P = np.eye(self.A.shape[1])
        self.x = np.matrix([[0], [0]])

    def predict(self):
        # Ref :Eq.(9) and Eq.(10)
        # Update time state
        self.x = np.dot(self.A, self.x) + np.dot(self.B, self.u)
        # Calculate error covariance
        # P= A*P*A' + Q
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        return self.x

    def update(self, z):
        # Ref :Eq.(11) , Eq.(11) and Eq.(13)
        # S = H*P*H'+R
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        # Calculate the Kalman Gain
        # K = P * H'* inv(H*P*H'+R)
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  # Eq.(11)
        self.x = np.round(self.x + np.dot(K, (z - np.dot(self.H, self.x))))  # Eq.(12)
        I = np.eye(self.H.shape[1])
        self.P = (I - (K * self.H)) * self.P  # Eq.(13)
        print("Update>> ", str(self.P))


def main():
    dt = 0.1  # Spacing
    t = np.arange(0, 10, dt)  # Fill in matrix with numbers 0 - 100 with 0.1 spacing
    # Define a model track
    u = 0.1
    # Speed of the robot
    std_acc = 1.3   # we assume that the standard deviation of the acceleration is 0.25 (m/s^2)
    std_meas = 3.5  # and standard deviation of the measurement is 1.2 (m)
    # create KalmanFilter object
    kf = KalmanFilter(dt, u, std_acc, std_meas)
    predictions = []
    measurements = []
    for j in range(0, 100):
        x = 1.0 + np.random.normal(-2, 5)

        i = np.matrix([x])
        print("Measured Pose>> ", i)
        predictions.append(kf.predict()[0])
        print("Predicted Pose>> ", kf.predict()[0])
        measurements.append(i.item(0))
        kf.update(i.item(0))
        print(i.item(0))
        # Measurement
        # To be deprecated
        # i = np.matrix(str(random.randint(0, 50)), str(random.randint(0, 50)))

        # The measured poses of the robot
    fig = plt.figure()
    fig.suptitle('Example of Kalman filter for tracking a moving object in 1-D', fontsize=10)
    plt.plot(t, measurements, label='Measurements', color='b',linewidth=0.5)
    plt.plot(t, np.squeeze(predictions), label='Kalman Filter Prediction', color='r', linewidth=1.5)
    plt.xlabel('Time (s)', fontsize=10)
    plt.ylabel('Position (m)', fontsize=10)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()