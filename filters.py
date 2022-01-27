#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters
import csv
from sensor import generate_sensor_data

def mean_filter(data, filter_width=3):  # default 3 if not specified
    print('Original data length', len(data))
    print('Filter width = ', filter_width)
    odd = filter_width % 2 # Making sure input filter width  is an odd and + number
    if odd == 1 and filter_width > 0:
        # List with the averages (shorter than original)
        m_filter = [0] * (len(data) - (filter_width - 1))  # empty list of size
        print('New data length = ', len(m_filter))

    else:
        print('No Bueno...Negative or ven filter width wont work ')
        return ValueError


if __name__ == "__main__":
    mean_filter([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 3)


    # if len(data_length) == 1:
    #     data = data_length
    # else:
    #     data = generate_sensor_data(data_length)  # getting sensor data