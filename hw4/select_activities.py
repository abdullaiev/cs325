# Created by Illia Abdullaiev on 04/28/2018
from operator import itemgetter

# This function parses the inout file and groups activities that belong to one set.
# Then, select_activities function is being invoked against each group.
def parse():
    # get file pointers for input and output
    input_file = open("act.txt", "r")
    out_file = open("actions.out", "w")

    # read all lines from input file
    lines = input_file.readlines()

    count = 0
    set_count = 1
    activities = []

    for line in lines:
        # convert a line of text into an array of integers
        line = line.strip()
        line = line.split()
        numbers = [int(word) for word in line]

        if count == 0:
            # this is the number of activities there are to process
            count = int(numbers[0])
            activities = []
        else:
            # decrement the number of activities the are yet to process
            count = count - 1
            activities.append(numbers)

            # When all activities from this group have been collected, run select_activities function against this group
            if count == 0:
                out_file.write('Set ')
                out_file.write(str(set_count))
                out_file.write('\n')
                set_count = set_count + 1

                selected_activities = select_activities(activities)

                out_file.write('Number of activities selected = ')
                out_file.write(str(len(selected_activities)))
                out_file.write('\n')

                out_file.write('Activities: ')
                for activity in selected_activities:
                    out_file.write(str(activity[0]))
                    out_file.write(' ')
                out_file.write('\n')
                out_file.write('\n')

    input_file.close()
    out_file.close()


# This function selects activities by choosing the last ones to start.
def select_activities(activities):
    selected_activities = []

    # sort activities by their start time in descending order
    # itemgetter(1) gets the activity's start time for comparison
    activities = sorted(activities, key=itemgetter(1), reverse=True)

    # activity that starts the last will be the first one to be selected
    selected_activities.append(activities.pop(0))

    # Loop over the array of activities until it's empty
    while len(activities) > 0:
        activity = activities.pop(0)

        # if this activity's finish time does not conflict with the last activity selected,
        # we can add it to the array of selected activities
        if activity[2] <= selected_activities[0][1]:
            selected_activities.insert(0, activity)

    return selected_activities


parse()
