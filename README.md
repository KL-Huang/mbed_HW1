## mbed_HW1
### (1) how to setup and run my program:
        * First, download "107061249.csv" and "HW1.py", then put them into the same directory.
        * Second, open the terminal, use the command
            $ python HW1.py
        * then the terminal will show the results.   
### (2) what are the results:
        * It will show that the station_id (which we choose here is 'C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260') and the maximum value of TEMP of the station.
        
        [['C0A880', 24.8], ['C0F9A0', 25.8], ['C0G640', 27.9], ['C0R190', 28.5], ['C0X260', 30.1]]
### (3) what are the program do:
        [1] read in the csv file '107061249.csv' and put the data in the dictionary 'data'.
        [2] set 'station' as the list of target stations we want.
        [3] use the filter to remove the data whose value of the 'TEMP' column is '-99.000' or '-999.000'.
        [4] for each target station, use the filter to choose the data from that station into 'target_data2'.
        [5] find the maximum value of 'TEMP' for the station and change the data type into float.
        [6] append the 'station_id' and maximum temperature 'top' into the list 'tmp'.
        [7] if there is no maximum of 'TEMP', append string 'None'.
        [8] output the results.
