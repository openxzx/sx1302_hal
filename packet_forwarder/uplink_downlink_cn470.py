#!/usr/bin/env python3


def main():
    idx = 1
    up_data = []
    down_data = []

    for tmp_up in range(4703, 4894, 2):
        up_data.append(tmp_up)

    for tmp_down in range(5003, 5098, 2):
        down_data.append(tmp_down)

    for i in range(96):
        if idx % 8 == 0:
            if i < 48:
                print("\033[0;31m%0.1f/%0.1f\033[0m" % (up_data[i] / 10, down_data[i] / 10))
            else:
                print("\033[0;31m%0.1f/%0.1f\033[0m" % (up_data[i] / 10, down_data[48 - i] / 10))
        else:
            if i < 48:
                print("%0.1f/%0.1f " % (up_data[i] / 10, down_data[i] / 10), end='')
            else:
                print("%0.1f/%0.1f " % (up_data[i] / 10, down_data[48 - i] / 10), end='')
        idx = idx + 1


if __name__ == '__main__':
    main()
