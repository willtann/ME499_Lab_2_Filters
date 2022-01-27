#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_2_Filters


def mean_filter(data, filter_width=3):  # default 3 if not specified
    print('Original data length = ', len(data))
    print('Filter width = ', filter_width)
    odd = filter_width % 2  # Making sure input filter width  is an odd and + number

    if odd == 1 and filter_width > 0:  # odd and positive width
        # List with the averages (shorter than original)
        m_filter = [filter_width] * (len(data) - (filter_width - 1))  # empty list of size
        print('New data length = ', len(m_filter))
        l_data = len(data)

        # Calculate cumulative sum for each set with function
        def sum_c(data):
            sum_data = data.copy()  # Leave data alone
            for i in range(1, len(data)):
                sum_data[i] = sum_data[i] + sum_data[i - 1]
            return sum_data

        sum_calc = sum_c(data)
        # Refining cumulative sum to filter_width
        # zipping to avoid type discrepancies
        sum_calc[filter_width:] = [a - b for a, b in zip(sum_calc[filter_width:] , sum_calc[:-filter_width])]
        # Divide sum of index by filter width to find mean
        return sum_calc[filter_width - 1:] / filter_width

    else:
        # print('No Bueno...Negative or ven filter width wont work ')
        return ValueError


if __name__ == "__main__":
    print(mean_filter([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 3))
