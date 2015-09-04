Title: Finding the filesystem of a partition
lang: en

    :::bash
    file -sL /dev/sda3
    fsck -N /dev/sda3
