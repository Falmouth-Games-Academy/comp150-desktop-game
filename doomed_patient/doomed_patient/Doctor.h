//! Class for the Doctors.
/*!
This is a class for handling the doctors 
and storing any unique data.
It inherits from th GameObject class 
for any general data.
*/
#pragma once

#include "GameObject.h"

class LevelCell;

class Doctor : public GameObject
{
public:
	//!Constructor for the Doctor
	/*!
	*/
	Doctor(PatientGame* game, std::shared_ptr<LevelCell>cell);

	//!Destuctor for the Doctor
	/*!
	*/
	~Doctor();


};

