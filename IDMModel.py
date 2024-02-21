from __future__ import annotations
from typing import List
from Traffic import Traffic
import math


class IDM:
    def __init__(self, v0: float, v_i: float, x_0: float, a: float, s0: float, headway: float, b: float,
                 car_front: IDM | None, l: float):
        self.v0 = v0
        self.l = l
        self.a = a
        self.s0 = s0
        self.delta = 4
        self.headway = headway
        self.b = b
        self.x_arr = []
        self.v_arr = []
        self.car_front = car_front
        self.v = v_i
        self.x = x_0

    def s_star(self):
        if self.car_front is None:
            return None
        delta_v = self.car_front.v - self.v
        return self.s0 + self.v * self.headway + (self.v * delta_v) / (2 * math.sqrt(self.a * self.b))

    def find_v(self, t):
        v_free = self.a * (1 - (self.v / self.v0) ** self.delta)
        if self.car_front is None:
            return v_free * t
        v_int = -self.a * (((self.s_star()) / (self.car_front.x - self.x - self.l)) ** 2)
        v_total = v_int + v_free
        return v_total * t

    def find_x(self, t):
        return self.v * t


class Simulation:
    def __init__(self, cars: List[IDM], t_final: float, traffic_lights: List[Traffic] | None):
        self.cars = cars
        self.t_arr = []
        self.t_lights = traffic_lights
        self.t_final = t_final

    def simulate(self):
        h = 0.05
        t = 0
        while t < self.t_final:
            self.t_arr.append(t)
            for car in self.cars:
                braking_dist = (car.v ** 2) / (2 * car.b)
                braking = False
                stopped = False
                if self.t_lights is not None:
                    for tl in self.t_lights:
                        if (tl.x - car.x) - 3 <= braking_dist <= (tl.x - car.x) + 3:
                            if tl.state == "red" or tl.state == "yellow":
                                braking = True
                                if stopped:
                                    continue
                                car.v += -car.b * h
                                if -0.1 < car.v < 0.1:
                                    car.v = 0
                                car.x += car.v * h
                        tl.update(h)
                if not braking:
                    new_v = car.find_v(h)
                    car.v += new_v
                    new_x = car.find_x(h)
                    car.x += new_x
                car.x_arr.append(car.x)
                car.v_arr.append(car.v)
                if t + h > self.t_final:
                    t = self.t_final
                else:
                    t += h
