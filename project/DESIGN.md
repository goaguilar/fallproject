#About the project
	This project was an idea inspired by some research I did the summer of my freshman year.
The idea was to effectively model these large dips and peaks in the data from brown dwarves.
The first step for any program was to create a baseline, a line or curve that was modeled where most of the 
data was located. According to the people giving us the project, the baseline was usally done by hand, using
their own judement to decide what would be a suitable line from which to fit the peaks or dips to. 
	The idea was to create a mathematically rigorous calculation of the baseline using python, specifically 
using numpy and scipy. The next step would be to actually fit the peaks to the data with the baseline and 
returning the parameters of that function. The valuable information would be the position at which the 
peak was located, and the FWHM(Full Width at Half Max) which was the measure of the width of an object 
and was used as a measure of the astronomical seeing conditions. The FWHM could be meausred in a gaussian,
for example, by going to the x coordinate of the peak, going to half of the peak's value in the y-axis, 
and then calculating the width from that point to the sides of the function. Given that the research experience 
was only eight weeks and I had no initial experience with python, me and my partner barely got far. We only 
managed to create a rought baseline for the sample data and was unable to actually find and plot the functions 
to model the dips. 
	The baseline was found by creating a line using the polynomial object from numpy. The first baseline could 
be completely off the mark, and later iterations would get closer and closer to the data. This was done by 
using the fit function that belongs to the polynomial object. The real problem was making sure that the 
really large peaks and dips in the data wouldn't influence the fits or else we would get a line that was 
visibly below or above the median value of the data. The key to solving this was to fit an arbitrary gaussian 
to the data using scipy.optimize, which would take an array of x coordinates, y coordinates, a function, and 
initial parameters and give the parameters for the given function that better fit the data. The algorithm 
subtracts this gaussian from the data and then calculate a new baseline, fit another gaussian that would grab 
the second highest peak or dip, optimize it, and subtract that from the data. Each progressive iteration would 
remove the more divergent peaks and dips and give us a more accurate curve. The computer would know when to stop 
when a convergence test would run comparing the previous iteration to the current iteration and give a value 
that was less than an specific number, an small arbitrary value set by the function. The function also had a 
max iteration value that would force the computer to stop in case the convergence test never reached the set value. 
	The main function in functionfit, specfit, returns to the user cntm, the polynomial object, whose parameters 
describe the baseline for the function, and gparams which was a tuple containing the parameters for the A, mu, and sigma
for a gaussian or lorentzian function. 
	These modules were than imported into the application.py file that would create the flask app. When it runs,
the user would be presented with a list of the two available functions, and the button to upload a text file. When the 
user clicks the submit button, a copy of the text file would be saved to a folder in the static directory 
in order for numpy.genfromtxt to work. Specfit would run the algorithm on the generated data, and the parameters for 
the baseline and the function would be evaluated at the points given by the txt file. Then, the app uses numpy.matplotlib
to plot a graph containing the original data, the baseline, and the function fit. This data would be turned into a BYTESIO
and converted into a response that would read the object and display the plots, with the parameters for the function listed 
in the title. 