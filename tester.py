import subprocess
import logging
import os
import time
import threading
import sys
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_gradle_assemble_debug(project_dir):
    gradlew_path = os.path.join(project_dir, 'gradlew')

    logging.info('Checking if gradlew script exists and is executable.')

    # Check if gradlew exists and is executable
    if not os.path.isfile(gradlew_path):
        logging.error(f'gradlew script not found in {project_dir}')
        return

    if not os.access(gradlew_path, os.X_OK):
        logging.error(f'gradlew script is not executable. Please run chmod +x {gradlew_path}')
        return

    logging.info('gradlew script found and is executable.')

    # Check if Java is installed
    java_path = shutil.which("java")
    if java_path is None:
        logging.error("Java is not installed or not found in PATH.")
        return
    logging.info(f'Java found: {java_path}')

    # Set the command to run
    command = [gradlew_path, 'assembleDebug']

    logging.info('Starting the Gradle assembleDebug process.')

    start_time = time.time()

    try:
        # Change directory to the project directory
        logging.info(f'Changing directory to {project_dir}')
        os.chdir(project_dir)
        
        # Run the Gradle command
        logging.info(f'Running command: {" ".join(command)}')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Function to update the timer in the terminal
        def update_timer():
            logging.info('Starting timer.')
            while process.poll() is None:
                elapsed_time = time.time() - start_time
                minutes, seconds = divmod(int(elapsed_time), 60)
                sys.stdout.write(f'\rElapsed time: {minutes:02d}:{seconds:02d}')
                sys.stdout.flush()
                time.sleep(1)
            # Print final time once the process is done
            elapsed_time = time.time() - start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            sys.stdout.write(f'\rElapsed time: {minutes:02d}:{seconds:02d}\n')
            sys.stdout.flush()
            logging.info('Timer ended.')

        # Start the timer thread
        logging.info('Starting the timer thread.')
        timer_thread = threading.Thread(target=update_timer)
        timer_thread.start()

        # Read the output and error streams
        logging.info('Reading the Gradle command output and error streams.')
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                logging.info(f'Gradle Output: {output.strip()}')
            
            error = process.stderr.readline()
            if error == '' and process.poll() is not None:
                break
            if error:
                logging.error(f'Gradle Error: {error.strip()}')

        # Wait for the timer thread to finish
        logging.info('Waiting for the timer thread to finish.')
        timer_thread.join()

        # Get the return code
        return_code = process.poll()
        if return_code == 0:
            logging.info('Gradle assembleDebug finished successfully.')
        else:
            logging.error(f'Gradle assembleDebug failed with return code {return_code}.')

    except subprocess.CalledProcessError as e:
        logging.error(f'CalledProcessError occurred: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')

    elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    logging.info(f'Total execution time: {minutes:02d}:{seconds:02d}')

if __name__ == '__main__':
    # Set the path to your project directory
    project_directory = '/Users/georgemariusstanciu/Desktop/CBLConstruction'
    logging.info(f'Starting build process for project at: {project_directory}')
    run_gradle_assemble_debug(project_directory)
    logging.info('Build process completed.')
