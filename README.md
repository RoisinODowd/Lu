#Usage:

#####**reducer.py**: used to find all common tumors between transposed expression and CNA data and writes the common tumors to OutputFile.
```
python reducer.py [EXPRESSIONS (IlluminaHiSeq)] [CNA] [OutputFile]
```
#####**transpose.py**: takes in a matrix file where the rows are genes and the columns are tumors and transposes the file
```
python transpose.py [InputMatrix] [OutputMatrix]
```

#####**annotation.py**: takes in the tissueSourceSite.txt and CommonTumors outputted by reducer.py and outputs a file with cancer names and their corresponding TCGA tumor IDs
```
python annotation.py [CommonTumors]
```

#####**cdfMaker.py**: takes in two transposed matrix files: NormalMatrix and a TumorMatrix, and outputs OutputFile, which is a matrix of the CDFs for each element
```
python cdfMaker.py [NormalMatrix] [TumorMatrix] [OutputFile]
```

#####**cnaExpExtractor.py**: takes in three files, two transposed matrix files: CNA matrix and Expression Matrix, and one common tumor list, and outputs two files that are the common tumors between the CNA and Expression matrices
```
python cnaExpExtractor.py [CNA] [EXPRESSIONS] [CommonTumors] [OutputCNA] [OutputExpression]
```

#####**normalFinder.py**: takes in one transposed Expression matrix and outputs a matrix of normal samples
```
python normalFinder.py [EXPRESSIONS] [OutputNormalMatrix]
```

All code written by Ritwik Gupta and Kevin Lu under the lab of Dr. Xinghua Lu at the Department of Biomedical Informatics, University of Pittsburgh.
