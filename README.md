**NB: CSV files are ignored during Git push. Please copy the csv files into `data` folder during testing.**
## System Architecture
### The Leader and Follower between two pairs of Trajectories
1. **Data Layer:** This layer consists of the CSV files in the `"data"` folder, which contain the `latitude`, `longitude`, and `time` data of the vehicle trajectories.

2. **Model Layer:** This layer consists of the `Trajectory` class, which represents a vehicle trajectory. It has attributes such as name, latitudes, longitudes, and times. It also has methods such as haversine and `get_leader_follower`, which calculate the distance between two trajectories and determine the leader and follower trajectories, respectively.

3. **Controller Layer:** This layer consists of the `read_csv_files` function, which reads the CSV files and returns a list of Trajectory objects. It also contains the main function, which calls the `read_csv_files` function and uses the Trajectory methods to determine the leader and follower trajectories and calculate the minimum TTC.

4. **View Layer:** There is no specific view layer in this code as the output is printed to the console. However, the main function can be considered as the view layer as it orchestrates the interactions between the data, model, and controller layers.

Overall, the architecture follows the Model-View-Controller (MVC) pattern, where the data layer represents the model, the Trajectory class represents the model logic, the read_csv_files function and the main function represent the controller, and the console output represents the view.


### Minimum TTC between two pairs of Trajectories
1. **Data Input Module:** This module is responsible for reading the 
trajectory files (T1.csv, T2.csv, etc.) and storing the data in memory 
for further processing. The module uses the pandas library to read the 
CSV files.

2. **Data Preprocessing Module:** This module is responsible for cleaning
and preprocessing the trajectory data. It removes any missing or 
erroneous data points, and transforms the latitude and longitude 
coordinates to the Cartesian coordinate system. The module also 
computes the velocities of the vehicles using the positions and times.

3. **TTC Computation Module:** This module is responsible for computing the TTC values for each pair of trajectories. 
It uses the formula mentioned earlier: `TTC = (Xl - Xƒ-Dl)/(Vf − Vl)`. The module takes the preprocessed data as input 
and computes the TTC values for all valid pairs of trajectories.

4. **Result Visualization Module:** This module is responsible for 
visualizing the results. It creates a graph of the TTC values over time 
for each pair of trajectories. It highlights the minimum TTC value and 
displays it on the graph.

## Test Plan

1. **Unit Testing:** Perform unit tests on each module to ensure that it functions as expected. This involves testing 
individual functions and methods to check that they produce the correct output for different input values. For example, 
test that the data input module reads the CSV files correctly and that the data preprocessing module cleans and 
preprocesses the data correctly.

2. **Integration Testing:** Perform integration tests to ensure that the modules work correctly together. 
This involves testing the interaction between different modules to check that the data flows correctly and that the 
modules produce the expected output. For example, test that the TTC computation module takes the preprocessed data 
as input and computes the TTC values correctly.

3. **End-to-End Testing:** Perform end-to-end tests to ensure that the system works as a whole. This involves testing 
the system with real-world scenarios to check that it produces the expected results. For example, test the system 
with different pairs of trajectories with varying lengths and velocities to ensure that it computes the TTC values 
correctly and highlights the minimum TTC value correctly.

4. **Performance Testing:** Perform performance tests to ensure that the system can handle large datasets and compute 
the TTC values in a reasonable time. This involves testing the system with large trajectory datasets and measuring 
the time taken to compute the TTC values.

5. **User Acceptance Testing:** Perform user acceptance tests to ensure that the system meets the requirements of 
the end-users. This involves testing the system with representative end-users to check that it is easy to use, 
provides the expected results, and meets their requirements.

6. **Error Handling Testing:** Perform error handling tests to ensure that the system handles errors and edge cases 
correctly. This involves testing the system with different types of invalid input data, such as missing or corrupted 
data, and checking that the system produces appropriate error messages and handles the errors gracefully.

7. **Regression Testing:** Perform regression tests to ensure that the system continues to work correctly after 
changes or updates. This involves re-running the previous tests on the modified system to check that it produces 
the expected results and that the changes have not introduced any new errors or issues.