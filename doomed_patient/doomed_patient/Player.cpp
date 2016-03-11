#include "stdafx.h"
#include "Player.h"
#include "PatientGame.h"
#include "LevelCell.h"

Player::Player(PatientGame* game, std::shared_ptr<LevelCell> cell)
//!This is to get the texture for the Doctor
/*!It inherits this from PatientGame.cpp
which then inherits from textures.h
*/
	: GameObject(game, game->getPlayerSprite()),
	speed(2)
{
	// Calculate the window position from the grid position
	centreX = cell->getCentreX();
	centreY = cell->getCentreY();
}

void Player::move(Directions::Direction direction)
{
	centreX += Directions::getDirectionVector(direction).x * speed;
	centreY += Directions::getDirectionVector(direction).y * speed;
}