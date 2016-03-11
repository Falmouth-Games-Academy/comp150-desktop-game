#include "stdafx.h"
#include "Exit.h"
#include "PatientGame.h"
#include "LevelCell.h"


Exit::Exit(PatientGame* game, std::shared_ptr<LevelCell> cell)
	: GameObject(game, game->getExitSprite())
{
	// Calculate the window position from the grid position
	centreX = cell->getCentreX();
	centreY = cell->getCentreY();
}


Exit::~Exit()
{
}
