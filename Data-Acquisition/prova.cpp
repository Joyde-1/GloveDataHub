// TODO: Spiegazione del file

#include <iostream> //Output to console
#include <fstream>	//Output to file 
#include <string>	//String manipulation
#include <vector>	//Using arrays
#include <sstream>	//String tokenizer
#include <iomanip>	//Date format manipulation
#include <regex>	//Regular Expression
#include <windows.h>	//To "Force-Start" SenseCom Application

#include <thread>   //Tools for timestamp
#include <chrono>   //Tools for timestamp

// TODO: Spiegazione delle librerie importate

#include "Library.h" //Contains version information on SGCore / SGConnect Libraries
#include "SenseCom.h" //Functions to check scanning process - and to start it if need be.

#include "HapticGlove.h" //Haptic Glove Interfacing
#include "Tracking.h" //To calculate wrist location based on fixed hardware offsets.
#include "SG_FFBCmd.h" //force-feedback command(s)
#include "SG_BuzzCmd.h" //vibration command(s)

struct GloveData {
    bool isRightHand;
    SGCore::HandPose handPose;
};

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
		return -1;
	}
}

// TODO: Commentare meglio funzionamento della funzione
void writeCSVHeader(std::ofstream& file) {
	//file << "Timestamp;";
	file << "Date_Time;";

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

// TODO: Commentare meglio funzionamento della funzione
void writeGloveDataToCSV(std::ofstream& file, const std::string& data, bool sep) {  
    // Vettore di stringhe per memorizzare i valori separati   
    std::vector<std::string> data_values;     
    
    // Stream di input per leggere dalla stringa
    std::istringstream data_stream(data);    
    
    std::string token_value;     
    
    while (std::getline(data_stream, token_value, ',')) {      
          
      // Dividi ogni token in base agli spazi
      std::istringstream value_stream(token_value);         
      
      while (std::getline(value_stream, token_value, ' ')) {             

        // Ignora eventuali stringhe vuote
        if (!token_value.empty()) {                 
          // Aggiungi il token (valore) al vettore di stringhe                
          data_values.push_back(token_value);             
        }        
      }     
    }

	int i = 0;

	// Scrivere su file CSV i valori separati
    for (const auto& value : data_values) {   
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

int main(int argc, char* argv[])
{	
	// Check number of arguments
	if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <path_to_csv> <total_time>" << std::endl;
        return 1;
    }


    // TODO: Modificare i commenti perchè identici all'esempio della libreria
    //-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    // Ensuring connectivity

    // Connecting to SenseGlove devices is done in a separate "Connection Process" - contained in the SGConnect library.
    // We can test if this Connection Process is running on this PC. Usually, it runs inside SenseCom.
    // It's good practice to start this process if your user has not sone so yet.

	// Path of SenseCom Application (Update the path if you're running on another PC)
	// TODO: Fare in modo che questa path venga passata da terminale tramite args del main
    const char* sensecom_path = "C:\\Program Files\\SenseCom\\SenseCom.exe";
	
    bool connectionsActive = SGCore::SenseCom::ScanningActive();//returns true if SenseCom (or another program) has started the SenseGlove Communications Process.
	if (!connectionsActive)                                    // If this process is not running yet, we can "Force-Start" SenseCom. Provided it has run on this PC at least once.
	{
		std::cout << "SenseCom is not yet running. Without it, we cannot connect to SenseGlove devices." << std::endl;
		
		// Force-Start SenseCom application
		if (LaunchAndWaitForApp(sensecom_path) == -1) {
			std::cout << "Could not Start the SenseCom process. Error: " << GetLastError() << std::endl;

			return -1;
		} else {
			std::cout << "Successfully started SenseCom." << std::endl;
		}
	} else {
		std::cout << "SenseCom already in execution." << std::endl;
	}
	std::cout << ("-------------------------------------------------------------------------") << std::endl;
/* 
	// FROM LATER VERSION
    std::string username;
    std::regex format("^[A-Za-z]+_[A-Za-z]+$"); // Regola per Nome_Cognome

    while (true) {
        std::cout << "Inserisci il nome dell'utente (Nome_Cognome): ";
        std::getline(std::cin, username);

        // Verifica che il formato sia corretto
        if (std::regex_match(username, format)) {
            username += ".csv"; // Aggiunge l'estensione ".csv"
            break; // Esce dal ciclo se il formato è corretto
        } else {
            std::cout << "Formato non valido. Riprova rispettando la formattazione Nome_Cognome \n";
        }
    } */

	const char* path_to_csv = argv[1];
	
	// Apertura del file in scrittura
  	std::ofstream csvFile(path_to_csv);
	
	// DICHIARAZIONE VARIABILI CHE VERRANNO UTILIZZATE PER IL CALCOLO DEL TIMESTAMP ALL'INTERNO DEL WHILE:

	// Ottieni il timestamp di inizio
	auto start = std::chrono::high_resolution_clock::now();

	// Ottieni il timestamp di fine
	auto end = std::chrono::high_resolution_clock::now();

	// Calcola la differenza di tempo in secondi
	auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() / 1000.0;

	// Ottieni il tempo corrente
	auto now = std::chrono::system_clock::now();
	auto now_time = std::chrono::system_clock::to_time_t(now);
	auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()) % 1000;

	// Converti il tempo corrente in una struttura tm
    std::tm time_info = *std::localtime(&now_time);

	//int num_gloves = HandLayer::GlovesConnected();	// Number of gloves connected to your system
	std::vector<std::shared_ptr<SGCore::HapticGlove>> gloves = SGCore::HapticGlove::GetHapticGloves();
	connectionsActive = SGCore::SenseCom::ScanningActive();	//returns true if SenseCom (or another program) has started the SenseGlove Communications Process.
	
	// Controllo se il file è aperto correttamente
	if (csvFile.is_open()) {

        writeCSVHeader(csvFile);

		// Durata totale della prova. Se uguale a -1 la prova avrà un tempo infinito e si interromperà alla chiusura di SenseCom
		int total_time = std::atoi(argv[2]);

		// Contatore temporale in secondi
    	double timestamp = 0.000;

		// Verifica la prima iterazione
		bool first_iter = true;

		std::cout << "Num gloves:" << gloves.size() << std::endl;

		// Check if number of gloves is 2 and SenseCom is running
		bool check_condition = gloves.size() == 2 && connectionsActive;

		if (total_time != -1) {
			check_condition = gloves.size() == 2 && connectionsActive && timestamp <= total_time;
		}
		
		while (check_condition) {
			//std::vector<std::shared_ptr<SGCore::HapticGlove>> gloves = SGCore::HapticGlove::GetHapticGloves();

			// Iter each glove to get data
			for (const auto& glove : gloves) {

					GloveData data;

					data.isRightHand = glove->IsRight();

					if (glove->GetHandPose(data.handPose)) {

						if(data.isRightHand){
							if (first_iter == true) {
								// Ottieni il timestamp di inizio
       							start = std::chrono::high_resolution_clock::now();

								// Stampa su file il contatore temporale
								//csvFile << timestamp << ";";

								first_iter = false;
							} else {
								// Ottieni il timestamp di fine
        						end = std::chrono::high_resolution_clock::now();

								// Calcola la differenza di tempo in secondi
								duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() / 1000.0;

								// Ottieni il timestamp di inizio
								start = std::chrono::high_resolution_clock::now();

								// Aggiorna il contatore temporale
								timestamp += duration;

								// Stampa su file il contatore temporale
								//csvFile << timestamp << ";";
							}

							// Ottieni il tempo corrente
							now = std::chrono::system_clock::now();
							now_time = std::chrono::system_clock::to_time_t(now);
							ms = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()) % 1000;

							// Converti il tempo corrente in una struttura tm
							time_info = *std::localtime(&now_time);

							// Formatta e stampa la stringa
							//csvFile << std::put_time(&time_info, "%Y / %m / %d / %H : %M : %S.") << ms.count() << ";";
							csvFile << std::put_time(&time_info, "%Y%m%d_%H%M%S") << ";";
						}

						bool sep = true;					

						for (int i = 0; i < 5; i++) {
							for (int j = 0; j < 3; j++) {
								writeGloveDataToCSV(csvFile, data.handPose.handAngles[i][j].ToString(), sep);
								//writeGloveDataToCSV(csvFile, data.handPose.GetHandAngles()[i][j].ToString(), sep);
							}
						}

						for (int i = 0; i < 5; i++) {
							for (int j = 0; j < 4; j++) {
								writeGloveDataToCSV(csvFile, data.handPose.jointRotations[i][j].ToString(), sep);
								//writeGloveDataToCSV(csvFile, data.handPose.GetJointRotations()[i][j].ToString(), sep);
							}
						}

						for (int i = 0; i < 5; i++) {
							for (int j = 0; j < 4; j++) {
								if (i == 4 && j == 3) {
									sep = false;	
								}

								writeGloveDataToCSV(csvFile, data.handPose.jointPositions[i][j].ToString(), sep);
								//writeGloveDataToCSV(csvFile, data.handPose.GetJointPositions()[i][j].ToString(), sep);
							}
						}

						if (data.isRightHand) {
							csvFile << ";";
						} else {
							csvFile << std::endl;
						}
					}
        		}

			//num_gloves = HandLayer::GlovesConnected();
			std::vector<std::shared_ptr<SGCore::HapticGlove>> gloves = SGCore::HapticGlove::GetHapticGloves();
			connectionsActive = SGCore::SenseCom::ScanningActive();

			if (total_time != -1) {
				check_condition = gloves.size() == 2 && connectionsActive && timestamp <= total_time;
			} else {
				check_condition = gloves.size() == 2 && connectionsActive;
			}
		}

		csvFile.close();
		std::cout << "Data written to " << path_to_csv << std::endl;
	} else {
		std::cerr << "Error opening file CSV!" << std::endl;
	}
}