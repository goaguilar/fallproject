My project is a flask app using python to take a text file that looks like this:
### lambda (microns)   Flambda (Normalized)
       1.2823071      0.97216253
       1.2823256      0.94421876
       1.2823441      0.94064778
       1.2823626      0.92688638
       1.2823811      0.91960648
       1.2823995      0.88540490
       1.2824180      0.83564144
       1.2824365      0.80550864
       1.2824550      0.88036657
       1.2824734      0.85811955
and fits a function to this data in the form of a gaussian or a lorentzian function.
Its implementation is fairly simple, launch flask from the terminal while the directory is 
pointed to where application.py is located. 
Type in:
$ export FLASK_APP=application.py
$ flask run 

When the app is launched, the homepage shows up with a function selection option and an upload 
button to upload the text file that is formatted as above. A gaussian function is wider than 
a lorentzian function and a user can experiment with both to find the one that most models the 
dips in the data.
	My sampledata is data taken from the high resolution data from the NIRSPEC Brown Dwarf Spectroscopic 
Survey (BDSS) and can be downloaded as a .dat file. Converting it into a .txt file is as simple as 
copying and pasting the data into another file and saving it with a .txt extension. Currently, the 
app takes the uploaded data, and returns a response in the form of a png of the function calculated to
the highest "peak", or "dip" from the original data. The graph shows the original data, the baseline 
calculated from the python code optimized for that data, and a function using that baseline that models
the biggest "dip". Due to the nature of the data, almost none of the data from the survey would contain
any peaks, only dips representing the absorption lines from the elements in the brown dwarf's atmosphere.
The title gives the parameters for the function that the user selected in the home screen. A is the amplitude 
of the function. mu is the expected value of the function, and sigma is the variance. Given these values, one could 
gain valuable information from the raw data for analysis. Of course, should one wish to play around with the 
python modules, it is easy to import them into a python interpreter to mess around with. One could change the iteration
that specfit goes through or add more functions to mathutils.py to have more models for your data. 
	The app is limited however, in that it only fits one function to the data. In cases where there are two or 
more visible peaks in the data, the app would only fit to the one with the biggest deviation from the baseline. 