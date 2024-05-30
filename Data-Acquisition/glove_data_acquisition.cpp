 /**
 * @author
 * Giovanni Fanara
 * Alfredo Gioacchino MariaPio Vecchio
 * 
 * @date 2024-05-30
 */

#include <iostream> 		// Output to console
#include <fstream>			// Output to file 
#include <string>			// String manipulation
#include <vector>			// Using arrays
#include <sstream>			// String tokenizer
#include <iomanip>			// Date format manipulation
#include <regex>			// Regular Expression
#include <windows.h>		// To "Force-Start" SenseCom Application

#include <thread>   		// Tools for timestamp
#include <chrono>   		// Tools for timestamp

#include "Library.h" 		///< version information for SGCore / SGConnect libraries
#include "SenseCom.h" 		///< Functions to check SenseCom status
#include "HapticGlove.h"	///< Haptic Glove Interfacing

/**
 * @struct GloveData
 * @brief Include data related to a single haptic glove.
 */
struct GloveData {
    /**
     * @brief Indicate if the haptic glove is for right or left hand
     */
    bool isRightHand;

    /**
     * @brief Hand pose of the haptic glove
     */
    SGCore::HandPose handPose;
};

/**
 * @brief This function launch SenseCom process and wait until it is start correctly.
 * 
 * @param path_application SenseCom API path
*/
int LaunchAndWaitForApp(const char *path_application) {

	// Initialize process and startup info
	STARTUPINFO startup_info = { sizeof(STARTUPINFO) };
	startup_info.dwFlags = STARTF_USESHOWWINDOW;
	startup_info.wShowWindow = SW_SHOWNORMAL;
	PROCESS_INFORMATION process_info;

	// Create the process and check if SenseCom was open correctly
	if (CreateProcess(NULL, const_cast<char*>(path_application), NULL, NULL, FALSE, 0, NULL, NULL, &startup_info, &process_info)) {

		std::cout << "Starting SenseCom process..." << std::endl;

		// Wait until the process is ready for input
		WaitForInputIdle(process_info.hProcess, INFINITE);

		// Close the handles
		CloseHandle(process_info.hProcess);
		CloseHandle(process_info.hThread);

		return 0;
	} else {
		return 6;
	}
}

