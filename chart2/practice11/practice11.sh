sed "s/[[:blank:]]/ /g" chart2/popular-names.txt
tr '\t' ' ' chart2/popular-names.txt
expand -t 1 chart2/popular-names.txt