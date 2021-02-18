#https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    output=""
    for i in range(len(dna)):
        if (dna[i]=="A"):
            output+="T"
        elif (dna[i]=="T"):
            output+="A"
        elif (dna[i]=="G"):
            output+="C"
        elif (dna[i]=="C"):
            output+="G"

    return(output)

print(DNA_strand("ATGC"))
