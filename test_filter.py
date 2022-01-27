#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters
import csv
from amp_filter import apply_amp_filter
from sensor import generate_sensor_data


def write_to_csv(data_length):
    data = generate_sensor_data(data_length)
    filtered = apply_amp_filter(data)
    with open('test_filter.csv', 'w') as f:
        writer = csv.writer(f)
        for val in data:
            writer.writerows(zip(data))

            # writer.writerows([data])
    # print(data)
    #
    # with open('test_filter.csv') as file:
    #     for i in range(data_length):
    #         writer = csv.writer(file)
    #         writer.writerow(data[:1])
    #         writer.writerow(filtered[:2])
    return


print(write_to_csv(10))