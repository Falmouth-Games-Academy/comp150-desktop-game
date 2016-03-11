#include "stdafx.h"
#include "Doctor.h"
#include "PatientGame.h"
#include "LevelCell.h"

Doctor::Doctor(PatientGame* game, std::shared_ptr<LevelCell> cell)
//!This is to get the texture for the Doctor
/*!It inherits this from PatientGame.cpp
which then inherits from textures.h
*/
	: GameObject(game, game->getDoctorSprite())
{
	// Calculate the window position from the grid position
	centreX = cell->getCentreX();
	centreY = cell->getCentreY();
}


Doctor::~Doctor()
{
}
