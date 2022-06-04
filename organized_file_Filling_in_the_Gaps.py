import re
import os
from pathlib import Path, PosixPath


def fill_the_gaps(path: PosixPath) -> None:

    regex = re.compile(r'[a-zA-Z-_ ]+[0-9][0-9][0-9].[a-z]+')
    file_nums = []
    for filepath in path.glob("*"):
        file_name = os.path.basename(filepath)
        if regex.search(file_name).group():
            num_regex = re.compile(r'[0-9][0-9][0-9]\.')
            file_nums.append([file_name, filepath, int(
                num_regex.search(file_name).group().strip("."))])

    file_nums = sorted(file_nums)
    difference = 0
    for idx in range(len(file_nums)-1):
        difference = file_nums[idx+1][2]-file_nums[idx][2]
        if difference > 1:
            prev_num = file_nums[idx+1][2]
            file_nums[idx+1][2] = file_nums[idx][2] + 1
            file_nums[idx+1][0] = file_nums[idx+1][0].replace(str(prev_num),
                                                              str(file_nums[idx][2] + 1))
            os.rename(file_nums[idx+1][1], Path(path / file_nums[idx+1][0]))


if _name_ == '_main_':
    fill_the_gaps(Path("/home/arslan/spam_backup"))
