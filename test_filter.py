#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters
import csv
from amp_filter import apply_amp_filter
from sensor import generate_sensor_data


def write_to_csv(data_length):
    data = generate_sensor_data(data_length)
    filtered = apply_amp_filter(data)
    with open('test_filter.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # for i in range(data_length):
        writer.writerow(data)
        writer.writerow(filtered)
    return


print(write_to_csv(10))