/**
 * @brief This fuction writes the column names in the first line of .CSV file
 * 
 * @param file File .CSV where is write the header
*/
void writeCSVHeader(std::ofstream& file) {
	file << "Date_Time;";

	// RIGHT HAND

	// Hand Angles
	file << "Hand_Angles_Thumb_0_x_Right;Hand_Angles_Thumb_0_y_Right;Hand_Angles_Thumb_0_z_Right;";
	file << "Hand_Angles_Thumb_1_x_Right;Hand_Angles_Thumb_1_y_Right;Hand_Angles_Thumb_1_z_Right;";
	file << "Hand_Angles_Thumb_2_x_Right;Hand_Angles_Thumb_2_y_Right;Hand_Angles_Thumb_2_z_Right;";

	file << "Hand_Angles_Index_0_x_Right;Hand_Angles_Index_0_t_Right;tHand_Angles_Index_0_z_Right;";
	file << "Hand_Angles_Index_1_x_Right;Hand_Angles_Index_1_y_Right;Hand_Angles_Index_1_z_Right;";
	file << "Hand_Angles_Index_2_x_Right;Hand_Angles_Index_2_y_Right;Hand_Angles_Index_2_z_Right;";

	file << "Hand_Angles_Middle_0_x_Right;Hand_Angles_Middle_0_y_Right;Hand_Angles_Middle_0_z_Right;";
	file << "Hand_Angles_Middle_1_x_Right;Hand_Angles_Middle_1_y_Right;Hand_Angles_Middle_1_z_Right;";
	file << "Hand_Angles_Middle_2_x_Right;Hand_Angles_Middle_2_y_Right;Hand_Angles_Middle_2_z_Right;";
	
	file << "Hand_Angles_Ring_0_x_Right;Hand_Angles_Ring_0_y_Right;Hand_Angles_Ring_0_z_Right;";
	file << "Hand_Angles_Ring_1_x_Right;Hand_Angles_Ring_1_y_Right;Hand_Angles_Ring_1_z_Right;";
	file << "Hand_Angles_Ring_2_x_Right;Hand_Angles_Ring_2_y_Right;Hand_Angles_Ring_2_z_Right;";
	
	file << "Hand_Angles_Pinky_0_x_Right;Hand_Angles_Pinky_0_y_Right;Hand_Angles_Pinky_0_z_Right;";
	file << "Hand_Angles_Pinky_1_x_Right;Hand_Angles_Pinky_1_y_Right;Hand_Angles_Pinky_1_z_Right;";
	file << "Hand_Angles_Pinky_2_x_Right;Hand_Angles_Pinky_2_y_Right;Hand_Angles_Pinky_2_z_Right;";

	// Joint Rotations
	file << "Joint_Rotations_Thumb_0_0_Right;Joint_Rotations_Thumb_0_1_Right;Joint_Rotations_Thumb_0_2_Right;Joint_Rotations_Thumb_0_3_Right;";
	file << "Joint_Rotations_Thumb_1_0_Right;Joint_Rotations_Thumb_1_1_Right;Joint_Rotations_Thumb_1_2_Right;Joint_Rotations_Thumb_1_3_Right;";
	file << "Joint_Rotations_Thumb_2_0_Right;Joint_Rotations_Thumb_2_1_Right;Joint_Rotations_Thumb_2_2_Right;Joint_Rotations_Thumb_2_3_Right;";
	file << "Joint_Rotations_Thumb_3_0_Right;Joint_Rotations_Thumb_3_1_Right;Joint_Rotations_Thumb_3_2_Right;Joint_Rotations_Thumb_3_3_Right;";
	
	file << "Joint_Rotations_Index_0_0_Right;Joint_Rotations_Index_0_1_Right;Joint_Rotations_Index_0_2_Right;Joint_Rotations_Index_0_3_Right;";
	file << "Joint_Rotations_Index_1_0_Right;Joint_Rotations_Index_1_1_Right;Joint_Rotations_Index_1_2_Right;Joint_Rotations_Index_1_3_Right;";
	file << "Joint_Rotations_Index_2_0_Right;Joint_Rotations_Index_2_1_Right;Joint_Rotations_Index_2_2_Right;Joint_Rotations_Index_2_3_Right;";
	file << "Joint_Rotations_Index_3_0_Right;Joint_Rotations_Index_3_1_Right;Joint_Rotations_Index_3_2_Right;Joint_Rotations_Index_3_3_Right;";
	
	file << "Joint_Rotations_Middle_0_0_Right;Joint_Rotations_Middle_0_1_Right;Joint_Rotations_Middle_0_2_Right;Joint_Rotations_Middle_0_3_Right;";
	file << "Joint_Rotations_Middle_1_0_Right;Joint_Rotations_Middle_1_1_Right;Joint_Rotations_Middle_1_2_Right;Joint_Rotations_Middle_1_3_Right;";
	file << "Joint_Rotations_Middle_2_0_Right;Joint_Rotations_Middle_2_1_Right;Joint_Rotations_Middle_2_2_Right;Joint_Rotations_Middle_2_3_Right;";
	file << "Joint_Rotations_Middle_3_0_Right;Joint_Rotations_Middle_3_1_Right;Joint_Rotations_Middle_3_2_Right;Joint_Rotations_Middle_3_3_Right;";
	
	file << "Joint_Rotations_Ring_0_0_Right;Joint_Rotations_Ring_0_1_Right;Joint_Rotations_Ring_0_2_Right;Joint_Rotations_Ring_0_3_Right;";
	file << "Joint_Rotations_Ring_1_0_Right;Joint_Rotations_Ring_1_1_Right;Joint_Rotations_Ring_1_2_Right;Joint_Rotations_Ring_1_3_Right;";
	file << "Joint_Rotations_Ring_2_0_Right;Joint_Rotations_Ring_2_1_Right;Joint_Rotations_Ring_2_2_Right;Joint_Rotations_Ring_2_3_Right;";
	file << "Joint_Rotations_Ring_3_0_Right;Joint_Rotations_Ring_3_1_Right;Joint_Rotations_Ring_3_2_Right;Joint_Rotations_Ring_3_3_Right;";
	
	file << "Joint_Rotations_Pinky_0_0_Right;Joint_Rotations_Pinky_0_1_Right;Joint_Rotations_Pinky_0_2_Right;Joint_Rotations_Pinky_0_3_Right;";
	file << "Joint_Rotations_Pinky_1_0_Right;Joint_Rotations_Pinky_1_1_Right;Joint_Rotations_Pinky_1_2_Right;Joint_Rotations_Pinky_1_3_Right;";
	file << "Joint_Rotations_Pinky_2_0_Right;Joint_Rotations_Pinky_2_1_Right;Joint_Rotations_Pinky_2_2_Right;Joint_Rotations_Pinky_2_3_Right;";
	file << "Joint_Rotations_Pinky_3_0_Right;Joint_Rotations_Pinky_3_1_Right;Joint_Rotations_Pinky_3_2_Right;Joint_Rotations_Pinky_3_3_Right;";

	// Joint Positions
	file << "Joint_Positions_Thumb_0_0_Right;Joint_Positions_Thumb_0_1_Right;Joint_Positions_Thumb_0_2_Right;";
	file << "Joint_Positions_Thumb_1_0_Right;Joint_Positions_Thumb_1_1_Right;Joint_Positions_Thumb_1_2_Right;";
	file << "Joint_Positions_Thumb_2_0_Right;Joint_Positions_Thumb_2_1_Right;Joint_Positions_Thumb_2_2_Right;";
	file << "Joint_Positions_Thumb_3_0_Right;Joint_Positions_Thumb_3_1_Right;Joint_Positions_Thumb_3_2_Right;";
	
	file << "Joint_Positions_Index_0_0_Right;Joint_Positions_Index_0_1_Right;Joint_Positions_Index_0_2_Right;";
	file << "Joint_Positions_Index_1_0_Right;Joint_Positions_Index_1_1_Right;Joint_Positions_Index_1_2_Right;";
	file << "Joint_Positions_Index_2_0_Right;Joint_Positions_Index_2_1_Right;Joint_Positions_Index_2_2_Right;";
	file << "Joint_Positions_Index_3_0_Right;Joint_Positions_Index_3_1_Right;Joint_Positions_Index_3_2_Right;";
	
	file << "Joint_Positions_Middle_0_0_Right;Joint_Positions_Middle_0_1_Right;Joint_Positions_Middle_0_2_Right;";
	file << "Joint_Positions_Middle_1_0_Right;Joint_Positions_Middle_1_1_Right;Joint_Positions_Middle_1_2_Right;";
	file << "Joint_Positions_Middle_2_0_Right;Joint_Positions_Middle_2_1_Right;Joint_Positions_Middle_2_2_Right;";
	file << "Joint_Positions_Middle_3_0_Right;Joint_Positions_Middle_3_1_Right;Joint_Positions_Middle_3_2_Right;";
	
	file << "Joint_Positions_Ring_0_0_Right;Joint_Rotations_Ring_0_1_Right;Joint_Positions_Ring_0_2_Right;";
	file << "Joint_Positions_Ring_1_0_Right;Joint_Positions_Ring_1_1_Right;Joint_Positions_Ring_1_2_Right;";
	file << "Joint_Positions_Ring_2_0_Right;Joint_Positions_Ring_2_1_Right;Joint_Positions_Ring_2_2_Right;";
	file << "Joint_Positions_Ring_3_0_Right;Joint_Positions_Ring_3_1_Right;Joint_Positions_Ring_3_2_Right;";
	
	file << "Joint_Positions_Pinky_0_0_Right;Joint_Positions_Pinky_0_1_Right;Joint_Positions_Pinky_0_2_Right;";
	file << "Joint_Positions_Pinky_1_0_Right;Joint_Positions_Pinky_1_1_Right;Joint_Positions_Pinky_1_2_Right;";
	file << "Joint_Positions_Pinky_2_0_Right;Joint_Positions_Pinky_2_1_Right;Joint_Positions_Pinky_2_2_Right;";
	file << "Joint_Positions_Pinky_3_0_Right;Joint_Positions_Pinky_3_1_Right;Joint_Positions_Pinky_3_2_Right;";

	// LEFT HAND

	// Hand Angles
	file << "Hand_Angles_Thumb_0_x_Left;Hand_Angles_Thumb_0_y_Left;Hand_Angles_Thumb_0_z_Left;";
	file << "Hand_Angles_Thumb_1_x_Left;Hand_Angles_Thumb_1_y_Left;Hand_Angles_Thumb_1_z_Left;";
	file << "Hand_Angles_Thumb_2_x_Left;Hand_Angles_Thumb_2_y_Left;Hand_Angles_Thumb_2_z_Left;";

	file << "Hand_Angles_Index_0_x_Left;Hand_Angles_Index_0_t_Left;tHand_Angles_Index_0_z_Left;";
	file << "Hand_Angles_Index_1_x_Left;Hand_Angles_Index_1_y_Left;Hand_Angles_Index_1_z_Left;";
	file << "Hand_Angles_Index_2_x_Left;Hand_Angles_Index_2_y_Left;Hand_Angles_Index_2_z_Left;";

	file << "Hand_Angles_Middle_0_x_Left;Hand_Angles_Middle_0_y_Left;Hand_Angles_Middle_0_z_Left;";
	file << "Hand_Angles_Middle_1_x_Left;Hand_Angles_Middle_1_y_Left;Hand_Angles_Middle_1_z_Left;";
	file << "Hand_Angles_Middle_2_x_Left;Hand_Angles_Middle_2_y_Left;Hand_Angles_Middle_2_z_Left;";
	
	file << "Hand_Angles_Ring_0_x_Left;Hand_Angles_Ring_0_y_Left;Hand_Angles_Ring_0_z_Left;";
	file << "Hand_Angles_Ring_1_x_Left;Hand_Angles_Ring_1_y_Left;Hand_Angles_Ring_1_z_Left;";
	file << "Hand_Angles_Ring_2_x_Left;Hand_Angles_Ring_2_y_Left;Hand_Angles_Ring_2_z_Left;";
	
	file << "Hand_Angles_Pinky_0_x_Left;Hand_Angles_Pinky_0_y_Left;Hand_Angles_Pinky_0_z_Left;";
	file << "Hand_Angles_Pinky_1_x_Left;Hand_Angles_Pinky_1_y_Left;Hand_Angles_Pinky_1_z_Left;";
	file << "Hand_Angles_Pinky_2_x_Left;Hand_Angles_Pinky_2_y_Left;Hand_Angles_Pinky_2_z_Left;";

	// Joint Rotations
	file << "Joint_Rotations_Thumb_0_0_Left;Joint_Rotations_Thumb_0_1_Left;Joint_Rotations_Thumb_0_2_Left;Joint_Rotations_Thumb_0_3_Left;";
	file << "Joint_Rotations_Thumb_1_0_Left;Joint_Rotations_Thumb_1_1_Left;Joint_Rotations_Thumb_1_2_Left;Joint_Rotations_Thumb_1_3_Left;";
	file << "Joint_Rotations_Thumb_2_0_Left;Joint_Rotations_Thumb_2_1_Left;Joint_Rotations_Thumb_2_2_Left;Joint_Rotations_Thumb_2_3_Left;";
	file << "Joint_Rotations_Thumb_3_0_Left;Joint_Rotations_Thumb_3_1_Left;Joint_Rotations_Thumb_3_2_Left;Joint_Rotations_Thumb_3_3_Left;";
	
	file << "Joint_Rotations_Index_0_0_Left;Joint_Rotations_Index_0_1_Left;Joint_Rotations_Index_0_2_Left;Joint_Rotations_Index_0_3_Left;";
	file << "Joint_Rotations_Index_1_0_Left;Joint_Rotations_Index_1_1_Left;Joint_Rotations_Index_1_2_Left;Joint_Rotations_Index_1_3_Left;";
	file << "Joint_Rotations_Index_2_0_Left;Joint_Rotations_Index_2_1_Left;Joint_Rotations_Index_2_2_Left;Joint_Rotations_Index_2_3_Left;";
	file << "Joint_Rotations_Index_3_0_Left;Joint_Rotations_Index_3_1_Left;Joint_Rotations_Index_3_2_Left;Joint_Rotations_Index_3_3_Left;";
	
	file << "Joint_Rotations_Middle_0_0_Left;Joint_Rotations_Middle_0_1_Left;Joint_Rotations_Middle_0_2_Left;Joint_Rotations_Middle_0_3_Left;";
	file << "Joint_Rotations_Middle_1_0_Left;Joint_Rotations_Middle_1_1_Left;Joint_Rotations_Middle_1_2_Left;Joint_Rotations_Middle_1_3_Left;";
	file << "Joint_Rotations_Middle_2_0_Left;Joint_Rotations_Middle_2_1_Left;Joint_Rotations_Middle_2_2_Left;Joint_Rotations_Middle_2_3_Left;";
	file << "Joint_Rotations_Middle_3_0_Left;Joint_Rotations_Middle_3_1_Left;Joint_Rotations_Middle_3_2_Left;Joint_Rotations_Middle_3_3_Left;";
	
	file << "Joint_Rotations_Ring_0_0_Left;Joint_Rotations_Ring_0_1_Left;Joint_Rotations_Ring_0_2_Left;Joint_Rotations_Ring_0_3_Left;";
	file << "Joint_Rotations_Ring_1_0_Left;Joint_Rotations_Ring_1_1_Left;Joint_Rotations_Ring_1_2_Left;Joint_Rotations_Ring_1_3_Left;";
	file << "Joint_Rotations_Ring_2_0_Left;Joint_Rotations_Ring_2_1_Left;Joint_Rotations_Ring_2_2_Left;Joint_Rotations_Ring_2_3_Left;";
	file << "Joint_Rotations_Ring_3_0_Left;Joint_Rotations_Ring_3_1_Left;Joint_Rotations_Ring_3_2_Left;Joint_Rotations_Ring_3_3_Left;";
	
	file << "Joint_Rotations_Pinky_0_0_Left;Joint_Rotations_Pinky_0_1_Left;Joint_Rotations_Pinky_0_2_Left;Joint_Rotations_Pinky_0_3_Left;";
	file << "Joint_Rotations_Pinky_1_0_Left;Joint_Rotations_Pinky_1_1_Left;Joint_Rotations_Pinky_1_2_Left;Joint_Rotations_Pinky_1_3_Left;";
	file << "Joint_Rotations_Pinky_2_0_Left;Joint_Rotations_Pinky_2_1_Left;Joint_Rotations_Pinky_2_2_Left;Joint_Rotations_Pinky_2_3_Left;";
	file << "Joint_Rotations_Pinky_3_0_Left;Joint_Rotations_Pinky_3_1_Left;Joint_Rotations_Pinky_3_2_Left;Joint_Rotations_Pinky_3_3_Left;";

	// Joint Positions
	file << "Joint_Positions_Thumb_0_0_Left;Joint_Positions_Thumb_0_1_Left;Joint_Positions_Thumb_0_2_Left;";
	file << "Joint_Positions_Thumb_1_0_Left;Joint_Positions_Thumb_1_1_Left;Joint_Positions_Thumb_1_2_Left;";
	file << "Joint_Positions_Thumb_2_0_Left;Joint_Positions_Thumb_2_1_Left;Joint_Positions_Thumb_2_2_Left;";
	file << "Joint_Positions_Thumb_3_0_Left;Joint_Positions_Thumb_3_1_Left;Joint_Positions_Thumb_3_2_Left;";
	
	file << "Joint_Positions_Index_0_0_Left;Joint_Positions_Index_0_1_Left;Joint_Positions_Index_0_2_Left;";
	file << "Joint_Positions_Index_1_0_Left;Joint_Positions_Index_1_1_Left;Joint_Positions_Index_1_2_Left;";
	file << "Joint_Positions_Index_2_0_Left;Joint_Positions_Index_2_1_Left;Joint_Positions_Index_2_2_Left;";
	file << "Joint_Positions_Index_3_0_Left;Joint_Positions_Index_3_1_Left;Joint_Positions_Index_3_2_Left;";
	
	file << "Joint_Positions_Middle_0_0_Left;Joint_Positions_Middle_0_1_Left;Joint_Positions_Middle_0_2_Left;";
	file << "Joint_Positions_Middle_1_0_Left;Joint_Positions_Middle_1_1_Left;Joint_Positions_Middle_1_2_Left;";
	file << "Joint_Positions_Middle_2_0_Left;Joint_Positions_Middle_2_1_Left;Joint_Positions_Middle_2_2_Left;";
	file << "Joint_Positions_Middle_3_0_Left;Joint_Positions_Middle_3_1_Left;Joint_Positions_Middle_3_2_Left;";
	
	file << "Joint_Positions_Ring_0_0_Left;Joint_Rotations_Ring_0_1_Left;Joint_Positions_Ring_0_2_Left;";
	file << "Joint_Positions_Ring_1_0_Left;Joint_Positions_Ring_1_1_Left;Joint_Positions_Ring_1_2_Left;";
	file << "Joint_Positions_Ring_2_0_Left;Joint_Positions_Ring_2_1_Left;Joint_Positions_Ring_2_2_Left;";
	file << "Joint_Positions_Ring_3_0_Left;Joint_Positions_Ring_3_1_Left;Joint_Positions_Ring_3_2_Left;";
	
	file << "Joint_Positions_Pinky_0_0_Left;Joint_Positions_Pinky_0_1_Left;Joint_Positions_Pinky_0_2_Left;";
	file << "Joint_Positions_Pinky_1_0_Left;Joint_Positions_Pinky_1_1_Left;Joint_Positions_Pinky_1_2_Left;";
	file << "Joint_Positions_Pinky_2_0_Left;Joint_Positions_Pinky_2_1_Left;Joint_Positions_Pinky_2_2_Left;";
	file << "Joint_Positions_Pinky_3_0_Left;Joint_Positions_Pinky_3_1_Left;Joint_Positions_Pinky_3_2_Left" << std::endl;		
}

