//! Class for the Player.
/*!
This is a class for handling the Players
and storing any unique data.
It inherits from th GameObject class
for any general data.
*/
#pragma once

#include "GameObject.h"
#include "Level.h"
#include "Directions.h"

class LevelCell;

class Player : public GameObject
{
public:
	//!Constructor for the Player
	/*!
	*/
	Player(PatientGame* game, std::shared_ptr<LevelCell>cell);

	// Indicates the starting position of the player.
	static const int playerStartX = 0;
	static const int playerStartY = Level::GRID_SIZE_Y - 1;

	int speed;
	void move(Directions::Direction direction);
};