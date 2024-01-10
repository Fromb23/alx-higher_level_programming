#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Calculate the difference in both directions
    set_diff_1 = set_1.difference(set_2)
    set_diff_2 = set_2.difference(set_1)

    # Combine the results
    combined_diff = set_diff_1.union(set_diff_2)

    return combined_diff