/**
 * @brief This fuction write the haptic glove data to a .CSV file.
 * 
 * @param file The file .CSV where data are write
 * @param data String with the data separated by ','
 * @param sep When it is True, it put a ';' when a value is write on the .CSV file
*/
void writeGloveDataToCSV(std::ofstream& file, const std::string& data, bool sep) {  
    // Strings vector to save separated values   
    std::vector<std::string> data_values;     
    
    // Input stream to read from the string
    std::istringstream data_stream(data);    
    
    std::string token_value;     
    
	// Iter each token in the input stream
    while (std::getline(data_stream, token_value, ',')) {      
          
      // Divide each token by spaces
      std::istringstream value_stream(token_value);         
      
      while (std::getline(value_stream, token_value, ' ')) {             

        // Ignore empty strings
        if (!token_value.empty()) {                 
          // Add token (value) to string vector                
          data_values.push_back(token_value);             
        }        
      }     
    }

	int i = 0;

	// Write on .CSV file the separated values
    for (const auto& value : data_values) {   
		
		// Check if is the last value to write in this line
		if (sep == true) {
			file << value << ";";
		} else {
			if (i != 2) {
				file << value << ";";
			} else {
				file << value;
			}
		}

		i++;
    }
}

/**
 * @brief Main of the programm.
 * 
 * @param argc Number of arguments
 * @param argv List of arguments that are: path to csv and total time
*/
int main(int argc, char* argv[])
{	
	// Check number of arguments
	if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <path_to_csv> <total_time>" << std::endl;
        return 2;
    }

    const char* sensecom_path = "C:\\Program Files\\SenseCom\\SenseCom.exe"; ///< Path of SenseCom Application (Update the path if you're running on another PC)
	
    bool connectionsActive = SGCore::SenseCom::ScanningActive(); ///< returns true if SenseCom is active
	
	// Check if SenseCom is active
	if (!connectionsActive)
	{
		// Force-Start SenseCom application
		if (LaunchAndWaitForApp(sensecom_path) == 6) {
			std::cout << "Could not Start the SenseCom process. Error: " << GetLastError() << std::endl;

			return 6;
		} else {
			std::cout << "Successfully started SenseCom." << std::endl;
		}
	} else {
		std::cout << "SenseCom already in execution." << std::endl;
	}

	const char* path_to_csv = argv[1]; ///< Path to .CSV file where data are write
	
	// Opening the file for writing
  	std::ofstream csvFile(path_to_csv);
	
	// VARIABLE DECLARATION TO BE USED TO CALCULATE THE TIMESTAMP WITHIN WHILE:

	// Get the start timestamp
	auto start = std::chrono::high_resolution_clock::now();

	// Get the last timestamp
	auto end = std::chrono::high_resolution_clock::now();

	// Calcola la differenza di tempo in secondi
	auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() / 1000.0;

	// Get the current time
	auto now = std::chrono::system_clock::now();
	auto now_time = std::chrono::system_clock::to_time_t(now);
	auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()) % 1000;

	// Convert current time in a tm structure
    std::tm time_info = *std::localtime(&now_time);

	// Get the haptic gloves objects
	std::vector<std::shared_ptr<SGCore::HapticGlove>> gloves = SGCore::HapticGlove::GetHapticGloves();

	// Get the SenseCom status
	connectionsActive = SGCore::SenseCom::ScanningActive();

	int total_time = std::atoi(argv[2]); ///< Total time duration of the data acquisition. If it is ugual to -1, the time is unlimited

	// timestamp in seconds
	double timestamp = 0.000;
	
	// Check if the file is correctly opened
	if (csvFile.is_open()) {
		
		// Write the column names on the .CSV file
        writeCSVHeader(csvFile);

		bool first_iter = true;	///< Verify the first iteration of the data acquisition loop

		std::cout << "Num gloves:" << gloves.size() << std::endl;

		// Check if number of gloves is 2 and SenseCom is running
		bool check_condition = gloves.size() == 2 && connectionsActive; ///< Essential condition to get data from haptic gloves

		// Check if the data acquisition time is unlimited
		if (total_time != -1) {
			// Update check condition with a control to the time
			check_condition = gloves.size() == 2 && connectionsActive && timestamp <= total_time;
		}
		
		// Iter until the check condition is satisfied
		while (check_condition) {

			// Iter each glove to get data
			for (const auto& glove : gloves) {

				GloveData data;

				// Get True if the current glove is right or False if it is left
				data.isRightHand = glove->IsRight();

				// Get the hand pose of the aptic glove
				if (glove->GetHandPose(data.handPose)) {
					
					// Check if the current hand is right or left
					if(data.isRightHand){
						// Check if it is the first iteration
						if (first_iter == true) {
							// Get the first timestamp
							start = std::chrono::high_resolution_clock::now();

							first_iter = false;
						} else {
							// Get the current timestamp
							end = std::chrono::high_resolution_clock::now();

							// Calculate the time difference in seconds
							duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() / 1000.0;

							// Get the time when data acquisition is started
							start = std::chrono::high_resolution_clock::now();

							// Update the timestamp
							timestamp += duration;
						}

						// Get the current time
						now = std::chrono::system_clock::now();
						now_time = std::chrono::system_clock::to_time_t(now);
						ms = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()) % 1000;

						// Convert the current time in a tm structure
						time_info = *std::localtime(&now_time);

						// Write the time in Date_Time column
						csvFile << std::put_time(&time_info, "%Y%m%d_%H%M%S") << ";";
					}

					bool sep = true;	///< Used when there is the last value to be written in the .CSV file

					// Iter the 3D Vectors with the hand angles and save these values to .CSV file
					for (int i = 0; i < 5; i++) {
						for (int j = 0; j < 3; j++) {
							writeGloveDataToCSV(csvFile, data.handPose.handAngles[i][j].ToString(), sep);
						}
					}

					// Iter the 3D Vectors with the joint rotations and save these values to .CSV file
					for (int i = 0; i < 5; i++) {
						for (int j = 0; j < 4; j++) {
							writeGloveDataToCSV(csvFile, data.handPose.jointRotations[i][j].ToString(), sep);
						}
					}

					// Iter the 3D Vectors with the joint positions and save these values to .CSV file
					for (int i = 0; i < 5; i++) {
						for (int j = 0; j < 4; j++) {
							if (i == 4 && j == 3) {
								sep = false;	
							}

							writeGloveDataToCSV(csvFile, data.handPose.jointPositions[i][j].ToString(), sep);
						}
					}

					// Check if the data are captured from the right or left and, in case is left, put a line break
					if (data.isRightHand) {
						csvFile << ";";
					} else {
						csvFile << std::endl;
					}
				}
        	}

			// Get the haptic gloves objects
			std::vector<std::shared_ptr<SGCore::HapticGlove>> gloves = SGCore::HapticGlove::GetHapticGloves();

			// Get the SenseCom status
			connectionsActive = SGCore::SenseCom::ScanningActive();

			// Update the check_condition
			if (total_time != -1) {
				check_condition = gloves.size() == 2 && connectionsActive && timestamp <= total_time;
			} else {
				check_condition = gloves.size() == 2 && connectionsActive;
			}
		}

		// Close the file
		csvFile.close();
		std::cout << "Data written to " << path_to_csv << std::endl;
	} else {
		std::cerr << "Error opening file CSV!" << std::endl;

		return 3;
	}

	// Check the conditions
	if (gloves.size != 2) {
		return 4;
	}

	if (!connectionsActive) {
		return 5;
	}

	if (total_time != -1) {
		if (timestamp > total_time) {
			return 0;
		}
	} else {
		return 7;
	}
}