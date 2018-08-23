# Task 16
def have_trains_crashed(v1, v2):
    total_distance = 10
    fist_train_save_distance = 4
    first_train_time = 4 / v1
    second_train_time = 6 / v2
    if not second_train_time < first_train_time:
        print("Trains did not crash!")
        return True
    else:
        print("Trains crashed!")
        return False

crash_test = have_trains_crashed(100, 50)