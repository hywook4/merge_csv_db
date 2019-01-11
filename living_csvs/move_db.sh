
shopt -s nullglob

dir=$PWD

for d in $dir/*
do
    if [ -d "$d" ]
    then
        for d2 in $d/*
        do
            if [ -d "$d2" ]
            then
                echo $d2

                for f in $d2/*.csv
                do
                    python3 living.py "$f"

                done

            fi
        done

    fi
done

echo merging csv files 'done'
