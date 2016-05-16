#include "stdafx.h"
#include "CellDoor.h"
#include "PatientGame.h"


CellDoor::CellDoor(Directions::Direction direction, std::shared_ptr<LevelCell> cell, PatientGame* game)
	: CellEdge(direction, cell)
{
	initialiseSprite(game);
	initialisePosition();

	//Currently creates locked doors randomly
	locked = rand() % 2;
}


CellDoor::~CellDoor()
{
}


void CellDoor::initialiseSprite(PatientGame* game)
{
	if (direction == Directions::Direction::NORTH || direction == Directions::Direction::SOUTH)
	{
		if (locked)
			sprite = game->getHorizontalLockedSprite();
		else
			sprite = game->getHorizontalDoorSprite();
	}

	else if (direction == Directions::Direction::EAST || direction == Directions::Direction::WEST)
	{
		if (locked)
			sprite = game->getVerticalDoorSprite();
		else
			sprite = game->getVerticalDoorSprite();
	}
}


