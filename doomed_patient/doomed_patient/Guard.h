//! Class for the Guards.
/*!
This is a class for handling the Guards
and storing any unique data.
It inherits from th GameObject class
for any general data.
*/
#pragma once

#include "GameObject.h"

class Guard : public GameObject
{
public:
	//!Constructor for the Guard
	/*!
	*/
	Guard(PatientGame* game);

	//!Destuctor for the Guard
	/*!
	*/
	~Guard();
};

