Title: Math in bash
lang: en

the simple way

    echo $((2+2))

the complex way

    echo 2+2|bc -lq

get a random number

    echo $(($RANDOM%10))
