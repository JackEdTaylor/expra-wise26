# Participate

Here, you will find instructions on how to participate in the Demo experiment.

## **Step 1**: Ensure PsychoPy is installed

First, as we'll be using psychopy, make sure you have correctly installed the standalone installation of PsychoPy, as explained in the [setup page](https://jackedtaylor.github.io/expra-wise24/introduction/setup.html).

## **Step 2**: Download and Extract the Files

**a**) [Download the Psychopy experiment](demo_experiment.zip) as a `.zip` folder. If you have a keyboard with no Alt keys, you can download this version of the experiment instead: [Experiment with No Alt Keys](demo_experiment_no_alt_keys.zip)

**b**) Extract the files from the `.zip` folder, and put them in a relevant folder for the ExPra.

**c**) Make sure that all the files are in the same folder. The files inside the demo experiment folder should look something like this:

<img src="demo_experiment_screenshot.png" onerror="this.onerror=null; this.src='https://raw.githubusercontent.com/JackEdTaylor/expra-wise24/master/lecture/demo/demo_experiment_screenshot.png'">

## **Step 3**: Check you are in "Run" Mode

Make sure that "Run" is selected in the toggle button at the top, and not "Pilot".

If set to "Run" mode, the play button will be green. If the play button is orange, you are probably in "Pilot" mode.

<img src="demo_experiment_runmode.png" onerror="this.onerror=null; this.src='https://raw.githubusercontent.com/JackEdTaylor/expra-wise24/master/lecture/demo/demo_experiment_runmode.png'">

## **Step 4**: Take Part!

In the experiment, you will have to identify which words are real, and which words are fake. These terms will be explained fully at the start of the experiment, but if you still If you have any questions about the task, then please ask!

To start the experiment, simply open `demo_experiment.psyexp` with PsychoPy. Once in the experiment, click the *Run experiment* button, circled below. The experiment should take around 20 minutes.

<img src="demo_experiment_run.png" onerror="this.onerror=null; this.src='https://raw.githubusercontent.com/JackEdTaylor/expra-wise24/master/lecture/demo/demo_experiment_run.png'">

## **Step 5**: Check the Data

Now that you've taken part, you want to check that the experiment has saved your responses. In the demo experiment folder, if you now enter the `data` folder, you should see 3 files: a `.csv` file, a `.log` file, and a `.psydat` file.

<img src="demo_experiment_data_screenshot.png" onerror="this.onerror=null; this.src='https://raw.githubusercontent.com/JackEdTaylor/expra-wise24/master/lecture/demo/demo_experiment_data_screenshot.png'">

Open the `.csv` file: you should have 313 rows, containing columns that store lots of relevant information about the stimuli and the experiment. Usually, each row is a single trial, but sometimes we also store other useful information during the experiment. The column, `text`, should contain all of the words and pseudowords that you saw. The column `stim_resp.corr` should contain your accuracies, and the column `stim_resp.rt` should contain your response times (in seconds). If that's all there, then you're good to go!

## **Step 6**: Send the Data

If the data all look to be there, you can upload and send the `.csv` containing your data to the `demo-data` channel in the Discord server.

That's it, you're done!

Here's a gif of a chicken walking through some concrete.

<iframe src="https://giphy.com/embed/29I0wgr3D2lZ9zA3mJ" width="432" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/29I0wgr3D2lZ9zA3mJ">via GIPHY</a></p>
