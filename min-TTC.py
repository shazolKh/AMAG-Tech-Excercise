import pandas as pd
from typing import List, Tuple


class Trajectory:
    def __init__(self, csv_file: str, vehicle_length: float = 3.0):
        self.data = pd.read_csv(f"./data/{csv_file}")
        self.vehicle_length = vehicle_length

    def get_positions(self) -> Tuple[List[float], List[float]]:
        return list(self.data['Latitude']), list(self.data['Longitude'])

    def get_velocities(self) -> List[float]:
        try:
            positions = self.get_positions()
            time = list(self.data['Time (s)'])
            dx = [positions[0][i + 1] - positions[0][i] for i in range(len(positions[0]) - 1)]
            dy = [positions[1][i + 1] - positions[1][i] for i in range(len(positions[1]) - 1)]
            dt = [time[i + 1] - time[i] for i in range(len(time) - 1)]
            velocities = [((dx[i] ** 2 + dy[i] ** 2) ** 0.5) / dt[i] for i in range(len(dx))]
            velocities.append(velocities[-1])
            return velocities
        except Exception as ex:
            print(ex)
            return []

    def compute_ttc(self, other: 'Trajectory') -> List[float]:
        try:
            my_pos = self.get_positions()
            other_pos = other.get_positions()
            my_vel = self.get_velocities()
            other_vel = other.get_velocities()
            my_length = self.vehicle_length
            other_length = other.vehicle_length
            ttc = []
            for i in range(len(my_pos[0])):
                if i >= len(other_pos[0]):
                    break
                xl = other_pos[0][i]
                xf = my_pos[0][i]
                dl = other_length
                vl = other_vel[i]
                vf = my_vel[i]
                t = (xl - xf - dl) / (vf - vl)
                if t >= 0:
                    ttc.append(t)
            return ttc
        except Exception as ex:
            print(ex)
            return []

    def get_min_ttc(self, other: 'Trajectory') -> float:
        try:
            ttcs = self.compute_ttc(other)
            return min(ttcs) if ttcs else float('inf')
        except Exception as ex:
            print(ex)
            return float('inf')


files_list = [['T1', 'T2'], ['T1', 'T2_2'], ['T3', 'T4']]
for files in files_list:
    t1 = Trajectory(files[0] + '.csv')
    t2 = Trajectory(files[1] + '.csv')

    min_ttc = t1.get_min_ttc(t2)
    print(f"Minimum TTC between {files[0]} and {files[1]} is {min_ttc:.2f}")
