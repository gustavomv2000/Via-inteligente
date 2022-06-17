import numpy as np
import random

class Vehicle:
    def __init__(self, config={}):
        # Set default configuration
        self.set_default_config()

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

        # Calculate properties
        self.init_properties()

    def set_default_config(self):    
        self.l = 4
        self.s0 = 4
        self.T = 1
        self.v_max = 16.6
        # self.a_max = 5 * random.uniform(1, 1.12) - 0.80 * random.uniform(0, 0.12)
        self.a_max = 3 
        self.b_max = 4.61

        self.path = []
        self.current_road_index = 0

        self.x = 0
        self.v = self.v_max
        self.a = 0
        self.stopped = False

    def init_properties(self):
        self.sqrt_ab = 2*np.sqrt(self.a_max*self.b_max)
        self._v_max = self.v_max

    def update(self, lead, dt):
        # Update position and velocity
        print(self.v)
        if self.v + self.a*dt < 0:
            self.x -= 1/2*self.v*self.v/self.a
            self.v = 0
        else:
            self.v += self.a*dt
            self.x += self.v*dt + self.a*dt*dt/2
        
        # Update acceleration
        alpha = 0
        if lead:
            delta_x = lead.x - self.x - lead.l
            delta_v = self.v - lead.v

            alpha = (self.s0 + max(0, self.T*self.v + delta_v*self.v/self.sqrt_ab)) / delta_x

        self.a = self.a_max * (1-(self.v/self.v_max)**4 - alpha**2)
        # self.a = self.a * random.uniform(1, 1.12) - self.a * random.uniform(0, 0.12)
        # if self.a < 1 * 0.5 or self.a > 1 * 1.1:
        #     self.a = 1 * random.uniform(1, 108)/100 - 1 * random.uniform(0, 8)/100

        # self.v_max = self._v_max * random.uniform(1, 1.50) - self._v_max * random.uniform(0, 0.50)
        # if self.v_max < 11.11 * 0.5 or self.v_max > 11.11 * 1.1:
        #     self.v_max = 11.11 * random.uniform(1, 1.08) - 11.11 * random.uniform(0, 0.08)

        # print(self.a)

        # print(self.v_max)

        if self.stopped: 
            self.a = -self.b_max*self.v/self.v_max
        
    def stop(self):
        self.stopped = True

    def unstop(self):
        self.stopped = False

    def slow(self, v):
        # self.v_max = v * random.uniform(1, 1.12) - self._v * random.uniform(0, 0.12)
        self.v_max = v

    def unslow(self):
        # self.v_max = self._v_max * random.uniform(1, 1.12) - self._v_max * random.uniform(0, 0.12)
        self.v_max = self._v_max 
        

