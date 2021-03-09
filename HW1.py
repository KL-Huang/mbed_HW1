# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061249.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
station = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
output_data = []
target_data = list(filter(lambda item: item['TEMP'] != '-99.000', data))
target_data = list(filter(lambda item: item['TEMP'] != '-999.000', target_data))
for i in station:
   tmp = []
   target_data2 = list(filter(lambda item: item['station_id'] == i, target_data))
   top = -999.000
   for d in target_data2:
      if float(d['TEMP']) > top:
         top = float(d['TEMP'])
   tmp.append(i)
   if top == -999.000:
      tmp.append('None')
   else:   
      tmp.append(top)
   output_data.append(tmp)

#=======================================

# Part. 4
#=======================================
# Print result
print(output_data)
#========================================