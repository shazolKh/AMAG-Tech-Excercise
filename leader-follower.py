import math
import pandas as pd


class Trajectory:
    def __init__(self, name, latitudes, longitudes, times):
        self.name = name
        self.latitudes = latitudes
        self.longitudes = longitudes
        self.times = times

    """
    The haversine method calculates the distance between two points on the Earth's surface 
    using the haversine formula, which is an equation that takes the spherical geometry of 
    the Earth into account when calculating distances between points.
    """
    def haversine(self, other):
        R = 6371  # Earth's radius in km

        length = min(len(self.latitudes), len(other.latitudes))
        distances = []

        """
        There are different length of rows between the CSV files. So, took the minimum length of the rows.
        i.e.  If the length of T1.csv is 10 and length of T2.csv is 5, then the loop will run only 5 times.
        """
        for i in range(length):
            lat1, lon1 = math.radians(self.latitudes[i]), math.radians(self.longitudes[i])
            lat2, lon2 = math.radians(other.latitudes[i]), math.radians(other.longitudes[i])

            lat_diff = lat2 - lat1
            lon_diff = lon2 - lon1

            """
            a: square of half the chord length between the two points.
            c: angular distance in radians between the two points.
            d: distance between the two points along the surface of the sphere(Earth), in kilometers.
            """
            a = math.sin(lat_diff / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = R * c

            distances.append(d)

        return distances

    def get_leader_follower(self, other):
        distances = self.haversine(other)

        if distances[0] < distances[-1]:
            leader = self
            follower = other
        else:
            leader = other
            follower = self

        return leader, follower

    def __str__(self):
        return self.name


def read_csv_files(files):
    trajectories = []
    for file in files:
        df = pd.read_csv(f"./data/{file}.csv")
        latitudes = df['Latitude'].tolist()
        longitudes = df['Longitude'].tolist()
        times = df['Time (s)'].tolist()
        trajectory = Trajectory(file, latitudes, longitudes, times)
        trajectories.append(trajectory)
    return trajectories


# Read trajectories from CSV files
files_list = [['T1', 'T2'], ['T1', 'T2_2'], ['T3', 'T4']]
for files in files_list:
    trajectories = read_csv_files(files)

    # Determine leader and follower
    leader, follower = trajectories[0].get_leader_follower(trajectories[1])
    print(f"For {files} === Leader: {leader}, Follower: {follower}")
