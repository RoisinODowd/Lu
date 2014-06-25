#Usage:

#####**reducer.py**: used to find all common tumors between mutation, expression, and CNA data and writes the common tumors to OutputFile.
```
python reducer.py [MUTATIONS] [EXPRESSIONS (IlluminaHiSeq)] [CNA] [OutputFile]
```
#####**transpose.py**: takes in a matrix file where the rows are genes and the columns are tumors and transposes the file
```
python transpose.py [InputMatrix] [OutputMatrix]
```

#####**annotation.py**: takes in the tissueSourceSite.txt and CommonTumors outputted by reducer.py and outputs a file with cancer names and their corresponding TCGA tumor IDs
```
python annotation.py [CommonTumors]
```

All code written by Ritwik Gupta and Kevin Lu under the lab of Dr. Xinghua Lu at the Department of Biomedical Informatics, University of Pittsburgh.
