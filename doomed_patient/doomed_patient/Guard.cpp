#include "stdafx.h"
#include "Guard.h"
#include "PatientGame.h"
#include "LevelCell.h"

Guard::Guard(PatientGame* game, std::shared_ptr<LevelCell> cell)
//!This is to get the texture for the Guard
/*!It inherits this from PatientGame.cpp
which then inherits from textures.h
*/
	: GameObject(game, game->getGuardSprite())
{
	// Calculate the window position from the grid position
	centreX = cell->getCentreX();
	centreY = cell->getCentreY();
}


Guard::~Guard()
{
}
