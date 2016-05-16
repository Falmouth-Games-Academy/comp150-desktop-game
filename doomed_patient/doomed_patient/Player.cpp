#include "stdafx.h"
#include "Player.h"
#include "PatientGame.h"
#include "LevelCell.h"
#include "Level.h"


Player::Player(PatientGame* game, VectorXY startCoordinates)
	: Character(game, startCoordinates, game->getPlayerSprite()),
	speed(2)
{
	currentCell = game->level.getCell(Level::PLAYER_START);
	centre = currentCell->getCentre();
}

void Player::resetPosition()
{
	centre = currentCell->getCentre();
	currentCell = game->level.getCell(Level::PLAYER_START);
}

void Player::move(Directions::Direction direction)
{
	
	movementCount++;
	if (movementCount >= movementDelay)
	{

		// Put collision detection here

		if (currentCell->getEdge(direction)->isWall())
		{
			return;
		}
		currentCell = game->level.getCell(currentCell->getCoordinates() + Directions::getDirectionVector(direction));
		centre = currentCell->getCentre();
		
		movementCount = 0;
	
	}
	//centre += Directions::getDirectionVector(direction) * speed;
}